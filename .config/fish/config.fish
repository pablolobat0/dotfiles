set fish_greeting ""

# Alias
alias grep "grep --color=auto"
alias cat "bat --style=plain --paging=never"
alias ls "exa --group-directories-first"
alias tree "exa -T"
alias grep "rg"
alias pylook="python3 ~/.local/bin/pylook.py"
# Prompt
starship init fish | source
