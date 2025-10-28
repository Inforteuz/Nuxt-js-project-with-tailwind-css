// nuxt.config.ts
export default defineNuxtConfig({
  compatibilityDate: '2025-07-15',
  devtools: { enabled: false },

  modules: [
    '@nuxtjs/tailwindcss'
  ],

  typescript: {
    shim: false, 
  },

  vite: {
    resolve: {
      alias: {},
    },
    optimizeDeps: {
      exclude: ['tsconfig-paths'],
    },
  },
})
