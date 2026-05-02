<template>
  <div class="pt-24 pb-20 bg-slate-50 min-h-screen">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">

      <div class="text-center mb-16">
        <div class="w-16 h-16 bg-primary-50 text-primary-600 rounded-2xl flex items-center justify-center mx-auto mb-6">
          <svg class="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0z"/></svg>
        </div>
        <h1 class="text-3xl md:text-4xl font-heading font-bold text-dark mb-4">Boshqarma rahbariyati</h1>
        <div class="w-20 h-1.5 bg-gradient-to-r from-primary-500 to-secondary-500 rounded-full mx-auto"></div>
      </div>

      <div v-if="pending" class="flex justify-center py-20">
        <div class="w-12 h-12 border-4 border-primary-200 border-t-primary-600 rounded-full animate-spin"></div>
      </div>

      <div v-else-if="leaders && leaders.length > 0" class="grid lg:grid-cols-2 gap-8 lg:gap-12">
        <div v-for="leader in leaders" :key="leader.id" class="bg-white rounded-3xl shadow-sm hover:shadow-lg border border-slate-100 overflow-hidden flex flex-col sm:flex-row transition-shadow">
          <div class="w-full sm:w-2/5 h-64 sm:h-auto bg-slate-100 flex-shrink-0">
            <img :src="leader.image || '/images/team.png'" :alt="t(leader, 'full_name')" class="w-full h-full object-cover object-top" />
          </div>

          <div class="p-6 sm:p-8 w-full sm:w-3/5 flex flex-col justify-center">
            <p class="text-secondary-600 font-bold text-sm uppercase tracking-wider mb-2">{{ t(leader.position, 'name') }}</p>
            <h3 class="text-2xl font-bold font-heading text-dark mb-4">{{ t(leader, 'full_name') }}</h3>

            <div class="space-y-3 mb-4">
              <div v-if="leader.phone" class="flex items-start gap-3 text-slate-600">
                <svg class="w-5 h-5 text-slate-400 mt-0.5 flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"/></svg>
                <a :href="`tel:${leader.phone}`" class="hover:text-primary-600 transition-colors">{{ leader.phone }}</a>
              </div>
              <div v-if="leader.email" class="flex items-start gap-3 text-slate-600">
                <svg class="w-5 h-5 text-slate-400 mt-0.5 flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"/></svg>
                <a :href="`mailto:${leader.email}`" class="hover:text-primary-600 transition-colors">{{ leader.email }}</a>
              </div>
              <div v-if="t(leader, 'reception_days')" class="flex items-start gap-3 text-slate-600">
                <svg class="w-5 h-5 text-slate-400 mt-0.5 flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
                <div class="text-sm">
                  <p class="font-medium text-slate-700">Qabul kunlari:</p>
                  <p>{{ t(leader, 'reception_days') }}</p>
                </div>
              </div>
            </div>

            <div v-if="t(leader, 'biography')" class="mt-2">
              <details class="text-sm text-slate-600">
                <summary class="cursor-pointer text-primary-600 font-medium hover:text-primary-700">Biografiya</summary>
                <p class="mt-2 whitespace-pre-line leading-relaxed">{{ t(leader, 'biography') }}</p>
              </details>
            </div>
          </div>
        </div>
      </div>

      <div v-else class="text-center py-20 bg-white rounded-2xl shadow-sm border border-slate-100">
        <h3 class="text-xl font-bold text-dark mb-2">Ma'lumot topilmadi</h3>
        <p class="text-slate-500">Tez orada bu yerda rahbariyat ma'lumotlari paydo bo'ladi.</p>
      </div>

    </div>
  </div>
</template>

<script setup>
import { useRuntimeConfig, useFetch } from '#imports'

useHead({ title: "Rahbariyat - Andijon SSB" })

const config = useRuntimeConfig()
const { t } = useLanguage()
const { data: leaders, pending } = await useFetch(`${config.public.apiBase}/leaders/`)
</script>
