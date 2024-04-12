# Neovim Configuration

## Dependencies

### Ripgrep

```bash
sudo pacman -Syu ripgrep
```

### Node

```bash
sudo pacman -Syu node
```

## Plugins

### Plugin Manager

- [folke/lazy.nvim](https://github.com/folke/lazy.nvim)

### Dependency for Other Plugins

- [nvim-lua/plenary.nvim](https://github.com/nvim-lua/plenary.nvim)
- [folke/neodev.nvim](https://github.com/folke/neodev.nvim)
- [folke/neoconf.nvim](https://github.com/folke/neoconf.nvim)

### Navigation

- [nvim-telescope/telescope.nvim](https://github.com/nvim-telescope/telescope.nvim): Fuzzy finder
- [ThePrimeagen/harpoon](https://github.com/ThePrimeagen/harpoon/tree/harpoon2): Mark and navigate between files
- [christoomey/vim-tmux-navigator](https://github.com/christoomey/vim-tmux-navigator): Navigation between Neovim and Tmux

### LSP

- [williamboman/mason.nvim](https://github.com/williamboman/mason.nvim): Install LSPs, formatters and linters
- [williamboman/mason-lspconfig.nvim](https://github.com/williamboman/mason-lspconfig.nvim): Bridge between mason and lspconfig
- [WhoIsSethDaniel/mason-tool-installer.nvim](https://github.com/WhoIsSethDaniel/mason-tool-installer.nvim): Ensure that some linters and formatter are installed
- [neovim/nvim-lspconfig](https://github.com/neovim/nvim-lspconfig): Easy way to configure lsp servers
- [onsails/lspkind.nvim](https://github.com/onsails/lspkind.nvim)

### Autocompletion

- [hrsh7th/nvim-cmp](https://github.com/hrsh7th/nvim-cmp): Completion plugin
- [hrsh7th/cmp-nvim-lsp](https://github.com/hrsh7th/cmp-nvim-lsp): Smart code autocompletion with lsp
- [hrsh7th/cmp-buffer](https://github.com/hrsh7th/cmp-buffer)
- [hrsh7th/cmp-path](https://github.com/hrsh7th/cmp-path)
- [saadparwaiz1/cmp_luasnip](https://github.com/saadparwaiz1/cmp_luasnip): Luasnip Completion

### Snippets

- [L3MON4D3/LuaSnip](https://github.com/L3MON4D3/LuaSnip)
- [rafamadriz/friendly-snippets](https://github.com/rafamadriz/friendly-snippets)

### Diagnostics

- [folke/trouble.nvim](https://github.com/folke/trouble.nvim): Diagnostics UI and navigation

### Formatting & Linting

- [stevearc/conform.nvim](https://github.com/stevearc/conform.nvim): Easy way to configure formatters
- [mfussenegger/nvim-lint](https://github.com/mfussenegger/nvim-lint): Easy way to configure linters
- [numToStr/Comment.nvim](https://github.com/numToStr/Comment.nvim): Comment and uncomment

### Treesitter Syntax Highlighting, Autoclosing

- [nvim-treesitter/nvim-treesitter](https://github.com/nvim-treesitter/nvim-treesitter)
- [windwp/nvim-ts-autotag](https://github.com/windwp/nvim-ts-autotag)

### Git

- [tpope/vim-fugitive](https://github.com/tpope/vim-fugitive): Git integration

### Undo

- [mbbill/undotree](https://github.com/mbbill/undotree): Undo history visualizer

### Style

- [rebelot/kanagawa.nvim](https://github.com/rebelot/kanagawa.nvim): Colorscheme
- [RRethy/vim-illuminate](https://github.com/RRethy/vim-illuminate): Highlighting other uses of the word under the cursor
- [xiyaowong/transparent.nvim](https://github.com/xiyaowong/transparent.nvim): Transparency
- [kyazdani42/nvim-web-devicons](https://github.com/nvim-tree/nvim-web-devicons): Icons
- [nvim-lualine](https://github.com/nvim-lualine/lualine.nvim): Better statusline

