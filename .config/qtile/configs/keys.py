from libqtile.lazy import lazy
from libqtile.config import Key


mod = "mod4"
terminal = "alacritty"
browser = "brave"
fileExplorer = "nemo"

keys = [
    # WINDOWS

    # Switch between windows
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),

    Key([mod, "shift"], "j", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up()),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod, "shift"], "Tab", lazy.prev_layout()),
    # Close window
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    # Reload Qtile
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    # Shutdown Qtile
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),

    # PROGRAMAS

    # Terminal
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Menu
    Key([mod], "m", lazy.spawn("rofi -show drun")),
    # Window Nav
    Key([mod, "shift"], "m", lazy.spawn("rofi -show")),
    # File Explorer
    Key([mod], "e", lazy.spawn(fileExplorer)),
    # Browser
    Key([mod], "b", lazy.spawn(browser)),
    # Vscode
    Key([mod], "v", lazy.spawn("code")),
    # Discord
    Key([mod], "d", lazy.spawn("discord")),
    # Screenshot
    Key([mod], "s", lazy.spawn("shotgun -s")),
    # Redshift
    Key([mod], "r", lazy.spawn("redshift -O 2400")),
    Key([mod, "shift"], "r", lazy.spawn("redshift -x")),
    # Shutdown menu
    Key([mod], "q", lazy.spawn("shutDownMenu.sh")),
    # Networks menu
    Key([mod], "n", lazy.spawn("networkMenu.sh")),

    # VOLUME AND BRIGHTNESS

    # Volume
    Key([], "XF86AudioLowerVolume", lazy.spawn(
        "pactl set-sink-volume @DEFAULT_SINK@ -5%"
    )),
    Key([], "XF86AudioRaiseVolume", lazy.spawn(
        "pactl set-sink-volume @DEFAULT_SINK@ +5%")),
    Key([], "XF86AudioMute", lazy.spawn(
        "pactl set-sink-mute @DEFAULT_SINK@ toggle")),
    # Brightness
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +5%")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 5%-")),
]