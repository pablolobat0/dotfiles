import json, re, argparse, yaml
from os import path, listdir
from sys import stderr
from getpass import getuser


class ThemeDoesNotExist(Exception):
    pass


class FontDoesNotExist(Exception):
    pass


def change_system_theme(theme: str):
    '''Cambia el tema de la barra de qtile'''
     # Ruta de qtile
    qtile_path = "/home/" + getuser() + "/.config/qtile"
    if theme not in listdir(path.join(qtile_path, "themes")):
        raise ThemeDoesNotExist("The theme introduced is not in theme's directory")
    qtile_config_path = path.join(qtile_path, "config.py")
    # Abrimos el archivo
    with open(qtile_config_path, "r") as file:
        contenido = file.read()
    # Buscamos el .json de los temas y lo sustituimos
    pattern = r'([\w\-]+\.json)'
    contenido_modificado = re.sub(pattern, theme, contenido)
    with open(qtile_config_path, "w") as archivo:
        archivo.write(contenido_modificado)  


def change_terminal_theme(theme: str):
    '''Cambia el tema de alacritty'''
     # Ruta de alacritty
    alacritty_path = "/home/" + getuser() + "/.config/alacritty/"
    if theme not in listdir(path.join(alacritty_path, "themes")):
        raise ThemeDoesNotExist("The theme introduced is not in theme's directory")
    # Abrimos el archivo de configuracion
    alacritty_config_path = path.join(alacritty_path, "alacritty.yml")
    with open(alacritty_config_path, "r") as file:
        contenido = yaml.load(file, Loader=yaml.FullLoader)
    # Abrimos el tema
    theme_path = path.join(alacritty_path, "themes/", theme)
    with open(theme_path, "r") as file:
        colors = yaml.load(file, Loader=yaml.FullLoader)
    # Recorremos los colores y modificamos
    for color_type in colors["colors"]:
        for color in colors["colors"][color_type]:
            contenido["colors"][color_type][color] = colors["colors"][color_type][color]
    with open(alacritty_config_path, "w") as file:
        yaml.dump(contenido, file)  

def change_theme(theme: str):
    system_theme = theme + ".json"
    change_system_theme(system_theme)
    terminal_theme = theme + ".yml"
    change_terminal_theme(terminal_theme)


def change_opacity(opacity: float):
    '''Cambia la opacidad de alacritty'''
    # Ruta de alacritty
    alacritty_config_path = "/home/" + getuser() + "/.config/alacritty/alacritty.yml"
    # Abrimos el archivo
    with open(alacritty_config_path, "r") as file:
        contenido = yaml.load(file, Loader=yaml.FullLoader)
    # Sustituimos la opacidad
    contenido["window"]["opacity"] = opacity
    with open(alacritty_config_path, "w") as file:
        yaml.dump(contenido, file)  


def change_size(size: float):
    '''Cambia el tamano de letra de alacritty'''
    # Ruta de alacritty
    alacritty_config_path = "/home/" + getuser() + "/.config/alacritty/alacritty.yml"
    # Abrimos el archivo
    with open(alacritty_config_path, "r") as file:
        contenido = yaml.load(file, Loader=yaml.FullLoader)
    # Sustituimos el tamano de letra
    contenido["font"]["size"] = size
    with open(alacritty_config_path, "w") as file:
        yaml.dump(contenido, file)  


def change_font(font: str):
    '''Cambia la fuente empleada en alacritty'''
    # Ruta de alacritty
    alacritty_path = "/home/" + getuser() + "/.config/alacritty/"
    # Fonts path 
    fonts_path = path.join(alacritty_path, "fonts.json")
    # Cogemos las fuentes
    with open(fonts_path, "r") as file:
        fonts = json.load(file)
    if font not in fonts:
        espacio = " "
        raise FontDoesNotExist("The font introduced is not in font's file \n"
                               + f"The available fonts are: {espacio.join(list(fonts.keys()))}")
    # Ruta del archivo de config de alacritty
    alacritty_config_path = path.join(alacritty_path, "alacritty.yml")
    with open(alacritty_config_path, "r") as file:
        contenido = yaml.load(file, Loader=yaml.FullLoader)
    # Cambiamos la fuente por la introducida
    contenido["font"]["bold"]["family"] = fonts[font][0]
    contenido["font"]["italic"]["family"] = fonts[font][1]
    contenido["font"]["normal"]["family"] = fonts[font][2]
    with open(alacritty_config_path, "w") as file:
        yaml.dump(contenido, file)  


def pylook(theme: str, font: str, opacity: float, size: float):
    if theme:
        change_theme(theme)
    if font:
        change_font(font)
    if opacity:
        change_opacity(opacity)
    if size:
        change_size(size)

def cli() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog = "pycolor",
        description = "Command for changing system and alacritty theme",
    )
    parser.add_argument("-t", "--theme", help="Theme for the system and alacritty")
    parser.add_argument("-f", "--font", help="Font for alacritty")
    parser.add_argument("-s", "--size", help="Size of font of alacritty", type=float)
    parser.add_argument("-o", "--opacity", help="Opacity of alacritty", type=float)

    return parser.parse_args()

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


if __name__ == "__main__":
    main()
