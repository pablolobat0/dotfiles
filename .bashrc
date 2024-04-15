#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return
# Alias
alias grep='rg'
alias cat='bat --style=plain --paging=never'
alias ls='exa --group-directories-first'
alias tree='exa -T'
eval "$(starship init bash)"
alias pylook="python3 ~/.local/bin/pylook.py"
