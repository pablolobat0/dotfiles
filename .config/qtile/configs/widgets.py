from libqtile import widget
from .theme import colors


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
        padding=pad,
    )


extension_defaults = widget_defaults.copy()


def init_widgets_list():
    widget_list = [
        widget.TextBox(
            text="  ",  # nf-linux-archlinux
            foregorund=["#338b85", "#338b85"],
            background=colors["bar"]["bar"],
            fontsize=22,
        ),
        separator(colors["color1"]["color1"], colors["bar"]["bar"], "left"),
        widget.GroupBox(
            foreground=colors["text"]["text"],
            background=colors["color1"]["color1"],
            fontsize=18,
            margin_y=3,
            margin_x=0,
            padding_y=8,
            padding_x=6,
            borderwidth=1,
            active=colors["active"]["active"],
            inactive=colors["inactive"]["inactive"],
            rounded=True,
            highlight_method="block",
            urgent_alert_method="block",
            urgent_border=colors["urgent"]["urgent"],
            this_current_screen_border=colors["this_screen"]["this_screen"],
            this_screen_border=colors["this_screen"]["this_screen"],
            other_current_screen_border=colors["other_screen"]["other_screen"],
            other_screen_border=colors["other_screen"]["other_screen"],
            disable_drag=True,
        ),
        separator(colors["color1"]["color1"], colors["bar"]["bar"], "right"),
        widget.WindowName(
            background=colors["bar"]["bar"],
            foreground=colors["color2"]["color2"],
            format="{state}{name}",
        ),
        separator(colors["color3"]["color3"], colors["bar"]["bar"], "left"),
        widget.CheckUpdates(
            background=colors["color3"]["color3"],
            foreground=colors["text"]["text"],
            colour_have_updates=colors["text"]["text"],
            colour_no_updates=colors["inactive"]["inactive"],
            fontsize=16,
            no_update_string=" 󰉍 0",
            display_format=" 󰉍 {updates}",  # nf-md-folder_download
            update_interval=1800,
            custom_command="checkupdates",
            # mouse_callbacks = {'Button1': lambda: lazy.spawn("-e sudo pacman -Syu")},
        ),
        widget.Battery(
            background=colors["color3"]["color3"],
            foreground=colors["text"]["text"],
            charge_char="󰂄",  # nf-md-battery_charging
            discharge_char="󱟞",  # nf-md-battery_arrow_down
            full_char="󰁹",  # nf-md-battery
            format="{char} {percent:2.0%}",
            notify_below=0.98,
        ),
        separator(colors["color2"]["color2"], colors["color3"]["color3"], "left"),
        widget.CurrentLayoutIcon(
            scale=0.65,
            background=colors["color2"]["color2"],
            foreground=colors["text"]["text"],
        ),
        widget.CurrentLayout(
            background=colors["color2"]["color2"],
            foreground=colors["text"]["text"],
        ),
        separator(colors["color1"]["color1"], colors["color2"]["color2"], "left"),
        widget.Clock(
            background=colors["color1"]["color1"],
            foreground=colors["text"]["text"],
            format="󰸗 %d/%m/%Y 󰥔 %H:%M",  # nf-md-calendar_month, nf-md-clock
        ),
        separator(colors["bar"]["bar"], colors["color1"]["color1"], "left"),
        widget.Systray(
            background=colors["bar"]["bar"],
        ),
    ]
    return widget_list
