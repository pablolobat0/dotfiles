set fish_greeting ""

# Alias
alias grep "grep --color=auto"
alias cat "bat --style=plain --paging=never"
alias ls "eza --group-directories-first"
alias tree "eza -T"
alias grep "rg"
alias pylook="python3 ~/.local/bin/pylook.py"

function custom_ctrl_f
    # Inserta aquí el comando para ejecutar tu script
    # Por ejemplo, ejecutar un script llamado "mi_script.sh":
    bash ~/.local/bin/tmux-sessionizer.sh
end

bind \cF custom_ctrl_f


# Prompt
starship init fish | source
