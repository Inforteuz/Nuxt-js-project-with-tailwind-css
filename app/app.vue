<template>
  <div class="app-root">
    <ClientOnly>
      <UiAppLoader v-if="loading" />
    </ClientOnly>

    <div class="scroll-indicator" :style="{ width: scrollProgress + '%' }"></div>

    <!-- Gov banner -->
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
          <!-- Maxsus imkoniyatlar (BVI) -->
          <div class="relative">
            <button @click="bviOpen = !bviOpen" class="flex items-center gap-1.5 hover:text-secondary-400 transition-colors" :aria-label="bviLabel">
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"/><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"/></svg>
              <span class="hidden md:inline">{{ bviLabel }}</span>
            </button>
            <div v-if="bviOpen" class="absolute left-1/2 -translate-x-1/2 sm:translate-x-0 sm:left-auto sm:right-0 top-full mt-3 w-64 bg-white rounded-xl shadow-2xl border border-slate-100 p-4 z-50 text-slate-800 text-left">
              <div class="flex justify-between items-center mb-4">
                <h4 class="font-bold text-sm">{{ bviLabel }}</h4>
                <button @click="bviOpen = false" class="text-slate-400 hover:text-slate-600"><svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/></svg></button>
              </div>
              <div class="space-y-4">
                <div>
                  <p class="text-xs text-slate-500 mb-2">{{ bviViewLabel }}</p>
                  <div class="grid grid-cols-2 gap-2">
                    <button @click="toggleGrayscale" class="px-3 py-2 border border-slate-200 rounded-lg text-xs font-medium hover:bg-slate-50 transition-colors" :class="{'bg-primary-50 border-primary-200 text-primary-700': bviSettings.grayscale}">{{ bviGrayscaleLabel }}</button>
                    <button @click="toggleContrast" class="px-3 py-2 border border-slate-200 rounded-lg text-xs font-medium hover:bg-slate-50 transition-colors" :class="{'bg-primary-50 border-primary-200 text-primary-700': bviSettings.contrast}">{{ bviContrastLabel }}</button>
                  </div>
                </div>
                <div>
                  <p class="text-xs text-slate-500 mb-2">{{ bviFontLabel }}</p>
                  <div class="grid grid-cols-3 gap-2">
                    <button @click="setFontSize('normal')" class="px-3 py-2 border border-slate-200 rounded-lg text-xs font-medium hover:bg-slate-50 transition-colors" :class="{'bg-primary-50 border-primary-200 text-primary-700': bviSettings.fontSize === 'normal'}">A</button>
                    <button @click="setFontSize('large')" class="px-3 py-2 border border-slate-200 rounded-lg text-base font-medium hover:bg-slate-50 transition-colors" :class="{'bg-primary-50 border-primary-200 text-primary-700': bviSettings.fontSize === 'large'}">A</button>
                    <button @click="setFontSize('xlarge')" class="px-3 py-2 border border-slate-200 rounded-lg text-lg font-medium hover:bg-slate-50 transition-colors" :class="{'bg-primary-50 border-primary-200 text-primary-700': bviSettings.fontSize === 'xlarge'}">A</button>
                  </div>
                </div>
                <button @click="resetBvi" class="w-full text-xs text-slate-500 hover:text-primary-600 py-1">{{ bviResetLabel }}</button>
              </div>
            </div>
          </div>

          <span class="text-white/20">|</span>

          <!-- Language switcher -->
          <div class="relative">
            <button @click="langOpen = !langOpen" class="flex items-center gap-1.5 hover:text-secondary-400 transition-colors uppercase font-medium">
              <template v-if="currentLang === 'uz_lot'">O'zbek</template>
              <template v-else-if="currentLang === 'uz_kr'">Ўзбек</template>
              <template v-else>Рус</template>
              <svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/></svg>
            </button>
            <div v-if="langOpen" class="absolute left-1/2 -translate-x-1/2 sm:translate-x-0 sm:left-auto sm:right-0 top-full mt-2 w-44 bg-white rounded-xl shadow-2xl border border-slate-100 py-1 z-50 text-slate-700">
              <button @click="changeLanguage('uz_lot')" class="w-full text-left px-4 py-2.5 text-sm hover:bg-slate-50 hover:text-primary-600 transition-colors font-medium" :class="currentLang==='uz_lot' ? 'text-primary-600 bg-primary-50' : ''">O'zbek (Lotin)</button>
              <button @click="changeLanguage('uz_kr')" class="w-full text-left px-4 py-2.5 text-sm hover:bg-slate-50 hover:text-primary-600 transition-colors font-medium border-t border-slate-50" :class="currentLang==='uz_kr' ? 'text-primary-600 bg-primary-50' : ''">Ўзбек (Кирил)</button>
              <button @click="changeLanguage('ru')" class="w-full text-left px-4 py-2.5 text-sm hover:bg-slate-50 hover:text-primary-600 transition-colors font-medium border-t border-slate-50" :class="currentLang==='ru' ? 'text-primary-600 bg-primary-50' : ''">Русский</button>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- HEADER -->
    <header class="sticky top-0 z-30 transition-all duration-300 border-b border-slate-100" :class="isScrolled ? 'navbar-scrolled' : 'bg-white'">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="flex items-center justify-between h-16 lg:h-20">
          <NuxtLink to="/" class="flex items-center gap-3 group flex-shrink-0">
            <div class="w-10 h-10 lg:w-12 lg:h-12 rounded-xl bg-gradient-to-br from-primary-500 to-primary-700 flex items-center justify-center shadow-md overflow-hidden flex-shrink-0">
              <img v-if="logoUrl" :src="logoUrl" alt="Logo" class="w-full h-full object-contain" />
              <svg v-else class="w-6 h-6 lg:w-7 lg:h-7 text-white" fill="currentColor" viewBox="0 0 24 24"><path d="M9 2h6v7h7v6h-7v7H9v-7H2V9h7V2z"/></svg>
            </div>
            <div class="hidden sm:block min-w-0">
              <p class="font-heading font-bold text-sm lg:text-base text-dark leading-tight truncate">{{ siteName.split(' ').slice(0, 3).join(' ') }}</p>
              <p class="text-xs lg:text-sm text-primary-500 font-medium leading-tight truncate">{{ siteName.split(' ').slice(3).join(' ') }}</p>
            </div>
          </NuxtLink>

          <nav class="hidden lg:flex items-center gap-1">
            <NuxtLink v-for="item in navItems" :key="item.to" :to="item.to"
              class="px-3 py-2 rounded-lg text-sm font-medium text-slate-600 hover:text-primary-600 hover:bg-primary-50 transition-colors whitespace-nowrap">
              {{ item.label }}
            </NuxtLink>
          </nav>

          <div class="flex items-center gap-2 flex-shrink-0">
            <NuxtLink to="/contact" class="hidden lg:inline-flex btn-primary text-sm">
              {{ currentLang === 'ru' ? 'Контакты' : "Bog'lanish" }}
            </NuxtLink>
            <!-- Hamburger -->
            <button @click="mobileOpen = !mobileOpen" class="lg:hidden w-10 h-10 rounded-lg hover:bg-slate-100 flex items-center justify-center" aria-label="Menyu">
              <svg v-if="!mobileOpen" class="w-6 h-6 text-slate-700" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"/></svg>
              <svg v-else class="w-6 h-6 text-slate-700" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/></svg>
            </button>
          </div>
        </div>
      </div>
    </header>

    <!-- MOBILE MENU — HEADER TASHQARISIDA (muhim!) -->
    <Transition name="overlay-fade">
      <div v-if="mobileOpen" class="fixed inset-0 bg-black/60 z-40" @click="mobileOpen = false"></div>
    </Transition>
    <div
      class="fixed top-0 right-0 h-full w-72 bg-white z-50 shadow-2xl transition-transform duration-300 ease-in-out overflow-y-auto"
      :class="mobileOpen ? 'translate-x-0' : 'translate-x-full'"
    >
      <div class="p-5">
        <div class="flex justify-between items-center mb-6">
          <div class="flex items-center gap-2">
            <div class="w-8 h-8 rounded-lg bg-gradient-to-br from-primary-500 to-primary-700 flex items-center justify-center overflow-hidden flex-shrink-0">
              <img v-if="logoUrl" :src="logoUrl" alt="Logo" class="w-full h-full object-contain" />
              <svg v-else class="w-5 h-5 text-white" fill="currentColor" viewBox="0 0 24 24"><path d="M9 2h6v7h7v6h-7v7H9v-7H2V9h7V2z"/></svg>
            </div>
            <span class="font-bold text-dark text-sm">Andijon SSB</span>
          </div>
          <button @click="mobileOpen = false" class="w-8 h-8 rounded-lg hover:bg-slate-100 flex items-center justify-center">
            <svg class="w-5 h-5 text-slate-600" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/></svg>
          </button>
        </div>

        <nav class="space-y-1 mb-6">
          <NuxtLink v-for="item in navItems" :key="item.to" :to="item.to" @click="mobileOpen = false"
            class="flex items-center gap-3 px-4 py-3 rounded-xl text-slate-700 hover:bg-primary-50 hover:text-primary-600 transition-colors font-medium text-sm">
            {{ item.label }}
          </NuxtLink>
        </nav>

        <NuxtLink to="/contact" @click="mobileOpen = false" class="w-full btn-primary text-sm text-center block mb-4">
          {{ currentLang === 'ru' ? 'Контакты' : "Bog'lanish" }}
        </NuxtLink>

        <!-- Til tanlash (mobil) -->
        <div class="border-t border-slate-100 pt-4">
          <p class="text-xs text-slate-400 mb-2 px-1">{{ currentLang === 'ru' ? 'Язык' : 'Til' }}</p>
          <div class="flex gap-2">
            <button @click="changeLanguage('uz_lot')" class="flex-1 py-2 rounded-lg text-xs font-semibold border-2 transition-colors"
              :class="currentLang==='uz_lot' ? 'bg-primary-500 text-white border-primary-500' : 'border-slate-200 text-slate-600'">O'z</button>
            <button @click="changeLanguage('uz_kr')" class="flex-1 py-2 rounded-lg text-xs font-semibold border-2 transition-colors"
              :class="currentLang==='uz_kr' ? 'bg-primary-500 text-white border-primary-500' : 'border-slate-200 text-slate-600'">Ўз</button>
            <button @click="changeLanguage('ru')" class="flex-1 py-2 rounded-lg text-xs font-semibold border-2 transition-colors"
              :class="currentLang==='ru' ? 'bg-primary-500 text-white border-primary-500' : 'border-slate-200 text-slate-600'">Рус</button>
          </div>
        </div>
      </div>
    </div>

    <main>
      <NuxtPage />
    </main>

    <!-- FOOTER -->
    <footer class="footer-gradient text-white">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12 lg:py-16">
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8 lg:gap-12">
          <div>
            <div class="flex items-center gap-3 mb-5">
              <div class="w-11 h-11 rounded-xl bg-gradient-to-br from-primary-500 to-secondary-500 flex items-center justify-center overflow-hidden flex-shrink-0">
                <img v-if="logoUrl" :src="logoUrl" alt="Logo" class="w-full h-full object-contain" />
                <svg v-else class="w-6 h-6 text-white" fill="currentColor" viewBox="0 0 24 24"><path d="M9 2h6v7h7v6h-7v7H9v-7H2V9h7V2z"/></svg>
              </div>
              <p class="font-heading font-bold text-sm leading-snug">{{ siteName }}</p>
            </div>
            <div class="flex items-center gap-3 mt-4">
              <a v-if="siteInfo?.telegram" :href="siteInfo.telegram" target="_blank" rel="noopener" class="w-9 h-9 rounded-lg bg-white/10 hover:bg-primary-500 flex items-center justify-center transition-all" aria-label="Telegram">
                <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 24 24"><path d="M11.944 0A12 12 0 0 0 0 12a12 12 0 0 0 12 12 12 12 0 0 0 12-12A12 12 0 0 0 12 0a12 12 0 0 0-.056 0zm4.962 7.224c.1-.002.321.023.465.14a.506.506 0 0 1 .171.325c.016.093.036.306.02.472-.18 1.898-.962 6.502-1.36 8.627-.168.9-.499 1.201-.82 1.23-.696.065-1.225-.46-1.9-.902-1.056-.693-1.653-1.124-2.678-1.8-1.185-.78-.417-1.21.258-1.91.177-.184 3.247-2.977 3.307-3.23.007-.032.014-.15-.056-.212s-.174-.041-.249-.024c-.106.024-1.793 1.14-5.061 3.345-.48.33-.913.49-1.302.48-.428-.008-1.252-.241-1.865-.44-.752-.245-1.349-.374-1.297-.789.027-.216.325-.437.893-.663 3.498-1.524 5.83-2.529 6.998-3.014 3.332-1.386 4.025-1.627 4.476-1.635z"/></svg>
              </a>
              <a v-if="siteInfo?.facebook" :href="siteInfo.facebook" target="_blank" rel="noopener" class="w-9 h-9 rounded-lg bg-white/10 hover:bg-blue-600 flex items-center justify-center transition-all" aria-label="Facebook">
                <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 24 24"><path d="M24 12.073c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.99 4.388 10.954 10.125 11.854v-8.385H7.078v-3.47h3.047V9.43c0-3.007 1.792-4.669 4.533-4.669 1.312 0 2.686.235 2.686.235v2.953H15.83c-1.491 0-1.956.925-1.956 1.874v2.25h3.328l-.532 3.47h-2.796v8.385C19.612 23.027 24 18.062 24 12.073z"/></svg>
              </a>
              <a v-if="siteInfo?.instagram" :href="siteInfo.instagram" target="_blank" rel="noopener" class="w-9 h-9 rounded-lg bg-white/10 hover:bg-pink-600 flex items-center justify-center transition-all" aria-label="Instagram">
                <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 24 24"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zM12 0C8.741 0 8.333.014 7.053.072 2.695.272.273 2.69.073 7.052.014 8.333 0 8.741 0 12c0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98C8.333 23.986 8.741 24 12 24c3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98C15.668.014 15.259 0 12 0zm0 5.838a6.162 6.162 0 100 12.324 6.162 6.162 0 000-12.324zM12 16a4 4 0 110-8 4 4 0 010 8zm6.406-11.845a1.44 1.44 0 100 2.881 1.44 1.44 0 000-2.881z"/></svg>
              </a>
            </div>
          </div>

          <div>
            <h3 class="font-heading font-semibold text-white mb-5">{{ currentLang === 'ru' ? 'Быстрые ссылки' : 'Tezkor havolalar' }}</h3>
            <ul class="space-y-3">
              <li v-for="link in quickLinks" :key="link.to">
                <NuxtLink :to="link.to" class="text-sm text-slate-400 hover:text-secondary-400 transition-colors flex items-center gap-2">
                  <svg class="w-3 h-3 text-secondary-500 flex-shrink-0" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M7.293 14.707a1 1 0 010-1.414L10.586 10 7.293 6.707a1 1 0 011.414-1.414l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414 0z" clip-rule="evenodd"/></svg>
                  {{ link.label }}
                </NuxtLink>
              </li>
            </ul>
          </div>

          <div>
            <h3 class="font-heading font-semibold text-white mb-5">{{ currentLang === 'ru' ? 'Госпорталы' : 'Davlat saytlari' }}</h3>
            <ul class="space-y-3">
              <li v-for="link in govLinks" :key="link.url">
                <a :href="link.url" target="_blank" rel="noopener" class="text-sm text-slate-400 hover:text-secondary-400 transition-colors flex items-center gap-2">
                  <svg class="w-3 h-3 text-accent-500 flex-shrink-0" fill="currentColor" viewBox="0 0 20 20"><path d="M11 3a1 1 0 100 2h2.586l-6.293 6.293a1 1 0 101.414 1.414L15 6.414V9a1 1 0 102 0V4a1 1 0 00-1-1h-5z"/><path d="M5 5a2 2 0 00-2 2v8a2 2 0 002 2h8a2 2 0 002-2v-3a1 1 0 10-2 0v3H5V7h3a1 1 0 000-2H5z"/></svg>
                  {{ link.label }}
                </a>
              </li>
            </ul>
          </div>

          <div>
            <h3 class="font-heading font-semibold text-white mb-5">{{ currentLang === 'ru' ? 'Контакты' : 'Aloqa' }}</h3>
            <div class="space-y-4">
              <div class="flex items-start gap-3">
                <div class="w-8 h-8 rounded-lg bg-primary-500/20 flex items-center justify-center flex-shrink-0 mt-0.5">
                  <svg class="w-4 h-4 text-primary-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"/><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"/></svg>
                </div>
                <p class="text-sm text-slate-400">{{ siteAddress }}</p>
              </div>
              <div v-if="sitePhone" class="flex items-center gap-3">
                <div class="w-8 h-8 rounded-lg bg-secondary-500/20 flex items-center justify-center flex-shrink-0">
                  <svg class="w-4 h-4 text-secondary-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"/></svg>
                </div>
                <a :href="`tel:${sitePhone}`" class="text-sm text-slate-400 hover:text-white transition-colors">{{ sitePhone }}</a>
              </div>
              <div v-if="siteEmail" class="flex items-center gap-3">
                <div class="w-8 h-8 rounded-lg bg-accent-500/20 flex items-center justify-center flex-shrink-0">
                  <svg class="w-4 h-4 text-accent-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"/></svg>
                </div>
                <a :href="`mailto:${siteEmail}`" class="text-sm text-slate-400 hover:text-white transition-colors">{{ siteEmail }}</a>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="border-t border-white/10">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-5 flex flex-col sm:flex-row items-center justify-between gap-3">
          <p class="text-xs text-slate-500">© {{ currentYear }} {{ siteName }}. {{ currentLang === 'ru' ? 'Все права защищены.' : 'Barcha huquqlar himoyalangan.' }}</p>
          <div class="flex items-center gap-1 text-xs text-slate-600">
            <span>{{ currentLang === 'ru' ? 'Разработчик:' : currentLang === 'uz_kr' ? 'Ишлаб чиқувчи:' : 'Ishlab chiquvchi:' }}</span>
            <a href="https://andijon-digitalcity.uz" target="_blank" rel="noopener" class="text-secondary-500 hover:text-secondary-400 font-medium transition-colors">Andijon Digital City</a>
          </div>
        </div>
      </div>
    </footer>

    <!-- Back to top (shifted left to not overlap AI chat) -->
    <button v-show="showBackToTop" @click="scrollToTop"
      class="fixed bottom-6 right-24 z-40 w-12 h-12 rounded-full bg-primary-500 text-white shadow-lg hover:bg-primary-600 transition-all duration-300 hover:-translate-y-1 flex items-center justify-center"
      aria-label="Yuqoriga qaytish">
      <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 15l7-7 7 7"/></svg>
    </button>

    <!-- AI Chat Widget -->
    <ClientOnly>
      <UiAiChat />
    </ClientOnly>
  </div>
