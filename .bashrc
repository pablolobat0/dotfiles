#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias grep='rg'
alias cat='bat --style=plain --paging=never'
alias ls='exa --group-directories-first'
alias tree='exa -T'
PS1='[\u@\h \W]\$ '
eval "$(starship init bash)"
alias dotfiles="git --git-dir $HOME/.dotfiles/ --work-tree $HOME"
export CLASSPATH=/home/pablo/Documentos/Uni/BD_II/ParqueAtraccionesNoso/ProyectoBasesDatos/lib:.
