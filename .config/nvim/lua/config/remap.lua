vim.g.mapleader = " "
vim.g.maplocalleader = " "
vim.keymap.set("n", "<leader>pv", vim.cmd.Ex)

vim.keymap.set("n", "<leader>y", "\"+y")
vim.keymap.set("v", "<leader>y", "\"+y")
vim.keymap.set("n", "<leader>Y", "\"+Y")

-- Fugitive
vim.keymap.set("n", "<leader>gs", vim.cmd.Git);

-- UndoTree
vim.keymap.set("n", "<leader>u", vim.cmd.UndotreeToggle)

-- Indenting
vim.keymap.set("v", "<", "<gv") -- Shift Indentation to Left
vim.keymap.set("v", ">", ">gv") -- Shift Indentation to Right

-- Comments
vim.api.nvim_set_keymap("n", "<C-k>", "gtc", { noremap = false })
vim.api.nvim_set_keymap("v", "<C-k>", "goc", { noremap = false })