</template>

<script setup>
const config = useRuntimeConfig()
const { currentLang, setLanguage, t } = useLanguage()

const loading = ref(true)
const scrollProgress = ref(0)
const showBackToTop = ref(false)
const isScrolled = ref(false)
const mobileOpen = ref(false)
const langOpen = ref(false)
const bviOpen = ref(false)
const bviSettings = reactive({ grayscale: false, contrast: false, fontSize: 'normal' })

const bviLabel = computed(() => currentLang.value === 'ru' ? 'Спец. возможности' : currentLang.value === 'uz_kr' ? 'Махсус имкониятлар' : 'Maxsus imkoniyatlar')
const bviViewLabel = computed(() => currentLang.value === 'ru' ? 'Вид' : currentLang.value === 'uz_kr' ? "Кўриниш" : "Ko'rinish")
const bviGrayscaleLabel = computed(() => currentLang.value === 'ru' ? 'Ч/Б' : currentLang.value === 'uz_kr' ? 'Оқ-қора' : 'Oq-qora')
const bviContrastLabel = computed(() => currentLang.value === 'ru' ? 'Контраст' : currentLang.value === 'uz_kr' ? 'Контраст' : 'Kontrast')
const bviFontLabel = computed(() => currentLang.value === 'ru' ? 'Размер шрифта' : currentLang.value === 'uz_kr' ? "Шрифт ўлчами" : "Shrift o'lchami")
const bviResetLabel = computed(() => currentLang.value === 'ru' ? 'Сбросить' : currentLang.value === 'uz_kr' ? 'Қайта тиклаш' : 'Qayta tiklash')

