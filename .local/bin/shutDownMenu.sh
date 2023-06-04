#!/bin/bash

opcion=$(printf "  Apagar\n  Reiniciar\n⏾  Suspender\n󰗼  Cerrar Sesión" | rofi -dmenu)

case "$opcion" in
    "  Apagar") shutdown now ;; # nf-fa-power_off
    "  Reiniciar") reboot ;; # nf-cod-debug_restart
    "⏾  Suspender") systemctl suspend ;; # nf-iec-sleep_mode
    "󰗼  Cerrar Sesión") qtile cmd-obj -o cmd -f shutdown ;; # nf-md-exit_to_app
    *) exit 1 ;;
esac
