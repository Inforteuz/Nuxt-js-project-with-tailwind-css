<template>
  <div class="min-h-screen bg-gradient-to-br from-emerald-50 via-teal-50 to-cyan-50">
    <!-- Header -->
    <header class="container mx-auto px-6 py-8">
      <div class="flex items-center justify-between">
        <div class="flex items-center space-x-3">
          <div class="w-12 h-12 bg-gradient-to-br from-emerald-500 to-teal-600 rounded-xl flex items-center justify-center shadow-lg">
            <span class="text-white font-bold text-2xl">🚀</span>
          </div>
          <div>
            <h2 class="text-xl font-bold text-gray-800">Nuxt Starter</h2>
            <p class="text-xs text-gray-500">Ready for Development</p>
          </div>
        </div>
        <div class="px-4 py-2 bg-emerald-100 text-emerald-700 rounded-full text-sm font-semibold">
          v1.0.0
        </div>
      </div>
    </header>

    <!-- Main Content -->
    <main class="container mx-auto px-6 py-12">
      <!-- Hero Section -->
      <div class="text-center mb-16">
        <div class="inline-flex items-center space-x-2 bg-white px-4 py-2 rounded-full shadow-md mb-6">
          <span class="w-2 h-2 bg-green-500 rounded-full animate-pulse"></span>
          <span class="text-sm font-medium text-gray-700">Yangi loyiha uchun tayyor</span>
        </div>
        
        <h1 class="text-5xl md:text-6xl font-extrabold text-gray-900 mb-4">
          Nuxt 3 Project
          <span class="block text-transparent bg-clip-text bg-gradient-to-r from-emerald-600 to-teal-600">
            Tayyor Holatda
          </span>
        </h1>
        
        <p class="text-xl text-gray-600 max-w-2xl mx-auto leading-relaxed">
          Bu loyiha Tailwind CSS bilan sozlangan va yangi Nuxt.js proyektingizni boshlash uchun mukammal starter template hisoblanadi.
        </p>
      </div>

      <!-- Quick Start Instructions -->
      <div class="max-w-4xl mx-auto mb-16">
        <div class="bg-white rounded-2xl shadow-xl p-8 border border-gray-100">
          <div class="flex items-center space-x-3 mb-6">
            <div class="w-10 h-10 bg-blue-100 rounded-lg flex items-center justify-center">
              <span class="text-xl">📋</span>
            </div>
            <h2 class="text-2xl font-bold text-gray-800">Boshlash yo'riqnomasi</h2>
          </div>
          
          <div class="space-y-6">
            <!-- Step 1 -->
            <div class="flex gap-4">
              <div class="flex-shrink-0 w-8 h-8 bg-emerald-500 text-white rounded-full flex items-center justify-center font-bold">
                1
              </div>
              <div class="flex-1">
                <h3 class="font-semibold text-gray-800 mb-2">Repository ni clone qiling</h3>
                <div class="bg-gray-900 rounded-lg p-4 font-mono text-sm text-green-400 overflow-x-auto">
                  git clone https://github.com/Inforteuz/Nuxt-js-project-with-tailwind-css.git
                </div>
              </div>
            </div>

            <!-- Step 2 -->
            <div class="flex gap-4">
              <div class="flex-shrink-0 w-8 h-8 bg-emerald-500 text-white rounded-full flex items-center justify-center font-bold">
                2
              </div>
              <div class="flex-1">
                <h3 class="font-semibold text-gray-800 mb-2">Loyiha papkasiga kiring</h3>
                <div class="bg-gray-900 rounded-lg p-4 font-mono text-sm text-green-400">
                  cd Nuxt-js-project-with-tailwind-css
                </div>
              </div>
            </div>

            <!-- Step 3 -->
            <div class="flex gap-4">
              <div class="flex-shrink-0 w-8 h-8 bg-emerald-500 text-white rounded-full flex items-center justify-center font-bold">
                3
              </div>
              <div class="flex-1">
                <h3 class="font-semibold text-gray-800 mb-2">Dependencies o'rnating</h3>
                <div class="bg-gray-900 rounded-lg p-4 font-mono text-sm text-green-400">
                  npm install
                </div>
              </div>
            </div>

            <!-- Step 4 -->
            <div class="flex gap-4">
              <div class="flex-shrink-0 w-8 h-8 bg-emerald-500 text-white rounded-full flex items-center justify-center font-bold">
                4
              </div>
              <div class="flex-1">
                <h3 class="font-semibold text-gray-800 mb-2">Development serverni ishga tushiring</h3>
                <div class="bg-gray-900 rounded-lg p-4 font-mono text-sm text-green-400">
                  npm run dev
                </div>
              </div>
            </div>
          </div>

          <div class="mt-6 p-4 bg-blue-50 border-l-4 border-blue-500 rounded">
            <p class="text-sm text-blue-800">
              <span class="font-semibold">💡 Maslahat:</span> Server ishga tushgandan so'ng 
              <code class="px-2 py-1 bg-white rounded text-xs">http://localhost:3000</code> 
              manzilida ochiladi.
            </p>
          </div>
        </div>
      </div>

      <!-- Features Grid -->
      <div class="max-w-6xl mx-auto mb-16">
        <h2 class="text-3xl font-bold text-center text-gray-800 mb-10">
          Nima o'rnatilgan?
        </h2>
        <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-6">
          <!-- Feature 1 -->
          <div class="bg-white p-6 rounded-xl shadow-lg hover:shadow-2xl transition border border-gray-100">
            <div class="w-14 h-14 bg-gradient-to-br from-green-400 to-emerald-500 rounded-xl flex items-center justify-center mb-4">
              <span class="text-3xl">⚡</span>
            </div>
            <h3 class="text-lg font-bold text-gray-800 mb-2">Nuxt 3</h3>
            <p class="text-gray-600 text-sm">Eng so'nggi Vue.js framework with server-side rendering va optimizatsiya</p>
          </div>

          <!-- Feature 2 -->
          <div class="bg-white p-6 rounded-xl shadow-lg hover:shadow-2xl transition border border-gray-100">
            <div class="w-14 h-14 bg-gradient-to-br from-cyan-400 to-blue-500 rounded-xl flex items-center justify-center mb-4">
              <span class="text-3xl">🎨</span>
            </div>
            <h3 class="text-lg font-bold text-gray-800 mb-2">Tailwind CSS</h3>
            <p class="text-gray-600 text-sm">Utility-first CSS framework to'liq sozlangan va ishga tayyor</p>
          </div>

          <!-- Feature 3 -->
          <div class="bg-white p-6 rounded-xl shadow-lg hover:shadow-2xl transition border border-gray-100">
            <div class="w-14 h-14 bg-gradient-to-br from-purple-400 to-pink-500 rounded-xl flex items-center justify-center mb-4">
              <span class="text-3xl">📦</span>
            </div>
            <h3 class="text-lg font-bold text-gray-800 mb-2">Auto Import</h3>
            <p class="text-gray-600 text-sm">Components va composables avtomatik import qilinadi</p>
          </div>

          <!-- Feature 4 -->
          <div class="bg-white p-6 rounded-xl shadow-lg hover:shadow-2xl transition border border-gray-100">
            <div class="w-14 h-14 bg-gradient-to-br from-orange-400 to-red-500 rounded-xl flex items-center justify-center mb-4">
              <span class="text-3xl">🔥</span>
            </div>
            <h3 class="text-lg font-bold text-gray-800 mb-2">Hot Reload</h3>
            <p class="text-gray-600 text-sm">O'zgarishlar darhol ko'rinadi, development jarayoni tezlashadi</p>
          </div>

          <!-- Feature 5 -->
          <div class="bg-white p-6 rounded-xl shadow-lg hover:shadow-2xl transition border border-gray-100">
            <div class="w-14 h-14 bg-gradient-to-br from-yellow-400 to-orange-500 rounded-xl flex items-center justify-center mb-4">
              <span class="text-3xl">📱</span>
            </div>
            <h3 class="text-lg font-bold text-gray-800 mb-2">Responsive</h3>
            <p class="text-gray-600 text-sm">Barcha qurilmalarda mukammal ko'rinish uchun optimallashtirilgan</p>
          </div>

          <!-- Feature 6 -->
          <div class="bg-white p-6 rounded-xl shadow-lg hover:shadow-2xl transition border border-gray-100">
            <div class="w-14 h-14 bg-gradient-to-br from-indigo-400 to-purple-500 rounded-xl flex items-center justify-center mb-4">
              <span class="text-3xl">🚀</span>
            </div>
            <h3 class="text-lg font-bold text-gray-800 mb-2">Production Ready</h3>
            <p class="text-gray-600 text-sm">Deploy qilish uchun tayyor, optimallashtirilgan build</p>
          </div>
        </div>
      </div>

      <!-- Next Steps -->
      <div class="max-w-4xl mx-auto">
        <div class="bg-gradient-to-r from-emerald-500 to-teal-600 rounded-2xl shadow-2xl p-8 text-white">
          <h2 class="text-3xl font-bold mb-4">Keyingi qadamlar</h2>
          <ul class="space-y-3">
            <li class="flex items-start gap-3">
              <span class="text-2xl">✅</span>
              <span class="text-lg">
                <code class="bg-white bg-opacity-20 px-2 py-1 rounded text-sm">pages/</code> 
                papkasida yangi sahifalar yarating
              </span>
            </li>
            <li class="flex items-start gap-3">
              <span class="text-2xl">✅</span>
              <span class="text-lg">
                <code class="bg-white bg-opacity-20 px-2 py-1 rounded text-sm">components/</code> 
                papkasida qayta ishlatiladigan komponentlar yozing
              </span>
            </li>
            <li class="flex items-start gap-3">
              <span class="text-2xl">✅</span>
              <span class="text-lg">
                <code class="bg-white bg-opacity-20 px-2 py-1 rounded text-sm">tailwind.config.js</code> 
                da ranglar va stillarni sozlang
              </span>
            </li>
            <li class="flex items-start gap-3">
              <span class="text-2xl">✅</span>
              <span class="text-lg">Documentation: 
                <a href="https://nuxt.com" class="underline hover:text-emerald-200" target="_blank">nuxt.com</a> va 
                <a href="https://tailwindcss.com" class="underline hover:text-emerald-200" target="_blank">tailwindcss.com</a>
              </span>
            </li>
          </ul>
        </div>
      </div>
    </main>

    <!-- Footer -->
    <footer class="container mx-auto px-6 py-12">
      <div class="border-t border-gray-200 pt-8">
        <div class="text-center text-gray-600">
          <p class="mb-2">Muvaffaqiyatli dasturlash tilaklar! 💚</p>
          <p class="text-sm">
            Built with 
            <span class="font-semibold text-emerald-600">Nuxt 3</span> + 
            <span class="font-semibold text-teal-600">Tailwind CSS</span>
          </p>
        </div>
      </div>
    </footer>
  </div>
</template>

<script setup>
useHead({
  title: 'Nuxt 3 Starter - Tayyor Project',
  meta: [
    { name: 'description', content: 'Nuxt 3 va Tailwind CSS bilan tayyor starter template' }
  ]
})
</script>