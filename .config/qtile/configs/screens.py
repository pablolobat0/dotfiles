from .widgets import init_widgets_list
from libqtile.config import Screen
from libqtile import bar


def init_widgets_screen1():
    widgets_screen1 = init_widgets_list()
    del widgets_screen1[7]  # remove battery
    return widgets_screen1


def init_widgets_screen2():
    widgets_screen2 = init_widgets_list()
    del widgets_screen2[13:15]  # remove systray
    del widgets_screen2[6]  # remove updates
    return widgets_screen2


def init_screens():
    return [
        Screen(
            top=bar.Bar(
                widgets=init_widgets_screen1(),
                opacity=0.9,
                size=26,
            )
        ),
        Screen(
            top=bar.Bar(
                widgets=init_widgets_screen2(),
                opacity=0.9,
                size=26,
            )
        ),
    ]


# 2 monitors
screens = init_screens()
widgets_list = init_widgets_list()
widgets_screen1 = init_widgets_screen1()
widgets_screen2 = init_widgets_screen2()
