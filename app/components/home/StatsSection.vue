<template>
  <section class="stats-gradient py-16 relative">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
      <div class="grid grid-cols-2 md:grid-cols-4 gap-8 divide-x divide-white/10">
        <!-- Stat 1 -->
        <div class="text-center px-4 scroll-animate stagger-1">
          <div class="text-secondary-400 mb-3 flex justify-center">
            <svg class="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4"/></svg>
          </div>
          <div class="text-4xl font-bold text-white mb-2 counter-number">240<span class="text-secondary-400">+</span></div>
          <p class="text-sm text-slate-300 font-medium uppercase tracking-wider">Tibbiyot muassasalari</p>
        </div>

        <!-- Stat 2 -->
        <div class="text-center px-4 scroll-animate stagger-2">
          <div class="text-secondary-400 mb-3 flex justify-center">
            <svg class="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0z"/></svg>
          </div>
          <div class="text-4xl font-bold text-white mb-2 counter-number">5000<span class="text-secondary-400">+</span></div>
          <p class="text-sm text-slate-300 font-medium uppercase tracking-wider">Malakali shifokorlar</p>
        </div>

        <!-- Stat 3 -->
        <div class="text-center px-4 scroll-animate stagger-3">
          <div class="text-secondary-400 mb-3 flex justify-center">
            <svg class="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z"/></svg>
          </div>
          <div class="text-4xl font-bold text-white mb-2 counter-number">3.2<span class="text-secondary-400">M</span></div>
          <p class="text-sm text-slate-300 font-medium uppercase tracking-wider">Aholi qamrovi</p>
        </div>

        <!-- Stat 4 -->
        <div class="text-center px-4 scroll-animate stagger-4">
          <div class="text-secondary-400 mb-3 flex justify-center">
            <svg class="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
          </div>
          <div class="text-4xl font-bold text-white mb-2 counter-number">30<span class="text-secondary-400">+</span></div>
          <p class="text-sm text-slate-300 font-medium uppercase tracking-wider">Yillik dasturlar</p>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
// Note: In a real scenario we'd use intersection observer to trigger counter animation
</script>
