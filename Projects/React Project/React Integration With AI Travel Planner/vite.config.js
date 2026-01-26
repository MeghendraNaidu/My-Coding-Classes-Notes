import path from "path"
import tailwindcss from "@tailwindcss/vite"
import react from "@vitejs/plugin-react"
import { defineConfig } from "vite"

import { fileURLToPath } from "url" // this extra i have added

const __filename = fileURLToPath(import.meta.url) // this extra i have added
const __dirname = path.dirname(__filename) // this extra i have added


// https://vite.dev/config/
export default defineConfig({
  plugins: [react(), tailwindcss()],
  resolve: {
    alias: {
      "@": path.resolve(__dirname, "./src"),
    },
  },
})