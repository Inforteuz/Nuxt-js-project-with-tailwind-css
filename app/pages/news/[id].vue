<template>
  <div class="pt-24 pb-16 min-h-[60vh] flex flex-col items-center justify-center text-center px-4">
    <div class="w-16 h-16 bg-primary-50 text-primary-600 rounded-2xl flex items-center justify-center mb-6">
      <svg class="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 20H5a2 2 0 01-2-2V6a2 2 0 012-2h10a2 2 0 012 2v1m2 13a2 2 0 01-2-2V7m2 13a2 2 0 002-2V9a2 2 0 00-2-2h-2m-4-3H9M7 16h6M7 8h6v4H7V8z"/></svg>
    </div>
    <h1 class="text-3xl font-heading font-bold text-dark mb-4">Yangilik tafsilotlari</h1>
    <p class="text-slate-500 max-w-lg mb-8">Ushbu sahifa hozirda ishlab chiqilmoqda. Tez orada to'liq ma'lumotlar kiritiladi.</p>
    <NuxtLink to="/news" class="btn-primary">Yangiliklarga qaytish</NuxtLink>
  </div>
</template>

<script setup>
useHead({ title: "Yangilik - Andijon SSB" })
</script>
