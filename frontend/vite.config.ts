import { defineConfig } from 'vite'
import { svelte } from '@sveltejs/vite-plugin-svelte'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [svelte()],
  server:{
    '/data': 'http://localhost:5001',
    changeOrigin: true,
    configure: (proxy, options) => {
      // proxy will be an instance of 'http-proxy'
    }}
})
