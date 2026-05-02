<template>
  <div>
    <!-- Page Loader -->
    <ClientOnly>
      <UiAppLoader v-if="loading" />
    </ClientOnly>

    <!-- Scroll Progress Indicator -->
    <div class="scroll-indicator" :style="{ width: scrollProgress + '%' }"></div>

    <!-- Gov.uz Banner -->
    <div class="gov-banner py-2 px-4 text-white text-center">
      <div class="max-w-7xl mx-auto flex flex-col sm:flex-row items-center justify-between gap-3">
        <div class="flex items-center justify-center gap-3 sm:gap-4 text-xs sm:text-sm flex-wrap">
          <a href="https://gov.uz" target="_blank" rel="noopener" class="flex items-center gap-1.5 hover:text-secondary-400">
            <svg class="w-3.5 h-3.5" fill="currentColor" viewBox="0 0 20 20"><path d="M10 2L3 7v11h14V7l-7-5zm0 2.236L15 8v8H5V8l5-3.764z"/></svg>
            Gov.uz
          </a>
          <span class="text-slate-500">|</span>
          <a href="https://my.gov.uz" target="_blank" rel="noopener" class="hover:text-secondary-400">Davlat xizmatlari</a>
          <a href="https://lex.uz" target="_blank" rel="noopener" class="hidden sm:inline hover:text-secondary-400">Qonunchilik</a>
        </div>
        <div class="flex items-center gap-4 text-xs">
          <!-- Accessibility (BVI) -->
          <div class="relative">
            <button @click="bviOpen = !bviOpen" class="flex items-center gap-1.5 hover:text-secondary-400 transition-colors" aria-label="Maxsus imkoniyatlar">
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"/><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"/></svg>
              <span class="hidden md:inline">Maxsus imkoniyatlar</span>
            </button>
            
            <!-- BVI Menu -->
            <div v-if="bviOpen" class="absolute left-1/2 -translate-x-1/2 sm:translate-x-0 sm:left-auto sm:right-0 top-full mt-3 w-64 bg-white rounded-xl shadow-2xl border border-slate-100 p-4 z-50 text-slate-800 text-left">
              <div class="flex justify-between items-center mb-4">
                <h4 class="font-bold text-sm">Maxsus imkoniyatlar</h4>
                <button @click="bviOpen = false" class="text-slate-400 hover:text-slate-600"><svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/></svg></button>
              </div>
              
              <div class="space-y-4">
                <div>
                  <p class="text-xs text-slate-500 mb-2">Ko'rinish</p>
                  <div class="grid grid-cols-2 gap-2">
                    <button @click="toggleGrayscale" class="px-3 py-2 border border-slate-200 rounded-lg text-xs font-medium hover:bg-slate-50 transition-colors" :class="{'bg-primary-50 border-primary-200 text-primary-700': bviSettings.grayscale}">Oq-qora</button>
                    <button @click="toggleContrast" class="px-3 py-2 border border-slate-200 rounded-lg text-xs font-medium hover:bg-slate-50 transition-colors" :class="{'bg-primary-50 border-primary-200 text-primary-700': bviSettings.contrast === 'high'}">Kontrast</button>
                  </div>
                </div>
                <div>
                  <p class="text-xs text-slate-500 mb-2">Shrift o'lchami</p>
                  <div class="grid grid-cols-3 gap-2">
                    <button @click="setFontSize('normal')" class="px-3 py-2 border border-slate-200 rounded-lg text-xs font-medium hover:bg-slate-50 transition-colors" :class="{'bg-primary-50 border-primary-200 text-primary-700': bviSettings.fontSize === 'normal'}">A</button>
                    <button @click="setFontSize('large')" class="px-3 py-2 border border-slate-200 rounded-lg text-base font-medium hover:bg-slate-50 transition-colors" :class="{'bg-primary-50 border-primary-200 text-primary-700': bviSettings.fontSize === 'large'}">A</button>
                    <button @click="setFontSize('xlarge')" class="px-3 py-2 border border-slate-200 rounded-lg text-lg font-medium hover:bg-slate-50 transition-colors" :class="{'bg-primary-50 border-primary-200 text-primary-700': bviSettings.fontSize === 'xlarge'}">A</button>
                  </div>
                </div>
              </div>
            </div>
          </div>
          
          <span class="text-white/20">|</span>
          
          <!-- Language Dropdown -->
          <div class="relative">
            <button @click="langOpen = !langOpen" class="flex items-center gap-1.5 hover:text-secondary-400 transition-colors uppercase font-medium">
              <template v-if="currentLang === 'uz_lot'">O'zbek (Lot)</template>
              <template v-else-if="currentLang === 'uz_kr'">O'zbek (Kril)</template>
              <template v-else>Русский</template>
              <svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/></svg>
            </button>
            
            <div v-if="langOpen" class="absolute left-1/2 -translate-x-1/2 sm:translate-x-0 sm:left-auto sm:right-0 top-full mt-2 w-44 bg-white rounded-xl shadow-2xl border border-slate-100 py-1 z-50 text-slate-700">
              <button @click="changeLanguage('uz_lot')" class="w-full text-left px-4 py-2.5 text-sm hover:bg-slate-50 hover:text-primary-600 transition-colors font-medium">O'zbek (Lot)</button>
              <button @click="changeLanguage('uz_kr')" class="w-full text-left px-4 py-2.5 text-sm hover:bg-slate-50 hover:text-primary-600 transition-colors font-medium border-t border-slate-50">O'zbek (Kril)</button>
              <button @click="changeLanguage('ru')" class="w-full text-left px-4 py-2.5 text-sm hover:bg-slate-50 hover:text-primary-600 transition-colors font-medium border-t border-slate-50">Русский</button>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- ============= HEADER / NAVBAR ============= -->
    <header class="sticky top-0 z-30 transition-all duration-300 border-b border-slate-100" :class="isScrolled ? 'navbar-scrolled' : 'bg-white'">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="flex items-center justify-between h-16 lg:h-20">
          <!-- Logo -->
          <NuxtLink to="/" class="flex items-center gap-3 group">
            <div class="w-10 h-10 lg:w-12 lg:h-12 rounded-xl bg-gradient-to-br from-primary-500 to-primary-700 flex items-center justify-center shadow-md group-hover:shadow-lg transition-shadow">
              <svg class="w-6 h-6 lg:w-7 lg:h-7 text-white" fill="currentColor" viewBox="0 0 24 24"><path d="M9 2h6v7h7v6h-7v7H9v-7H2V9h7V2z"/></svg>
            </div>
            <div class="hidden sm:block">
              <p class="font-heading font-bold text-sm lg:text-base text-dark leading-tight">Andijon viloyati</p>
              <p class="text-xs lg:text-sm text-primary-500 font-medium leading-tight">Sog'liqni saqlash boshqarmasi</p>
            </div>
          </NuxtLink>

          <!-- Desktop Navigation -->
          <nav class="hidden lg:flex items-center gap-1">
            <NuxtLink v-for="item in navItems" :key="item.to" :to="item.to"
              class="px-3 py-2 rounded-lg text-sm font-medium text-slate-600 hover:text-primary-600 hover:bg-primary-50 transition-colors">
              {{ item.label }}
            </NuxtLink>
          </nav>

          <!-- Right Actions -->
          <div class="flex items-center gap-3">
            <button @click="searchOpen = !searchOpen" class="w-10 h-10 rounded-lg hover:bg-slate-100 flex items-center justify-center transition-colors" aria-label="Qidirish">
              <svg class="w-5 h-5 text-slate-600" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"/></svg>
            </button>
            <NuxtLink to="/contact" class="hidden lg:inline-flex btn-primary text-sm">Bog'lanish</NuxtLink>
            <!-- Mobile hamburger -->
            <button @click="mobileOpen = !mobileOpen" class="lg:hidden w-10 h-10 rounded-lg hover:bg-slate-100 flex items-center justify-center" aria-label="Menyu">
              <svg v-if="!mobileOpen" class="w-6 h-6 text-slate-700" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"/></svg>
              <svg v-else class="w-6 h-6 text-slate-700" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/></svg>
            </button>
          </div>
        </div>
      </div>

      <!-- Search bar -->
      <div v-if="searchOpen" class="border-t border-slate-100 bg-white px-4 py-3">
        <div class="max-w-2xl mx-auto relative">
          <input type="text" placeholder="Sayt bo'ylab qidirish..." class="w-full pl-10 pr-4 py-2.5 rounded-lg border border-slate-200 focus:border-primary-500 focus:ring-2 focus:ring-primary-500/20 outline-none text-sm" />
          <svg class="w-5 h-5 text-slate-400 absolute left-3 top-1/2 -translate-y-1/2" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"/></svg>
        </div>
      </div>

      <!-- Mobile menu overlay -->
      <div v-if="mobileOpen" class="fixed inset-0 bg-black/50 z-40" @click="mobileOpen = false"></div>
      <div class="fixed top-0 right-0 h-full w-80 bg-white z-50 shadow-2xl transform transition-transform duration-300" :class="mobileOpen ? 'translate-x-0' : 'translate-x-full'">
        <div class="p-6">
          <div class="flex justify-between items-center mb-8">
            <p class="font-heading font-bold text-dark">Andijon SSB</p>
            <button @click="mobileOpen = false" class="w-8 h-8 rounded-lg hover:bg-slate-100 flex items-center justify-center">
              <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/></svg>
            </button>
          </div>
          <nav class="space-y-1">
            <NuxtLink v-for="item in navItems" :key="item.to" :to="item.to" @click="mobileOpen = false"
              class="block px-4 py-3 rounded-lg text-slate-700 hover:bg-primary-50 hover:text-primary-600 transition-colors font-medium">
              {{ item.label }}
            </NuxtLink>
          </nav>
        </div>
      </div>
    </header>

    <!-- ============= MAIN CONTENT ============= -->
    <main>
      <NuxtPage />
    </main>

    <!-- ============= FOOTER ============= -->
    <footer class="footer-gradient text-white">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12 lg:py-16">
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8 lg:gap-12">
          <!-- About -->
          <div>
            <div class="flex items-center gap-3 mb-5">
              <div class="w-11 h-11 rounded-xl bg-gradient-to-br from-primary-500 to-secondary-500 flex items-center justify-center">
                <svg class="w-6 h-6 text-white" fill="currentColor" viewBox="0 0 24 24"><path d="M9 2h6v7h7v6h-7v7H9v-7H2V9h7V2z"/></svg>
              </div>
              <div>
                <p class="font-heading font-bold text-sm">Andijon viloyati</p>
                <p class="text-xs text-slate-400">Sog'liqni saqlash boshqarmasi</p>
              </div>
            </div>
            <p class="text-sm text-slate-400 leading-relaxed mb-5">O'zbekiston Respublikasi sog'liqni saqlash vazirligi — Andijon viloyati hokimligi sog'liqni saqlash boshqarmasi rasmiy veb-sayti.</p>
            <div class="flex items-center gap-3">
              <a href="#" class="w-9 h-9 rounded-lg bg-white/5 hover:bg-primary-500 flex items-center justify-center transition-all duration-300 hover:-translate-y-0.5" aria-label="Telegram">
                <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 24 24"><path d="M11.944 0A12 12 0 0 0 0 12a12 12 0 0 0 12 12 12 12 0 0 0 12-12A12 12 0 0 0 12 0a12 12 0 0 0-.056 0zm4.962 7.224c.1-.002.321.023.465.14a.506.506 0 0 1 .171.325c.016.093.036.306.02.472-.18 1.898-.962 6.502-1.36 8.627-.168.9-.499 1.201-.82 1.23-.696.065-1.225-.46-1.9-.902-1.056-.693-1.653-1.124-2.678-1.8-1.185-.78-.417-1.21.258-1.91.177-.184 3.247-2.977 3.307-3.23.007-.032.014-.15-.056-.212s-.174-.041-.249-.024c-.106.024-1.793 1.14-5.061 3.345-.48.33-.913.49-1.302.48-.428-.008-1.252-.241-1.865-.44-.752-.245-1.349-.374-1.297-.789.027-.216.325-.437.893-.663 3.498-1.524 5.83-2.529 6.998-3.014 3.332-1.386 4.025-1.627 4.476-1.635z"/></svg>
              </a>
              <a href="#" class="w-9 h-9 rounded-lg bg-white/5 hover:bg-blue-600 flex items-center justify-center transition-all duration-300 hover:-translate-y-0.5" aria-label="Facebook">
                <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 24 24"><path d="M24 12.073c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.99 4.388 10.954 10.125 11.854v-8.385H7.078v-3.47h3.047V9.43c0-3.007 1.792-4.669 4.533-4.669 1.312 0 2.686.235 2.686.235v2.953H15.83c-1.491 0-1.956.925-1.956 1.874v2.25h3.328l-.532 3.47h-2.796v8.385C19.612 23.027 24 18.062 24 12.073z"/></svg>
              </a>
              <a href="#" class="w-9 h-9 rounded-lg bg-white/5 hover:bg-pink-600 flex items-center justify-center transition-all duration-300 hover:-translate-y-0.5" aria-label="Instagram">
                <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 24 24"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zM12 0C8.741 0 8.333.014 7.053.072 2.695.272.273 2.69.073 7.052.014 8.333 0 8.741 0 12c0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98C8.333 23.986 8.741 24 12 24c3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98C15.668.014 15.259 0 12 0zm0 5.838a6.162 6.162 0 100 12.324 6.162 6.162 0 000-12.324zM12 16a4 4 0 110-8 4 4 0 010 8zm6.406-11.845a1.44 1.44 0 100 2.881 1.44 1.44 0 000-2.881z"/></svg>
              </a>
            </div>
          </div>

          <!-- Quick Links -->
          <div>
            <h3 class="font-heading font-semibold text-white mb-5">Tezkor havolalar</h3>
            <ul class="space-y-3">
              <li v-for="link in footerLinks" :key="link.to">
                <NuxtLink :to="link.to" class="text-sm text-slate-400 hover:text-secondary-400 transition-colors flex items-center gap-2">
                  <svg class="w-3 h-3 text-secondary-500" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M7.293 14.707a1 1 0 010-1.414L10.586 10 7.293 6.707a1 1 0 011.414-1.414l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414 0z" clip-rule="evenodd"/></svg>
                  {{ link.label }}
                </NuxtLink>
              </li>
            </ul>
          </div>

          <!-- Gov Links -->
          <div>
            <h3 class="font-heading font-semibold text-white mb-5">Davlat saytlari</h3>
            <ul class="space-y-3">
              <li v-for="link in govLinks" :key="link.url">
                <a :href="link.url" target="_blank" rel="noopener" class="text-sm text-slate-400 hover:text-secondary-400 transition-colors flex items-center gap-2">
                  <svg class="w-3 h-3 text-accent-500" fill="currentColor" viewBox="0 0 20 20"><path d="M11 3a1 1 0 100 2h2.586l-6.293 6.293a1 1 0 101.414 1.414L15 6.414V9a1 1 0 102 0V4a1 1 0 00-1-1h-5z"/><path d="M5 5a2 2 0 00-2 2v8a2 2 0 002 2h8a2 2 0 002-2v-3a1 1 0 10-2 0v3H5V7h3a1 1 0 000-2H5z"/></svg>
                  {{ link.label }}
                </a>
              </li>
            </ul>
          </div>

          <!-- Contact -->
          <div>
            <h3 class="font-heading font-semibold text-white mb-5">Aloqa</h3>
            <div class="space-y-4">
              <div class="flex items-start gap-3">
                <div class="w-8 h-8 rounded-lg bg-primary-500/20 flex items-center justify-center flex-shrink-0 mt-0.5">
                  <svg class="w-4 h-4 text-primary-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"/><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"/></svg>
                </div>
                <p class="text-sm text-slate-400">710000, Andijon shahar, Amir Umarxon ko'chasi, 19-uy</p>
              </div>
              <div class="flex items-center gap-3">
                <div class="w-8 h-8 rounded-lg bg-secondary-500/20 flex items-center justify-center flex-shrink-0">
                  <svg class="w-4 h-4 text-secondary-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"/></svg>
                </div>
                <a href="tel:+998374228-42-84" class="text-sm text-slate-400 hover:text-white transition-colors">(374) 228-42-84</a>
              </div>
              <div class="flex items-center gap-3">
                <div class="w-8 h-8 rounded-lg bg-accent-500/20 flex items-center justify-center flex-shrink-0">
                  <svg class="w-4 h-4 text-accent-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"/></svg>
                </div>
                <a href="mailto:andijon.vssb@ssv.uz" class="text-sm text-slate-400 hover:text-white transition-colors">andijon.vssb@ssv.uz</a>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Bottom Bar -->
      <div class="border-t border-white/10">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-5">
          <div class="flex flex-col sm:flex-row items-center justify-between gap-3">
            <p class="text-xs text-slate-500">© {{ currentYear }} Andijon viloyati sog'liqni saqlash boshqarmasi. Barcha huquqlar himoyalangan.</p>
            <div class="flex items-center gap-1 text-xs text-slate-600">
              <span>Ishlab chiquvchi:</span>
              <a href="https://inforte.uz" target="_blank" rel="noopener" class="text-secondary-500 hover:text-secondary-400 font-medium transition-colors">INFORTE</a>
            </div>
          </div>
        </div>
      </div>
    </footer>

    <!-- Back to Top -->
    <button v-show="showBackToTop" @click="scrollToTop"
      class="fixed bottom-6 right-6 z-40 w-12 h-12 rounded-full bg-primary-500 text-white shadow-lg hover:bg-primary-600 transition-all duration-300 hover:-translate-y-1 flex items-center justify-center"
      aria-label="Yuqoriga qaytish">
      <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 15l7-7 7 7"/></svg>
    </button>
  </div>
