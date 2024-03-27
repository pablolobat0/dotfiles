local config = function()
	require("neoconf").setup({})
	local cmp_nvim_lsp = require("cmp_nvim_lsp")
	local lspconfig = require("lspconfig")

	local diagnostic_signs = { Error = " ", Warn = " ", Hint = "ﴞ ", Info = "" }
	for type, icon in pairs(diagnostic_signs) do
		local hl = "DiagnosticSign" .. type
		vim.fn.sign_define(hl, { text = icon, texthl = hl, numhl = "" })
	end

	local on_attach = function(client, bufnr)
		local opts = { noremap = true, silent = true, buffer = bufnr }
		vim.keymap.set("n", "<leader>fd", "Lspsaga finder", opts) -- go to definition
		vim.keymap.set("n", "<leader>gd", "Lspsaga peek_definition", "n", opts) -- peak definition
		vim.keymap.set("n", "<leader>gD", "Lspsaga goto_definition", "n", opts) -- go to definition
		vim.keymap.set("n", "<leader>ca", "Lspsaga code_action", "n", opts) -- see available code actions
		vim.keymap.set("n", "<leader>rn", "Lspsaga rename", "n", opts) -- smart rename
		vim.keymap.set("n", "<leader>D", "Lspsaga show_line_diagnostics", "n", opts) -- show  diagnostics for line
		vim.keymap.set("n", "<leader>d", "Lspsaga show_cursor_diagnostics", "n", opts) -- show diagnostics for cursor
		vim.keymap.set("n", "<leader>pd", "Lspsaga diagnostic_jump_prev", "n", opts) -- jump to prev diagnostic in buffer
		vim.keymap.set("n", "<leader>nd", "Lspsaga diagnostic_jump_next", "n", opts) -- jump to next diagnostic in buffer
		vim.keymap.set("n", "K", "Lspsaga hover_doc", "n", opts) -- show documentation for what is under cursor
	end

	local capabilities = cmp_nvim_lsp.default_capabilities()

	-- lua
	lspconfig.lua_ls.setup({
		capabilities = capabilities,
		on_attach = on_attach,
		settings = { -- custom settings for lua
			Lua = {
				-- make the language server recognize "vim" global
				diagnostics = {
					globals = { "vim" },
				},
				workspace = {
					-- make language server aware of runtime files
					library = {
						[vim.fn.expand("$VIMRUNTIME/lua")] = true,
						[vim.fn.stdpath("config") .. "/lua"] = true,
					},
				},
			},
		},
	})

	-- python
	lspconfig.pyright.setup({
		capabilities = capabilities,
		on_attach = on_attach,
		settings = {
			pyright = {
				disableOrganizeImports = false,
				analysis = {
					useLibraryCodeForTypes = true,
					autoSearchPaths = true,
					diagnosticMode = "workspace",
					autoImportCompletions = true,
				},
			},
		},
	})

	-- typescript
	lspconfig.tsserver.setup({
		on_attach = on_attach,
		capabilities = capabilities,
		filetypes = {
			"typescript",
		},
		root_dir = lspconfig.util.root_pattern("package.json", "tsconfig.json", ".git"),
	})

	-- bash
	lspconfig.bashls.setup({
		capabilities = capabilities,
		on_attach = on_attach,
		filetypes = { "sh" },
	})

	-- html, typescriptreact, javascriptreact, css, sass, scss, less, svelte, vue
	lspconfig.emmet_ls.setup({
		capabilities = capabilities,
		on_attach = on_attach,
		filetypes = {
			"html",
			"javascript",
			"css",
		},
	})

	local luacheck = require("efmls-configs.linters.luacheck")
	local stylua = require("efmls-configs.formatters.stylua")
	local flake8 = require("efmls-configs.linters.flake8")
	local black = require("efmls-configs.formatters.black")
	local eslint_d = require("efmls-configs.linters.eslint_d")
	local prettierd = require("efmls-configs.formatters.prettier_d")
	local shellcheck = require("efmls-configs.linters.shellcheck")
	local shfmt = require("efmls-configs.formatters.shfmt")
	local alex = require("efmls-configs.linters.alex")

	-- configure efm server
	lspconfig.efm.setup({
		filetypes = {
			"lua",
			"python",
			"sh",
			"javascript",
			"typescript",
			"markdown",
		},
		init_options = {
			documentFormatting = true,
			documentRangeFormatting = true,
			hover = true,
			documentSymbol = true,
			codeAction = true,
			completion = true,
		},
		settings = {
			languages = {
				lua = { luacheck, stylua },
				python = { flake8, black },
				typescript = { eslint_d, prettierd },
				sh = { shellcheck, shfmt },
				javascript = { eslint_d, prettierd },
				markdown = { alex, prettierd },
			},
		},
	})
end

return {
	"neovim/nvim-lspconfig",
	config = config,
	lazy = false,
	dependencies = {
		"windwp/nvim-autopairs",
		"williamboman/mason.nvim",
		"creativenull/efmls-configs-nvim",
		"hrsh7th/nvim-cmp",
		"hrsh7th/cmp-buffer",
		"hrsh7th/cmp-nvim-lsp",
	},
}
