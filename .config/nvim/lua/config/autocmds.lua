-- auto-format on save
local lsp_group = vim.api.nvim_create_augroup("LspFormattingGroup", {})

vim.api.nvim_create_autocmd("LspAttach", {
	group = lsp_group,
	callback = function(e)
		local opts = { buffer = e.buf }
		vim.keymap.set("n", "gd", function() -- Go to the definition
			vim.lsp.buf.definition()
		end, opts)
		vim.keymap.set("n", "K", function()
			vim.lsp.buf.hover()
		end, opts)
		vim.keymap.set("n", "<leader>vws", function()
			vim.lsp.buf.workspace_symbol()
		end, opts)
		vim.keymap.set("n", "<leader>vd", function()
			vim.diagnostic.open_float()
		end, opts)
		vim.keymap.set("n", "<leader>vca", function()
			vim.lsp.buf.code_action()
		end, opts)
		vim.keymap.set("n", "<leader>vrr", function()
			vim.lsp.buf.references()
		end, opts)
		vim.keymap.set("n", "<leader>vrn", function()
			vim.lsp.buf.rename()
		end, opts)
		vim.keymap.set("i", "<C-h>", function()
			vim.lsp.buf.signature_help()
		end, opts)
		vim.keymap.set("n", "[d", function()
			vim.diagnostic.goto_next()
		end, opts)
		vim.keymap.set("n", "]d", function()
			vim.diagnostic.goto_prev()
		end, opts)
	end,
})

-- Highlight when yanking (copying) text
vim.api.nvim_create_autocmd("TextYankPost", {
	desc = "Highlight when yanking (copying) text",
	group = vim.api.nvim_create_augroup("kickstart-highlight-yank", { clear = true }),
	callback = function()
		vim.highlight.on_yank()
	end,
})