function applyBvi() {
  if (typeof document === 'undefined') return
  const html = document.documentElement
  html.classList.toggle('bvi-grayscale', bviSettings.grayscale)
  html.classList.toggle('bvi-contrast', bviSettings.contrast)
  html.classList.remove('bvi-font-large', 'bvi-font-xlarge')
  if (bviSettings.fontSize === 'large') html.classList.add('bvi-font-large')
  if (bviSettings.fontSize === 'xlarge') html.classList.add('bvi-font-xlarge')
  try { localStorage.setItem('bvi', JSON.stringify(bviSettings)) } catch (e) {}
}
function toggleGrayscale() { bviSettings.grayscale = !bviSettings.grayscale; applyBvi() }
function toggleContrast() { bviSettings.contrast = !bviSettings.contrast; applyBvi() }
function setFontSize(size) { bviSettings.fontSize = size; applyBvi() }
function resetBvi() { bviSettings.grayscale = false; bviSettings.contrast = false; bviSettings.fontSize = 'normal'; applyBvi(); bviOpen.value = false }

const [{ data: apiNav }, { data: apiFooter }, { data: siteInfo }, { data: siteSettings }] = await Promise.all([
  useFetch(`${config.public.apiBase}/nav/`),
  useFetch(`${config.public.apiBase}/footer-links/`),
  useFetch(`${config.public.apiBase}/info/`),
  useFetch(`${config.public.apiBase}/site-settings/`),
])

