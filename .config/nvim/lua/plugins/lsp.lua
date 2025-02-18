return {
	"neovim/nvim-lspconfig",
	dependencies = {
		"williamboman/mason.nvim",
		"williamboman/mason-lspconfig.nvim",
		"hrsh7th/cmp-nvim-lsp",
		{ "antosha417/nvim-lsp-file-operations", config = true },
		{ "folke/lazydev.nvim", opts = {} },
	},
	config = function()
		local lspconfig = require("lspconfig")
		local mason_lspconfig = require("mason-lspconfig")
		local cmp_lsp = require("cmp_nvim_lsp")

		local capabilities = cmp_lsp.default_capabilities()

		local diagnostic_signs = { Error = " ", Warn = " ", Hint = " ", Info = "" }
		for type, icon in pairs(diagnostic_signs) do
			local hl = "DiagnosticSign" .. type
			vim.fn.sign_define(hl, { text = icon, texthl = hl, numhl = "" })
		end

		mason_lspconfig.setup_handlers({
			["clangd"] = function()
				lspconfig["clangd"].setup({
					capabilities = capabilities,
					filetypes = { "c, cuda" },
				})
			end,
			["pyright"] = function()
				lspconfig["pyright"].setup({
					capabilities = capabilities,
					filetypes = { "python" },
				})
			end,
			["lua_ls"] = function()
				lspconfig.lua_ls.setup({
					capabilities = capabilities,
					settings = {
						Lua = {
							runtime = { version = "Lua 5.1" },
							diagnostics = {
								globals = { "vim", "it", "describe", "before_each", "after_each" },
							},
						},
					},
				})
			end,
		})
	end,
}
