// nuxt.config.ts
export default defineNuxtConfig({
  compatibilityDate: '2025-07-15',
  devtools: { enabled: false },

  // app/ papka ichidagi fayllarni to'g'ri topish uchun
  srcDir: 'app/',

  modules: [
    '@nuxtjs/tailwindcss'
  ],

  app: {
    head: {
      title: "Andijon viloyati sog'liqni saqlash boshqarmasi",
      htmlAttrs: { lang: 'uz' },
      meta: [
        { charset: 'utf-8' },
        { name: 'viewport', content: 'width=device-width, initial-scale=1' },
        { name: 'description', content: "O'zbekiston Respublikasi sog'liqni saqlash vazirligi — Andijon viloyati hokimligi sog'liqni saqlash boshqarmasi rasmiy veb-sayti" },
        { name: 'format-detection', content: 'telephone=no' },
        { name: 'theme-color', content: '#0A4D8C' },
        { property: 'og:type', content: 'website' },
        { property: 'og:title', content: "Andijon viloyati sog'liqni saqlash boshqarmasi" },
        { property: 'og:description', content: "Andijon viloyati hokimligi sog'liqni saqlash boshqarmasi rasmiy veb-sayti" },
        { property: 'og:locale', content: 'uz_UZ' },
      ],
      link: [
        { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' },
        { rel: 'preconnect', href: 'https://fonts.googleapis.com' },
        { rel: 'preconnect', href: 'https://fonts.gstatic.com', crossorigin: '' },
        { rel: 'stylesheet', href: 'https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Outfit:wght@400;500;600;700;800&display=swap' },
      ],
    },
    pageTransition: { name: 'page', mode: 'out-in' },
  },

  css: [
    '~/assets/css/tailwind.css',
    '~/assets/css/style.css',
  ],

  typescript: { shim: false },
})