const logoUrl = computed(() => siteSettings.value?.logo || null)
const siteName = computed(() => t(siteInfo.value, 'name') || "Andijon viloyati SSB")
const siteAddress = computed(() => t(siteInfo.value, 'address') || "Andijon shahar")
const sitePhone = computed(() => siteInfo.value?.phone || '')
const siteEmail = computed(() => siteInfo.value?.email || '')

function changeLanguage(lang) {
  setLanguage(lang)
  langOpen.value = false
}

// Body scroll bloklanadi mobil menyu ochilganda
watch(mobileOpen, (val) => {
  if (typeof document !== 'undefined') {
    document.body.style.overflow = val ? 'hidden' : ''
  }
})

const navFallback = computed(() => {
  if (currentLang.value === 'ru') return [
    { to: '/', label: 'Главная' },
    { to: '/about', label: 'Об управлении' },
    { to: '/leadership', label: 'Руководство' },
    { to: '/structure', label: 'Структура' },
    { to: '/news', label: 'Новости' },
    { to: '/contact', label: 'Контакты' },
  ]
  if (currentLang.value === 'uz_kr') return [
    { to: '/', label: 'Бош саҳифа' },
    { to: '/about', label: 'Бошқарма ҳақида' },
    { to: '/leadership', label: 'Раҳбарият' },
    { to: '/structure', label: 'Тузилма' },
    { to: '/news', label: 'Янгиликлар' },
    { to: '/contact', label: 'Боғланиш' },
  ]
  return [
    { to: '/', label: 'Bosh sahifa' },
    { to: '/about', label: 'Boshqarma haqida' },
    { to: '/leadership', label: 'Rahbariyat' },
    { to: '/structure', label: 'Tashkiliy tuzilma' },
    { to: '/news', label: 'Yangiliklar' },
    { to: '/contact', label: "Bog'lanish" },
  ]
})

