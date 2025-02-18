return {
	"stevearc/conform.nvim",
	event = { "BufReadPre", "BufNewFile" },
	config = function()
		local conform = require("conform")

		conform.setup({
			formatters = {
				clang_format = {
					prepend_args = { "--style=file", "--fallback-style=LLVM" },
				},
				shfmt = {
					prepend_args = { "-i", "4" },
				},
				my_rustfmt = {
					command = "cargo fmt",
				},
			},
			formatters_by_ft = {
				lua = { "stylua" },
				python = { "black" },
				c = { "clang-format" },
				rust = { "my_rustfmt" },
			},
			format_on_save = {
				lsp_fallback = true,
				async = false,
				timeout_ms = 500,
			},
			vim.keymap.set({ "n", "v" }, "<leader>ff", function()
				conform.format({
					lsp_fallback = true,
					async = false,
					timeout_ms = 500,
				})
			end, { desc = "Format file or range (in visual mode)" }),
		})
	end,
}
