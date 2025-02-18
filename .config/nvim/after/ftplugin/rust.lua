local bufnr = vim.api.nvim_get_current_buf()

vim.keymap.set("n", "K", function()
	vim.cmd.RustLsp({ "hover", "actions" })
end, { silent = true, buffer = bufnr })

vim.keymap.set("n", "<space>rdd", function()
	vim.cmd.RustLsp("debuggables")
end)
vim.keymap.set("n", "<space>rdl", function()
	vim.cmd.RustLsp({ "debuggables", bang = true })
end)
vim.keymap.set("n", "<space>rr", function()
	vim.cmd.RustLsp("runnables")
end)
vim.keymap.set("n", "<space>rl", function()
	vim.cmd.RustLsp({ "runnables", bang = true })
end)
vim.keymap.set("n", "<space>rtt", function()
	vim.cmd.RustLsp("testables")
end)
vim.keymap.set("n", "<space>rtl", function()
	vim.cmd.RustLsp({ "testables", bang = true })
end)
