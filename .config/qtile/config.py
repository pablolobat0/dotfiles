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
from libqtile import bar, layout
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy

# Qtile extras
from qtile_extras.widget.decorations import RectDecoration
from qtile_extras.widget.decorations import PowerLineDecoration
from qtile_extras.bar import Bar
from qtile_extras import widget

# Autostart
from os import path
import subprocess 

@hook.subscribe.startup_once
def autostart():
    subprocess.call([path.join(path.expanduser('~'), '.config', 'qtile', 'autostart.sh')])

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

    #VOLUME AND BRIGHTNESS

    # Volume
    Key([], "XF86AudioLowerVolume", lazy.spawn(
        "pactl set-sink-volume @DEFAULT_SINK@ -5%"
    )),
    Key([], "XF86AudioRaiseVolume", lazy.spawn(
        "pactl set-sink-volume @DEFAULT_SINK@ +5%"
    )),
    Key([], "XF86AudioMute", lazy.spawn(
        "pactl set-sink-mute @DEFAULT_SINK@ toggle"
    )),
     # Brightness
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-")),
]

# Groups icons: nf-cod-globe, nf-md-microsoft_visual_studio_code, nf-dev-terminal, nf-fa-stack_overflow, nf-fa-folder, nf-fa-youtube_play

groups = [Group(i) for i in ["󰖟 ", "󰨞 ", " ", " ", " "," "]]

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
    #layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=4),
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

widget_defaults = dict(
    font="UbuntuMono Nerd Font",
    fontsize=16,
    padding=3,
)

decoration_group = {
    "decorations": [
        RectDecoration(
            filled = True,
            radius = 10,
            use_widget_background = True,
        )
    ],
}

decoration_group_borders_left = {
    "decorations": [
        RectDecoration(
            filled = True,
            radius = [10, 0, 0, 10],
            use_widget_background = True,
        )
    ],
}

decoration_group_borders_right = {
    "decorations": [
        RectDecoration(
            filled = True,
            radius = [0, 10, 10, 0],
            use_widget_background = True,
        )
    ],
}

powerline = {
    "decorations": [
        PowerLineDecoration(
            path = "arrow_right", # arrow_right, rounded_left(right), forward(back)_slash, zig_zag 
            size = 10
        )
    ]
}

extension_defaults = widget_defaults.copy()