</template>

<script setup>
const loading = ref(true)
const scrollProgress = ref(0)
const showBackToTop = ref(false)
const isScrolled = ref(false)
const searchOpen = ref(false)
const mobileOpen = ref(false)

const { currentLang, setLanguage, t } = useLanguage()

function changeLanguage(lang) {
  setLanguage(lang)
  langOpen.value = false
  // Sahifani qayta yuklash shart emas, lekin reactive t() funksiyasi ishlaydi
}

// BVI Settings (Accessibility)
const bviOpen = ref(false)
const bviSettings = ref({
  contrast: 'normal',
  fontSize: 'normal',
  grayscale: false
})

function toggleContrast() {
  bviSettings.value.contrast = bviSettings.value.contrast === 'normal' ? 'high' : 'normal'
  applyBvi()
}

function setFontSize(size) {
  bviSettings.value.fontSize = size
  applyBvi()
}

function toggleGrayscale() {
  bviSettings.value.grayscale = !bviSettings.value.grayscale
  applyBvi()
}

function applyBvi() {
  if (typeof document === 'undefined') return
  const html = document.documentElement
  html.classList.remove('bvi-high-contrast', 'bvi-font-large', 'bvi-font-xlarge', 'bvi-grayscale')
  if (bviSettings.value.contrast === 'high') html.classList.add('bvi-high-contrast')
  if (bviSettings.value.fontSize === 'large') html.classList.add('bvi-font-large')
  if (bviSettings.value.fontSize === 'xlarge') html.classList.add('bvi-font-xlarge')
  if (bviSettings.value.grayscale) html.classList.add('bvi-grayscale')
}

