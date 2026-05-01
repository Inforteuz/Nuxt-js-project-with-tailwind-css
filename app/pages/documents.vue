<template>
  <div class="pt-24 pb-16 min-h-[60vh] flex flex-col items-center justify-center text-center px-4">
    <div class="w-16 h-16 bg-primary-50 text-primary-600 rounded-2xl flex items-center justify-center mb-6">
      <svg class="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/></svg>
    </div>
    <h1 class="text-3xl font-heading font-bold text-dark mb-4">Hujjatlar</h1>
    <p class="text-slate-500 max-w-lg mb-8">Ushbu sahifa hozirda ishlab chiqilmoqda. Tez orada to'liq ma'lumotlar kiritiladi.</p>
    <NuxtLink to="/" class="btn-primary">Bosh sahifaga qaytish</NuxtLink>
  </div>
</template>

<script setup>
useHead({ title: "Hujjatlar - Andijon SSB" })
</script>
