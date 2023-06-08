set fish_greeting ""

# Alias
alias grep "grep --color=auto"
alias cat "bat --style=plain --paging=never"
alias ls "exa --group-directories-first"
alias tree "exa -T"
alias grep "rg"
alias dotfiles "git --git-dir $HOME/.dotfiles/ --work-tree $HOME"
alias salir="bash ~/.config/shutDownMenu.sh"
alias pycolor="python3 ~/.local/bin/pycolor.py"
# Prompt
starship init fish | source