const navItems = computed(() => {
  if (apiNav.value?.length > 0) {
    return apiNav.value.map(item => ({ to: item.url, label: t(item, 'label') }))
  }
  return navFallback.value
})

const quickLinks = computed(() => {
  if (apiFooter.value?.length > 0) {
    const quick = apiFooter.value.filter(l => l.column === 'quick')
    if (quick.length > 0) return quick.map(l => ({ to: l.url, label: t(l, 'label') }))
  }
  const isRu = currentLang.value === 'ru'
  return [
    { to: '/about', label: isRu ? 'Об управлении' : 'Boshqarma haqida' },
    { to: '/leadership', label: isRu ? 'Руководство' : 'Rahbariyat' },
    { to: '/structure', label: isRu ? 'Структура' : 'Tashkiliy tuzilma' },
    { to: '/news', label: isRu ? 'Новости' : 'Yangiliklar' },
    { to: '/contact', label: isRu ? 'Контакты' : "Bog'lanish" },
  ]
})

const govLinks = computed(() => {
  if (apiFooter.value?.length > 0) {
    const gov = apiFooter.value.filter(l => l.column === 'gov')
    if (gov.length > 0) return gov.map(l => ({ url: l.url, label: t(l, 'label') }))
  }
  return [
    { url: 'https://gov.uz', label: "O'zbekiston hukumat portali" },
    { url: 'https://ssv.uz', label: "Sog'liqni saqlash vazirligi" },
    { url: 'https://my.gov.uz', label: 'Davlat xizmatlari' },
    { url: 'https://lex.uz', label: "Qonunchilik ma'lumotlari" },
  ]
})

