import re
import argparse
import toml
import subprocess
from os import path, listdir
from sys import stderr
from getpass import getuser


ALACRITTY_PATH = "/home/" + getuser() + "/.config/alacritty/"
ALACRITTY_CONFIG_PATH = path.join(ALACRITTY_PATH, "alacritty.toml")

QTILE_PATH = "/home/" + getuser() + "/.config/qtile"
QTILE_CONFIG_THEME_PATH = path.join(QTILE_PATH, "configs/theme.py")

NEOVIM_CONFIG_PATH = "/home/" + getuser() + "/.config/nvim/"
NEOVIM_THEMES = path.join(NEOVIM_CONFIG_PATH, "themes.toml")
NEOVIM_CONFIG_THEME = path.join(NEOVIM_CONFIG_PATH, "lua/plugins/colors.lua")
NEOVIM_LUALINE = path.join(NEOVIM_CONFIG_PATH, "lua/plugins/lualine.lua")


class ThemeDoesNotExist(Exception):
    pass


class FontDoesNotExist(Exception):
    pass


def main():
    args = cli()
    try:
        pylook(args.theme, args.font, args.opacity, args.size)
    except ThemeDoesNotExist as e:
        print(e, file=stderr)
        exit(1)
    except FontDoesNotExist as e:
        print(e, file=stderr)
        exit(1)


def cli() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="pycolor",
        description="Command for changing system and alacritty settings",
    )
    parser.add_argument("-t", "--theme", help="Theme for the system and alacritty")
    parser.add_argument("-f", "--font", help="Font for alacritty")
    parser.add_argument("-s", "--size", help="Size of font of alacritty", type=float)
    parser.add_argument("-o", "--opacity", help="Opacity of alacritty", type=float)

    return parser.parse_args()


def pylook(theme: str, font: str, opacity: float, fontsize: float):
    alacritty_config = open_alacritty_config()

    if theme:
        change_theme(theme, alacritty_config)
    if font:
        change_font(font, alacritty_config)
    if opacity:
        change_opacity(opacity, alacritty_config)
    if fontsize:
        change_fontsize(fontsize, alacritty_config)

    close_alacritty_config(alacritty_config)


def open_alacritty_config():
    with open(ALACRITTY_CONFIG_PATH, "r") as file:
        alacritty_config = toml.load(file)
    return alacritty_config


def change_theme(theme: str, alacritty_config):
    system_theme = theme + ".toml"
    change_system_theme(system_theme)
    terminal_theme = theme + ".toml"
    change_terminal_theme(terminal_theme, alacritty_config)
    change_neovim_theme(theme)


def change_system_theme(theme: str):
    """Cambia el tema de la barra de qtile"""
    if theme not in listdir(path.join(QTILE_PATH, "themes")):
        raise ThemeDoesNotExist("The theme introduced is not in theme's directory")
    # Abrimos el archivo
    with open(QTILE_CONFIG_THEME_PATH, "r") as file:
        qtile_config = file.read()
    # Buscamos el .json de los temas y lo sustituimos
    pattern = r"([\w\-]+\.toml)"
    new_qtile_config = re.sub(pattern, theme, qtile_config)
    with open(QTILE_CONFIG_THEME_PATH, "w") as archivo:
        archivo.write(new_qtile_config)
    # Qtile configuration reaload when it receives SIGUSR1
    subprocess.run(["pkill", "-SIGUSR1", "qtile"])


def change_terminal_theme(theme: str, alacritty_config):
    """Cambia el tema de alacritty"""
    if theme not in listdir(path.join(ALACRITTY_PATH, "themes")):
        raise ThemeDoesNotExist("The theme introduced is not in theme's directory")
    # Abrimos el tema
    theme_path = path.join(ALACRITTY_PATH, "themes/", theme)
    with open(theme_path, "r") as file:
        colors = toml.load(file)
    # Recorremos los colores y modificamos
    for color_type in colors["colors"]:
        for color in colors["colors"][color_type]:
            alacritty_config["colors"][color_type][color] = colors["colors"][
                color_type
            ][color]


def change_neovim_theme(theme: str):
    with open(NEOVIM_THEMES, "r") as file:
        themes = toml.load(file)

    with open(NEOVIM_CONFIG_THEME, "r") as file:
        neovim_colors = file.read()

    with open(NEOVIM_LUALINE, "r") as file:
        lualine = file.read()

    plugin_regex = r'"(.*?)"'
    name_regex = r'name\s*=\s*"(.*?)"'
    colorscheme_regex = r'vim\.cmd\.colorscheme\("(.*?)"\)'
    lualine_regex = r"lualine.themes.(.)+"

    plugin = '"' + themes[theme]["plugin"] + '"'
    name = 'name = "' + theme + '"'
    colorscheme = 'vim.cmd.colorscheme("' + theme + '")'
    theme_lualine = "lualine.themes." + theme + '"),'

    resultado1 = re.sub(plugin_regex, plugin, neovim_colors, count=1)
    resultado2 = re.sub(name_regex, name, resultado1)
    resultado3 = re.sub(colorscheme_regex, colorscheme, resultado2)

    with open(NEOVIM_CONFIG_THEME, "w") as file:
        file.write(resultado3)

    new_lualine = re.sub(lualine_regex, theme_lualine, lualine)

    with open(NEOVIM_LUALINE, "w") as file:
        file.write(new_lualine)


def change_font(font: str, alacritty_config):
    """Cambia la fuente empleada en alacritty"""
    # Fonts path
    fonts_path = path.join(ALACRITTY_PATH, "fonts.toml")
    # Cogemos las fuentes
    with open(fonts_path, "r") as file:
        fonts = toml.load(file)
    if font not in fonts:
        raise FontDoesNotExist(
            "The font introduced is not in font's file \n"
            + f"The available fonts are: {list(fonts.keys())}"
        )
    # Cambiamos la fuente por la introducida
    alacritty_config["font"]["bold"]["family"] = fonts[font][font][0]
    alacritty_config["font"]["italic"]["family"] = fonts[font][font][1]
    alacritty_config["font"]["normal"]["family"] = fonts[font][font][2]


def change_opacity(opacity: float, alacritty_config):
    """Cambia la opacidad de alacritty"""
    # Abrimos el archivo
    # Sustituimos la opacidad
    alacritty_config["window"]["opacity"] = opacity


def change_fontsize(fontsize: float, alacritty_config):
    """Cambia el tamano de letra de alacritty"""
    # Abrimos el archivo
    # Sustituimos el tamano de letra
    alacritty_config["font"]["size"] = fontsize


def close_alacritty_config(alacritty_config):
    with open(ALACRITTY_CONFIG_PATH, "w") as file:
        toml.dump(alacritty_config, file)


if __name__ == "__main__":
    main()
