<template>
  <section class="py-24 bg-gradient-to-b from-white to-slate-50 relative overflow-hidden">
    <!-- Decorative background elements -->
    <div class="absolute top-0 left-0 w-full h-full overflow-hidden z-0 pointer-events-none">
      <div class="absolute -top-[20%] -right-[10%] w-[50%] h-[50%] rounded-full bg-primary-50/50 blur-3xl"></div>
      <div class="absolute top-[60%] -left-[10%] w-[40%] h-[40%] rounded-full bg-secondary-50/50 blur-3xl"></div>
    </div>

    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
      <div class="text-center max-w-3xl mx-auto mb-20 scroll-animate">
        <h2 class="text-sm font-bold text-primary-600 uppercase tracking-widest mb-3">Asosiy vazifalarimiz</h2>
        <h3 class="text-3xl md:text-5xl font-extrabold font-heading text-slate-900 mb-6 tracking-tight">Boshqarma faoliyati</h3>
        <p class="text-lg text-slate-600 leading-relaxed">
          Andijon viloyati hokimligi sog'liqni saqlash boshqarmasi viloyatdagi barcha tibbiyot muassasalari faoliyatini muvofiqlashtiruvchi va boshqaruvchi asosiy davlat organidir.
        </p>
      </div>

      <div class="grid md:grid-cols-3 gap-8 lg:gap-10">
        <!-- Card 1 -->
        <div class="group bg-white rounded-3xl p-10 shadow-[0_10px_40px_rgba(0,0,0,0.04)] hover:shadow-[0_20px_60px_rgba(0,0,0,0.08)] border border-slate-100/50 transition-all duration-500 hover:-translate-y-2 scroll-animate stagger-1">
          <div class="w-16 h-16 rounded-2xl bg-gradient-to-br from-primary-100 to-primary-50 flex items-center justify-center mb-8 group-hover:scale-110 transition-transform duration-500 shadow-inner">
            <svg class="w-8 h-8 text-primary-600" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4"/></svg>
          </div>
          <h4 class="text-2xl font-bold text-slate-900 mb-4 font-heading group-hover:text-primary-600 transition-colors">Tashkilot maqomi</h4>
          <p class="text-slate-600 mb-8 leading-relaxed">
            O'zbekiston Respublikasi Sog'liqni saqlash vazirligi va Andijon viloyati hokimligiga bo'ysunuvchi davlat boshqaruvi organi.
          </p>
          <NuxtLink to="/about" class="inline-flex items-center gap-2 text-primary-600 font-bold hover:text-primary-700 transition-colors">
            Batafsil 
            <svg class="w-5 h-5 transform group-hover:translate-x-2 transition-transform duration-300" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3"/></svg>
          </NuxtLink>
        </div>

        <!-- Card 2 -->
        <div class="group bg-white rounded-3xl p-10 shadow-[0_10px_40px_rgba(0,0,0,0.04)] hover:shadow-[0_20px_60px_rgba(0,0,0,0.08)] border border-slate-100/50 transition-all duration-500 hover:-translate-y-2 scroll-animate stagger-2 relative overflow-hidden">
          <div class="absolute top-0 right-0 w-32 h-32 bg-secondary-50/50 rounded-bl-full -z-10 group-hover:scale-150 transition-transform duration-700"></div>
          <div class="w-16 h-16 rounded-2xl bg-gradient-to-br from-secondary-100 to-secondary-50 flex items-center justify-center mb-8 group-hover:scale-110 transition-transform duration-500 shadow-inner">
            <svg class="w-8 h-8 text-secondary-600" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"/></svg>
          </div>
          <h4 class="text-2xl font-bold text-slate-900 mb-4 font-heading group-hover:text-secondary-600 transition-colors">Vazifa va funksiyalar</h4>
          <p class="text-slate-600 mb-8 leading-relaxed">
            Aholiga malakali tibbiy yordam ko'rsatishni tashkil etish, kasalliklar profilaktikasi va sog'lom turmush tarzini targ'ib qilish.
          </p>
          <NuxtLink to="/about" class="inline-flex items-center gap-2 text-secondary-600 font-bold hover:text-secondary-700 transition-colors">
            Batafsil 
            <svg class="w-5 h-5 transform group-hover:translate-x-2 transition-transform duration-300" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3"/></svg>
          </NuxtLink>
        </div>

        <!-- Card 3 -->
        <div class="group bg-white rounded-3xl p-10 shadow-[0_10px_40px_rgba(0,0,0,0.04)] hover:shadow-[0_20px_60px_rgba(0,0,0,0.08)] border border-slate-100/50 transition-all duration-500 hover:-translate-y-2 scroll-animate stagger-3">
          <div class="w-16 h-16 rounded-2xl bg-gradient-to-br from-teal-100 to-teal-50 flex items-center justify-center mb-8 group-hover:scale-110 transition-transform duration-500 shadow-inner">
            <svg class="w-8 h-8 text-teal-600" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0z"/></svg>
          </div>
          <h4 class="text-2xl font-bold text-slate-900 mb-4 font-heading group-hover:text-teal-600 transition-colors">Rahbariyat</h4>
          <p class="text-slate-600 mb-8 leading-relaxed">
            Boshqarma boshlig'i va o'rinbosarlarining qabul kunlari, bog'lanish ma'lumotlari va tarjimai holi bilan tanishishingiz mumkin.
          </p>
          <NuxtLink to="/leadership" class="inline-flex items-center gap-2 text-teal-600 font-bold hover:text-teal-700 transition-colors">
            Batafsil 
            <svg class="w-5 h-5 transform group-hover:translate-x-2 transition-transform duration-300" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3"/></svg>
          </NuxtLink>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
</script>
