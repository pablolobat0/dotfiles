# Dotfiles

This repository contains my dotfiles, which include my development setup and work environment configuration for Arch Linux.

## Tools

- **Window Manager:** Qtile
- **Text Editor:** Neovim
- **Terminal Emulator:** Alacritty
- **Terminal Multiplexer:** tmux
- **Shell:** fish

## Dependencies

- **fzf:** A command-line fuzzy finder.
- **bat:** A modern alternative to `cat`.
- **eza:** A modern replacement for `ls`.
- **ripgrep:** A fast and modern alternative to `grep`.
- **stow:** A symbolic link manager for organizing configuration files.
- **Nerd Font:** A font set that includes icons and glyphs for enhanced terminal experience.

## Configuration Details

### **Qtile**

The Qtile configuration is located in `.config/qtile`. It includes:

- Custom keybindings.
- Multiple workspace layouts.
- Styling and theme adjustments.

### **Neovim**

The Neovim configuration is located in `.config/nvim`. It includes:

- Plugin management.
- Custom keybindings.
- Language-specific settings for an optimized coding experience.

### **Alacritty**

The Alacritty configuration is stored in `.config/alacritty`. It contains:

- Custom appearance settings.
- Behavior adjustments for a personalized terminal experience.

### **tmux**

The tmux configuration is located in `.config/tmux/.tmux.conf`. It features:

- Custom keybindings for productivity.
- Visual and functional tweaks.
- Integration with plugins for enhanced terminal multiplexing.

## Usage

To use these dotfiles, clone this repository into a directory under your `$HOME`, ensure all dependencies are installed, and use **stow** to create symbolic links.

```bash
git clone https://github.com/your_username/dotfiles.git
cd dotfiles
stow .
```

