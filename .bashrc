#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias grep='rg'
alias cat='bat --style=plain --paging=never'
alias ls='exa --group-directories-first'
alias tree='exa -T'
eval "$(starship init bash)"
alias dotfiles="git --git-dir $HOME/.dotfiles/ --work-tree $HOME"
alias salir="bash ~/.config/shutDownMenu.sh"
