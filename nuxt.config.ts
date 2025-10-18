import tsconfigPaths from 'vite-tsconfig-paths'

export default defineNuxtConfig({
  compatibilityDate: '2025-07-15',
  devtools: { enabled: true },

  // 1. REMOVE OR COMMENT THIS LINE
  // css: ['./assets/css/tailwind.css'], 

  // 2. DELETE THIS BLOCK COMPLETELY
  // postcss: {
  //   plugins: {
  //     tailwindcss: {},
  //     autoprefixer: {},
  //   },
  // },

  // 3. ADD MODULE HERE
  modules: [
    '@nuxtjs/tailwindcss'
  ],

  vite: {
    plugins: [tsconfigPaths()],
  },
})
