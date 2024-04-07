vim.g.mapleader = " "
vim.g.maplocalleader = " "
vim.keymap.set("n", "<leader>pv", vim.cmd.Ex)

-- Copy paste
vim.keymap.set("n", "<leader>y", '"+y')
vim.keymap.set("v", "<leader>y", '"+y')
vim.keymap.set("n", "<leader>Y", '"+Y')

-- Vertical moves
vim.keymap.set("n", "<C-d>", "<C-d>zz")
vim.keymap.set("n", "<C-u>", "<C-u>zz")

-- Search moves
vim.keymap.set("n", "n", "nzzzv")
vim.keymap.set("n", "N", "Nzzzv")

-- Indenting
vim.keymap.set("v", "<", "<gv") -- Shift Indentation to Left
vim.keymap.set("v", ">", ">gv") -- Shift Indentation to Right

-- Comments
vim.api.nvim_set_keymap("n", "<leader>c", "gtc", { noremap = false })
vim.api.nvim_set_keymap("v", "<leader>c", "goc", { noremap = false })

-- Split window
vim.keymap.set("n", "<leader>sv", "<C-w>v", { desc = "Split window vertically" }) -- split window vertically
vim.keymap.set("n", "<leader>sh", "<C-w>s", { desc = "Split window horizontally" }) -- split window horizontally