const currentYear = new Date().getFullYear()

const navItems = [
  { to: '/', label: 'Bosh sahifa' },
  { to: '/about', label: 'Boshqarma haqida' },
  { to: '/leadership', label: 'Rahbariyat' },
  { to: '/structure', label: 'Tashkiliy tuzilma' },
  { to: '/news', label: 'Yangiliklar' },
  { to: '/contact', label: "Bog'lanish" },
]

const footerLinks = [
  { to: '/about', label: 'Boshqarma haqida' },
  { to: '/leadership', label: 'Rahbariyat' },
  { to: '/structure', label: 'Tashkiliy tuzilma' },
  { to: '/documents', label: 'Hujjatlar' },
  { to: '/news', label: 'Yangiliklar' },
  { to: '/contact', label: "Bog'lanish" },
]

const govLinks = [
  { url: 'https://gov.uz', label: "O'zbekiston hukumat portali" },
  { url: 'https://ssv.uz', label: "Sog'liqni saqlash vazirligi" },
  { url: 'https://my.gov.uz', label: 'Davlat xizmatlari' },
  { url: 'https://lex.uz', label: "Qonunchilik ma'lumotlari" },
]

onMounted(() => {
  setTimeout(() => { loading.value = false }, 2200)
  window.addEventListener('scroll', handleScroll)
  nextTick(() => {
    setTimeout(() => {
      document.documentElement.classList.add('js-ready')
      initScrollAnimations()
    }, 300)
  })
})

onUnmounted(() => { window.removeEventListener('scroll', handleScroll) })

function handleScroll() {
  const winScroll = document.documentElement.scrollTop
  const height = document.documentElement.scrollHeight - document.documentElement.clientHeight
  scrollProgress.value = height > 0 ? (winScroll / height) * 100 : 0
  showBackToTop.value = winScroll > 400
  isScrolled.value = winScroll > 20
}

function scrollToTop() { window.scrollTo({ top: 0, behavior: 'smooth' }) }

function initScrollAnimations() {
  const observer = new IntersectionObserver(
    (entries) => { entries.forEach((entry) => { if (entry.isIntersecting) entry.target.classList.add('visible') }) },
    { threshold: 0.1, rootMargin: '0px 0px -50px 0px' }
  )
  document.querySelectorAll('.scroll-animate, .scroll-animate-left, .scroll-animate-right, .scroll-animate-scale').forEach((el) => observer.observe(el))
}
</script>
