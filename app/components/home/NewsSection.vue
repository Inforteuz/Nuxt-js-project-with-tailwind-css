<template>
  <section class="py-20 bg-white">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex flex-col sm:flex-row justify-between items-end mb-12 scroll-animate">
        <div>
          <h2 class="text-3xl md:text-4xl font-bold font-heading text-dark mb-4">So'nggi yangiliklar</h2>
          <div class="w-20 h-1.5 bg-gradient-to-r from-primary-500 to-secondary-500 rounded-full"></div>
        </div>
        <NuxtLink to="/news" class="hidden sm:inline-flex items-center gap-2 text-primary-500 font-semibold hover:text-primary-600 transition-colors mt-4 sm:mt-0">
          Barcha yangiliklar
          <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3"/></svg>
        </NuxtLink>
      </div>

      <div class="grid md:grid-cols-3 gap-8">
        <!-- News Card 1 -->
        <article class="news-card bg-surface border border-slate-100 scroll-animate stagger-1">
          <div class="relative h-56 overflow-hidden">
            <img src="/images/team.png" alt="Tibbiyot ko'rigi" class="w-full h-full object-cover news-image" />
            <div class="absolute top-4 left-4 bg-white/90 backdrop-blur text-primary-600 text-xs font-bold px-3 py-1.5 rounded-lg shadow-sm">
              24 May, 2026
            </div>
          </div>
          <div class="p-6">
            <div class="flex items-center gap-2 text-xs font-medium text-secondary-600 mb-3 uppercase tracking-wider">
              <span>Tadbir</span>
            </div>
            <h3 class="text-xl font-bold text-dark mb-3 line-clamp-2 leading-snug">
              Viloyat hududlarida bepul tibbiy ko'riklar tashkil etilmoqda
            </h3>
            <p class="text-slate-600 mb-5 line-clamp-3 text-sm">
              Sog'liqni saqlash boshqarmasi tashabbusi bilan chekka hududlarda aholini chuqurlashtirilgan tibbiy ko'rikdan o'tkazish tadbirlari boshlandi.
            </p>
            <NuxtLink to="/news/1" class="text-primary-500 font-semibold text-sm hover:text-primary-600 flex items-center gap-1">
              Batafsil o'qish
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/></svg>
            </NuxtLink>
          </div>
        </article>

        <!-- News Card 2 -->
        <article class="news-card bg-surface border border-slate-100 scroll-animate stagger-2">
          <div class="relative h-56 overflow-hidden">
            <img src="/images/equipment.png" alt="Yangi uskuna" class="w-full h-full object-cover news-image" />
            <div class="absolute top-4 left-4 bg-white/90 backdrop-blur text-primary-600 text-xs font-bold px-3 py-1.5 rounded-lg shadow-sm">
              22 May, 2026
            </div>
          </div>
          <div class="p-6">
            <div class="flex items-center gap-2 text-xs font-medium text-secondary-600 mb-3 uppercase tracking-wider">
              <span>Yangilik</span>
            </div>
            <h3 class="text-xl font-bold text-dark mb-3 line-clamp-2 leading-snug">
              Tuman shifoxonasiga yangi rentgen uskunasi keltirildi
            </h3>
            <p class="text-slate-600 mb-5 line-clamp-3 text-sm">
              Tibbiyot muassasalarini zamonaviy tibbiy uskunalar bilan ta'minlash dasturi doirasida navbatdagi jihozlar topshirildi.
            </p>
            <NuxtLink to="/news/2" class="text-primary-500 font-semibold text-sm hover:text-primary-600 flex items-center gap-1">
              Batafsil o'qish
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/></svg>
            </NuxtLink>
          </div>
        </article>

        <!-- News Card 3 -->
        <article class="news-card bg-surface border border-slate-100 scroll-animate stagger-3">
          <div class="relative h-56 overflow-hidden">
            <img src="/images/building.png" alt="Seminar" class="w-full h-full object-cover news-image" />
            <div class="absolute top-4 left-4 bg-white/90 backdrop-blur text-primary-600 text-xs font-bold px-3 py-1.5 rounded-lg shadow-sm">
              20 May, 2026
            </div>
          </div>
          <div class="p-6">
            <div class="flex items-center gap-2 text-xs font-medium text-secondary-600 mb-3 uppercase tracking-wider">
              <span>Press-reliz</span>
            </div>
            <h3 class="text-xl font-bold text-dark mb-3 line-clamp-2 leading-snug">
              Viloyat shifokorlari uchun xalqaro o'quv-seminar o'tkazildi
            </h3>
            <p class="text-slate-600 mb-5 line-clamp-3 text-sm">
              Xorijiy mutaxassislar ishtirokida o'tkazilgan seminarda kasalliklarni barvaqt aniqlash bo'yicha zamonaviy metodlar muhokama qilindi.
            </p>
            <NuxtLink to="/news/3" class="text-primary-500 font-semibold text-sm hover:text-primary-600 flex items-center gap-1">
              Batafsil o'qish
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/></svg>
            </NuxtLink>
          </div>
        </article>
      </div>

      <div class="mt-10 text-center sm:hidden">
        <NuxtLink to="/news" class="btn-outline inline-block">
          Barcha yangiliklarni ko'rish
        </NuxtLink>
      </div>
    </div>
  </section>
</template>

<script setup>
</script>