const currentYear = new Date().getFullYear()

onMounted(() => {
  setTimeout(() => { loading.value = false }, 1800)
  window.addEventListener('scroll', handleScroll)
  applyDynamicColors()
  try {
    const saved = JSON.parse(localStorage.getItem('bvi') || '{}')
    if (saved.grayscale) bviSettings.grayscale = true
    if (saved.contrast) bviSettings.contrast = true
    if (saved.fontSize) bviSettings.fontSize = saved.fontSize
    applyBvi()
  } catch (e) {}
  nextTick(() => {
    setTimeout(() => {
      document.documentElement.classList.add('js-ready')
      initScrollAnimations()
    }, 300)
  })
})

function hexToRgb(hex) {
  if (!hex) return null
  const m = String(hex).trim().replace('#', '')
  const v = m.length === 3 ? m.split('').map(c => c + c).join('') : m
  if (!/^[0-9a-fA-F]{6}$/.test(v)) return null
  return { r: parseInt(v.slice(0, 2), 16), g: parseInt(v.slice(2, 4), 16), b: parseInt(v.slice(4, 6), 16) }
}
function setPalette(name, hex) {
  const root = document.documentElement
  const rgb = hexToRgb(hex)
  if (!rgb) return
  // Lighter shades: mix base towards white. 50 is lightest, 400 closest to base.
  const lightMix = { 50: 0.94, 100: 0.86, 200: 0.7, 300: 0.5, 400: 0.25 }
  for (const [shade, t] of Object.entries(lightMix)) {
    const r = Math.round(rgb.r + (255 - rgb.r) * t)
    const g = Math.round(rgb.g + (255 - rgb.g) * t)
    const b = Math.round(rgb.b + (255 - rgb.b) * t)
    root.style.setProperty(`--c-${name}-${shade}`, `${r} ${g} ${b}`)
  }
  root.style.setProperty(`--c-${name}-500`, `${rgb.r} ${rgb.g} ${rgb.b}`)
  // Darker shades: scale base towards black.
  const darkMix = { 600: 0.85, 700: 0.7, 800: 0.55, 900: 0.4 }
  for (const [shade, k] of Object.entries(darkMix)) {
    const r = Math.round(rgb.r * k)
    const g = Math.round(rgb.g * k)
    const b = Math.round(rgb.b * k)
    root.style.setProperty(`--c-${name}-${shade}`, `${r} ${g} ${b}`)
  }
}
function applyDynamicColors() {
  if (typeof document === 'undefined') return
  const s = siteSettings.value
  if (!s) return
  if (s.primary_color)   setPalette('primary',   s.primary_color)
  if (s.secondary_color) setPalette('secondary', s.secondary_color)
  if (s.accent_color)    setPalette('accent',    s.accent_color)
}

