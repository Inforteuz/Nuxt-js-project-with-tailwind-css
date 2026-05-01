<template>
  <div class="pt-24 pb-16 min-h-[60vh] flex flex-col items-center justify-center text-center px-4">
    <div class="w-16 h-16 bg-primary-50 text-primary-600 rounded-2xl flex items-center justify-center mb-6">
      <svg class="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"/></svg>
    </div>
    <h1 class="text-3xl font-heading font-bold text-dark mb-4">Bog'lanish</h1>
    <p class="text-slate-500 max-w-lg mb-8">Ushbu sahifa hozirda ishlab chiqilmoqda. Tez orada to'liq ma'lumotlar kiritiladi.</p>
    <NuxtLink to="/" class="btn-primary">Bosh sahifaga qaytish</NuxtLink>
  </div>
</template>

<script setup>
useHead({ title: "Bog'lanish - Andijon SSB" })
</script>
