from .widgets import init_widgets_list
from libqtile.config import Screen
from libqtile import bar


def init_widgets_screen1():
    widgets_screen1 = init_widgets_list()
    return widgets_screen1


def init_widgets_screen2():
    widgets_screen2 = init_widgets_list()
    del widgets_screen2[11:12]  # remove systray
    del widgets_screen2[5:7]  # remove updates
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