def init_widgets_list():
    widget_list = [
                widget.TextBox(
                    text = "   ", # nf-linux-archlinux
                    background=["#338b85","#338b85"],
                    foreground=["#3e4144","#3e4144"],
                    fontsize=22,
                    **decoration_group
                ),
                widget.TextBox(
                    text = "󰇙", # nf-md-dots_vertical
                    background=["#3e4144","#3e4144"],
                    foreground=["#65727c","#65727c"],
                    fontsize=18,
                ),
                widget.Sep(
                    linewidth=0,
                    padding=10,
                    background=["#5dc1b9","#5dc1b9"],
                    **decoration_group_borders_left
                ),
                widget.GroupBox(
                     foreground =["#ffffff", "#ffffff"],
                     background=["#5dc1b9", "#5dc1b9"],
                     font='UbuntuMono Nerd Font',
                     fontsize=16,
                     margin_y=3,
                     margin_x=0,
                     padding_y=8,
                     padding_x=6,
                     borderwidth=1,
                     active=["#3e4144", "#3e4144"],
                     inactive=["#65727c", "#65727c"],
                     rounded=True,
                     highlight_method='block',
                     urgent_alert_method='block',
                     urgent_border=["#b48ead", "#b48ead"],
                     this_current_screen_border=["#9ce0db", "#9ce0db"],
                     this_screen_border=["#9ce0db", "#9ce0db"],
                     other_current_screen_border=["#5dc1b9", "#5dc1b9"],
                     other_screen_border=["#5dc1b9", "#5dc1b9"],
                     disable_drag=True,
                 ),
                widget.Sep(
                    linewidth=0,
                    padding=10,
                    background=["#5dc1b9","#5dc1b9"],
                    **decoration_group_borders_right
                ),
                widget.WindowName(
                     background=["#3e4144", "#3e4144"],
                     foreground = ["#5dc1b9", "#5dc1b9"],
                     font='mononoki Nerd Font',
                     fontsize=12,
                     format = ' {state}{name}',
                ),
                widget.Sep(
                    linewidth=0,
                    padding=10,
                    background=["#d5ffff","#d5ffff"],
                    **decoration_group_borders_left
                ),
                widget.Systray(
                    background=["#d5ffff","#d5ffff"],
                ),
                widget.Sep(
                    linewidth=0,
                    padding=10,
                    background=["#9ce0db","#9ce0db"],
                    **decoration_group_borders_left
                ),
                widget.Sep(
                    linewidth=0,
                    padding=10,
                    background=["#d5ffff","#d5ffff"],
                    **powerline
                ),
                widget.Memory(
                    background=["#9ce0db", "#9ce0db"],
                    foreground =["#3e4144", "#3e4144"],
                    format = '󰍛{MemUsed: .2f}{mm}', # nf-md-memory
                    measure_mem = "G",
                    update_interval=5,

                ),
                widget.CPU(
                    background=["#9ce0db", "#9ce0db"],
                    foreground =["#3e4144", "#3e4144"],
                    format=' {load_percent}%', # nf-fa-microchip
                    update_interval=5,
                ),
                widget.Battery( 
                    background=["#9ce0db", "#9ce0db"],
                    foreground =["#3e4144", "#3e4144"],
                    charge_char = " 󰂄", # nf-md-battery_charging
                    discharge_char = " 󱟞", # nf-md-battery_arrow_down
                    full_char = " 󰁹", # nf-md-battery
                    format = '{char} {percent:2.0%} ',
                    notify_below = 0.98,
                    **powerline,
                ),
                widget.CheckUpdates(
                    background=["#9ce0db", "#9ce0db"],
                    foreground =["#3e4144", "#3e4144"],
                    colour_have_updates=["#3e4144","#3e4144"],
                    colour_no_updates=["#65727c","#65727c"],
                    no_update_string='󰉍 0',
                    display_format='󰉍 {updates} ', # nf-md-folder_download
                    update_interval=1800,
                    custom_command='checkupdates',
                    # mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(terminal + ' -e sudo pacman -Syu')},
                    **powerline,
                ),
                widget.CurrentLayoutIcon(
                     scale=0.7,
                     background=["#5dc1b9","#5dc1b9"],
                     foreground =["#3e4144", "#3e4144"],
                ),
                widget.CurrentLayout( 
                    background=["#5dc1b9","#5dc1b9"],
                    foreground =["#3e4144", "#3e4144"],
                ),
                widget.Sep(
                    linewidth=0,
                    padding=10,
                    background=["#5dc1b9","#5dc1b9"],
                    **decoration_group_borders_right
                ),
                widget.TextBox(
                    text = "󰇙", # nf-md-dots_vertical
                    background=["#3e4144","#3e4144"],
                    foreground=["#65727c","#65727c"],
                    fontsize=18,
                ),
                widget.Clock(
                    background=["#338b85","#338b85"],
                    foreground=["#3e4144","#3e4144"],
                    format=" 󰸗 %d/%m/%Y 󰥔 %H:%M ", # nf-md-calendar_month, nf-md-clock
                    **decoration_group
                    ),
            ]
    return widget_list

def init_widgets_screen1():
    widgets_screen1 = init_widgets_list()
    del widgets_screen1[12] 
    del widgets_screen1[8] # remove battery icon
    return widgets_screen1    

def init_widgets_screen2():
    widgets_screen2 = init_widgets_list()
    del widgets_screen2[13] # remove updates
    del widgets_screen2[9] # remove updates
    del widgets_screen2[6:8] # remove systray
    return widgets_screen2

def init_screens():
    return [Screen(top=bar.Bar(
                widgets=init_widgets_screen1(), 
                opacity=0.9, 
                size=24,  
                background=["#3e4144","#3e4144"],
                # margin= [5, 5, 0, 5],
                )),
            Screen(top=bar.Bar(widgets=init_widgets_screen2(), opacity=0.9, size=24,background=["#3e4144","#3e4144"]))]


# 2 monitors
screens = init_screens()
widgets_list = init_widgets_list()
widgets_screen1 = init_widgets_screen1()
widgets_screen2 = init_widgets_screen2()



# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
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
