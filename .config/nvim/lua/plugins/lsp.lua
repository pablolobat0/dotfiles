return {
	"neovim/nvim-lspconfig",
	dependencies = {
		"williamboman/mason.nvim",
		"williamboman/mason-lspconfig.nvim",
		"WhoIsSethDaniel/mason-tool-installer.nvim",
		"hrsh7th/cmp-nvim-lsp",
		{ "antosha417/nvim-lsp-file-operations", config = true },
		{ "folke/lazydev.nvim", opts = {} },
	},
	config = function()
		local lspconfig = require("lspconfig")
		local mason = require("mason")
		local mason_lspconfig = require("mason-lspconfig")
		local mason_tool_installer = require("mason-tool-installer")
		local cmp_lsp = require("cmp_nvim_lsp")

		local capabilities = cmp_lsp.default_capabilities()

		vim.diagnostic.config({
			signs = {
				text = {
					[vim.diagnostic.severity.ERROR] = " ",
					[vim.diagnostic.severity.WARN] = " ",
					[vim.diagnostic.severity.HINT] = " ",
					[vim.diagnostic.severity.INFO] = "",
				},
			},
		})

		-- 1. Setup mason first
		mason.setup({
			ui = {
				icons = {
					package_installed = "✓",
					package_pending = "➜",
					package_uninstalled = "✗",
				},
			},
		})

		-- 2. Setup mason-lspconfig with handlers (new API)
		mason_lspconfig.setup({
			ensure_installed = {
				"lua_ls",
				"pyright",
			},
			handlers = {
				["clangd"] = function()
					lspconfig["clangd"].setup({
						capabilities = capabilities,
						filetypes = { "c", "cuda", "cpp" },
					})
				end,
				["pyright"] = function()
					lspconfig["pyright"].setup({
						capabilities = capabilities,
						filetypes = { "python" },
					})
				end,
				["ts_ls"] = function()
					lspconfig["ts_ls"].setup({
						capabilities = capabilities,
						filetypes = { "js", "ts", "typescriptreact" },
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
			},
		})

		-- 3. Setup rust_analyzer directly (uses system binary from rustup)
		vim.lsp.config("rust_analyzer", {
			capabilities = capabilities,
			settings = {
				["rust-analyzer"] = {
					check = {
						command = "clippy",
						extraArgs = { "--no-deps" },
					},
					checkOnSave = true,
				},
			},
		})

		-- 4. Setup mason-tool-installer for formatters/linters
		mason_tool_installer.setup({
			ensure_installed = {
				"stylua",
				"ruff",
				"flake8",
			},
		})
	end,
}