watch(() => siteSettings.value, applyDynamicColors, { deep: true })

onUnmounted(() => {
  window.removeEventListener('scroll', handleScroll)
  if (typeof document !== 'undefined') document.body.style.overflow = ''
})

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
    (entries) => { entries.forEach(e => { if (e.isIntersecting) e.target.classList.add('visible') }) },
    { threshold: 0.1, rootMargin: '0px 0px -50px 0px' }
  )
  document.querySelectorAll('.scroll-animate, .scroll-animate-left, .scroll-animate-right, .scroll-animate-scale')
    .forEach(el => observer.observe(el))
}
</script>

<style>
.app-root { min-height: 100vh; }
html, body { overflow-x: hidden !important; max-width: 100vw; }

.overlay-fade-enter-active, .overlay-fade-leave-active { transition: opacity 0.25s ease; }
.overlay-fade-enter-from, .overlay-fade-leave-to { opacity: 0; }

/* Maxsus imkoniyatlar (BVI) */
html.bvi-grayscale { filter: grayscale(100%); }
html.bvi-contrast { filter: contrast(140%); }
html.bvi-grayscale.bvi-contrast { filter: grayscale(100%) contrast(140%); }
html.bvi-font-large { font-size: 110%; }
html.bvi-font-xlarge { font-size: 125%; }
</style>
