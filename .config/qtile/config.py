# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# Pablo Lobato
# Github: https://github.com/pablolobat0

# Qtile base

from libqtile import hook
from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy

# Qtile extras
# from qtile_extras.widget.decorations import RectDecoration
# from qtile_extras.widget.decorations import PowerLineDecoration
# from qtile_extras.bar import Bar
# from qtile_extras import widget


# Autostart
from os import path
import json
import subprocess


@hook.subscribe.startup_once
def autostart():
    subprocess.call(
        [path.join(path.expanduser('~'), '.config', 'qtile', 'autostart.sh')])


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

# Groups icons: nf-cod-globe, nf-md-microsoft_visual_studio_code, nf-dev-terminal, nf-fa-stack_overflow, nf-fa-folder, nf-fa-youtube_play

groups = [Group(i) for i in ["󰖟 ", "󰨞 ", " ", " ", " ", " "]]

for i, group in enumerate(groups):
    actual_key = str(i + 1)
    keys.extend([
        # Switch to workspace N
        Key([mod], actual_key, lazy.group[group.name].toscreen()),
        # Send window to workspace N
        Key([mod, "shift"], actual_key, lazy.window.togroup(group.name))
    ])

layout_conf = {
    "border_focus": "#d5ffff",
    "border_normal": "#338b85",
    "border_width": 2,
    "margin": 10,
}

layouts = [
    # layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=4),
    layout.Max(),
    layout.MonadTall(**layout_conf),
    layout.MonadWide(**layout_conf),
    layout.RatioTile(**layout_conf),
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

# Get the path of the current Qtile config file
config_dir = path.dirname(path.abspath(__file__))

# Construct the path to the JSON file within the folder
json_file_path = path.join(config_dir, "themes", "nord.json")

with open(json_file_path, "r") as file:
    colors = json.load(file)

widget_defaults = dict(
    font="UbuntuMono Nerd Font",
    fontsize=15,
    padding=3,
)


def separator(foreground, background, direction, size=30, pad=-0.55):
    if direction == "left":
        sep = " "  # nf-ple-left_half_circle_thick
    elif direction == "right":
        sep = " "  # nf-ple-right_half_circle_thick

    return widget.TextBox(
        text=sep,
        foreground=foreground,
        background=background,
        fontsize=size,
        padding=pad
    )


extension_defaults = widget_defaults.copy()


def init_widgets_list():
    widget_list = [
        widget.TextBox(
            text="  ",  # nf-linux-archlinux
            foregorund=["#338b85", "#338b85"],
            background=colors["bar"],
            fontsize=22,
        ),
        separator(colors["color1"], colors["bar"], "left"),
        widget.GroupBox(
            foreground=colors["text"],
            background=colors["color1"],
            fontsize=16,
            margin_y=3,
            margin_x=0,
            padding_y=8,
            padding_x=6,
            borderwidth=1,
            active=colors["active"],
            inactive=colors["inactive"],
            rounded=True,
            highlight_method='block',
            urgent_alert_method='block',
            urgent_border=colors["urgent"],
            this_current_screen_border=colors["this_screen"],
            this_screen_border=colors["this_screen"],
            other_current_screen_border=colors["other_screen"],
            other_screen_border=colors["other_screen"],
            disable_drag=True,
        ),
        separator(colors["color1"], colors["bar"], "right"),
        widget.WindowName(
            background=colors["bar"],
            foreground=colors["color2"],
            format='{state}{name}',
        ),
        # widget.Memory(
        # background=["#9ce0db", "#9ce0db"],
        # foreground =["#3e4144", "#3e4144"],
        #  format = '󰍛{MemUsed: .2f}{mm}', # nf-md-memory
        #   measure_mem = "G",
        #    update_interval=5,

        # ),
        # widget.CPU(
        # background=["#9ce0db", "#9ce0db"],
        # foreground =["#3e4144", "#3e4144"],
        #  format=' {load_percent}%', # nf-fa-microchip
        #   update_interval=5,
        # ),
        # widget.Battery(
        #     background=["#9ce0db", "#9ce0db"],
        #     foreground =["#3e4144", "#3e4144"],
        #     charge_char = " 󰂄", # nf-md-battery_charging
        #     discharge_char = " 󱟞", # nf-md-battery_arrow_down
        #     full_char = " 󰁹", # nf-md-battery
        #     format = '{char} {percent:2.0%} ',
        #     notify_below = 0.98,
        # ),
        separator(colors["color3"], colors["bar"], "left"),
        widget.CheckUpdates(
            background=colors["color3"],
            foreground=colors["text"],
            colour_have_updates=colors["text"],
            colour_no_updates=colors["inactive"],
            fontsize=16,
            no_update_string=' 󰉍 0',
            display_format=' 󰉍 {updates}',  # nf-md-folder_download
            update_interval=1800,
            custom_command='checkupdates',
            # mouse_callbacks = {'Button1': lambda: lazy.spawn("-e sudo pacman -Syu")},
        ),
        separator(colors["color2"], colors["color3"], "left"),
        widget.CurrentLayoutIcon(
            scale=0.65,
            background=colors["color2"],
        ),
        widget.CurrentLayout(
            background=colors["color2"],
            foreground=colors["text"],
        ),
        separator(colors["color1"], colors["color2"], "left"),
        widget.Clock(
            background=colors["color1"],
            foreground=colors["text"],
            format="󰸗 %d/%m/%Y 󰥔 %H:%M",  # nf-md-calendar_month, nf-md-clock
        ),
        separator(colors["bar"], colors["color1"], "left"),
        widget.Systray(
            background=colors["bar"],
        ),
    ]
    return widget_list


def init_widgets_screen1():
    widgets_screen1 = init_widgets_list()
    return widgets_screen1


def init_widgets_screen2():
    widgets_screen2 = init_widgets_list()
    del widgets_screen2[11:13]  # remove systray
    del widgets_screen2[5:8]  # remove updates
    return widgets_screen2


def init_screens():
    return [Screen(top=bar.Bar(
        widgets=init_widgets_screen1(),
        opacity=0.9,
        size=26,
        # margin= [5, 5, 5, 5],
    )),
        Screen(top=bar.Bar(widgets=init_widgets_screen2(), opacity=0.9, size=24, background=["#3e4144", "#3e4144"]))]


# 2 monitors
screens = init_screens()
widgets_list = init_widgets_list()
widgets_screen1 = init_widgets_screen1()
widgets_screen2 = init_widgets_screen2()


# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ], border_focus="#5dc1b9"
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
