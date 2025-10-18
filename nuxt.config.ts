import tsconfigPaths from 'vite-tsconfig-paths'

export default defineNuxtConfig({
  compatibilityDate: '2025-07-15',
  devtools: { enabled: true },

  // 1. BU QATORNI OLIB TASHLANG YOKI KOMMENTGA OLING
  // css: ['./assets/css/tailwind.css'], 

  // 2. BU BLOKNI TO'LIQ O'CHIRIB TASHLANG
  // postcss: {
  //   plugins: {
  //     tailwindcss: {},
  //     autoprefixer: {},
  //   },
  // },

  // 3. MODULNI SHU YERGA QO'SHING
  modules: [
    '@nuxtjs/tailwindcss'
  ],

  vite: {
    plugins: [tsconfigPaths()],
  },
})