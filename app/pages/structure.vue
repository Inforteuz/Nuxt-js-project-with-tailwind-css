<template>
  <div class="pt-24 pb-16 min-h-[60vh] flex flex-col items-center justify-center text-center px-4">
    <div class="w-16 h-16 bg-primary-50 text-primary-600 rounded-2xl flex items-center justify-center mb-6">
      <svg class="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 5a1 1 0 011-1h14a1 1 0 011 1v2a1 1 0 01-1 1H5a1 1 0 01-1-1V5zM4 13a1 1 0 011-1h6a1 1 0 011 1v6a1 1 0 01-1 1H5a1 1 0 01-1-1v-6zM16 13a1 1 0 011-1h2a1 1 0 011 1v6a1 1 0 01-1 1h-2a1 1 0 01-1-1v-6z"/></svg>
    </div>
    <h1 class="text-3xl font-heading font-bold text-dark mb-4">Tashkiliy tuzilma</h1>
    <p class="text-slate-500 max-w-lg mb-8">Ushbu sahifa hozirda ishlab chiqilmoqda. Tez orada to'liq ma'lumotlar kiritiladi.</p>
    <NuxtLink to="/" class="btn-primary">Bosh sahifaga qaytish</NuxtLink>
  </div>
</template>

<script setup>
useHead({ title: "Tashkiliy tuzilma - Andijon SSB" })
</script>
