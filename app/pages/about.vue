<template>
  <div class="pt-24 pb-20 bg-slate-50 min-h-screen">
    <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">

      <NuxtLink to="/" class="inline-flex items-center gap-2 text-slate-500 hover:text-primary-600 transition-colors mb-8 font-medium">
        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18"/></svg>
        Bosh sahifaga qaytish
      </NuxtLink>

      <div class="bg-white rounded-3xl shadow-sm border border-slate-100 p-8 md:p-12">
        <div class="flex items-center gap-4 mb-8 pb-8 border-b border-slate-100">
          <div class="w-16 h-16 bg-primary-50 text-primary-600 rounded-2xl flex items-center justify-center flex-shrink-0">
            <svg class="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
          </div>
          <div>
            <h1 class="text-2xl md:text-3xl font-heading font-bold text-dark mb-2">Boshqarma haqida</h1>
            <p class="text-slate-500">{{ t(generalInfo, 'name') || "Andijon viloyati sog'liqni saqlash boshqarmasi" }}</p>
          </div>
        </div>

        <div v-if="pending" class="flex justify-center py-10">
          <div class="w-10 h-10 border-4 border-primary-200 border-t-primary-600 rounded-full animate-spin"></div>
        </div>

        <div v-else class="space-y-10">
          <section v-if="t(generalInfo, 'about')">
            <h2 class="text-xl font-bold text-dark mb-4">Vazifa va funksiyalari</h2>
            <div class="prose prose-slate max-w-none text-slate-600 whitespace-pre-line leading-relaxed">
              {{ t(generalInfo, 'about') }}
            </div>
          </section>
          <section v-else>
            <h2 class="text-xl font-bold text-dark mb-4">Vazifa va funksiyalari</h2>
            <p class="text-slate-500">Ma'lumot kiritilmagan</p>
          </section>

          <section v-if="t(generalInfo, 'history')">
            <h2 class="text-xl font-bold text-dark mb-4">Boshqarma tarixi</h2>
            <div class="prose prose-slate max-w-none text-slate-600 whitespace-pre-line leading-relaxed p-6 bg-slate-50 rounded-2xl border border-slate-100">
              {{ t(generalInfo, 'history') }}
            </div>
          </section>

          <section v-if="generalInfo?.statute_link" class="pt-6">
            <a :href="generalInfo.statute_link" target="_blank" class="inline-flex items-center gap-2 btn-outline">
              <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/></svg>
              Boshqarma nizomi bilan tanishish
            </a>
          </section>

          <!-- Aloqa ma'lumotlari -->
          <section class="grid grid-cols-1 md:grid-cols-2 gap-6 pt-4 border-t border-slate-100">
            <div class="flex items-start gap-3">
              <div class="w-10 h-10 bg-primary-50 rounded-xl flex items-center justify-center flex-shrink-0">
                <svg class="w-5 h-5 text-primary-600" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"/></svg>
              </div>
              <div>
                <p class="text-xs text-slate-400 mb-1 font-medium uppercase tracking-wider">Manzil</p>
                <p class="text-slate-700">{{ t(generalInfo, 'address') || '710000, Andijon shahar' }}</p>
              </div>
            </div>
            <div class="flex items-start gap-3">
              <div class="w-10 h-10 bg-secondary-50 rounded-xl flex items-center justify-center flex-shrink-0">
                <svg class="w-5 h-5 text-secondary-600" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"/></svg>
              </div>
              <div>
                <p class="text-xs text-slate-400 mb-1 font-medium uppercase tracking-wider">Telefon</p>
                <a :href="`tel:${generalInfo?.phone}`" class="text-slate-700 hover:text-primary-600">{{ generalInfo?.phone }}</a>
              </div>
            </div>
            <div class="flex items-start gap-3" v-if="generalInfo?.email">
              <div class="w-10 h-10 bg-accent-50 rounded-xl flex items-center justify-center flex-shrink-0">
                <svg class="w-5 h-5 text-accent-600" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"/></svg>
              </div>
              <div>
                <p class="text-xs text-slate-400 mb-1 font-medium uppercase tracking-wider">Email</p>
                <a :href="`mailto:${generalInfo.email}`" class="text-slate-700 hover:text-primary-600">{{ generalInfo.email }}</a>
              </div>
            </div>
            <div class="flex items-start gap-3" v-if="t(generalInfo, 'work_hours')">
              <div class="w-10 h-10 bg-slate-100 rounded-xl flex items-center justify-center flex-shrink-0">
                <svg class="w-5 h-5 text-slate-600" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
              </div>
              <div>
                <p class="text-xs text-slate-400 mb-1 font-medium uppercase tracking-wider">Ish vaqti</p>
                <p class="text-slate-700">{{ t(generalInfo, 'work_hours') }}</p>
              </div>
            </div>
          </section>
        </div>
      </div>

    </div>
  </div>
</template>

<script setup>
import { useRuntimeConfig, useFetch } from '#imports'

useHead({ title: "Boshqarma haqida - Andijon SSB" })

const config = useRuntimeConfig()
const { t } = useLanguage()
const { data: generalInfo, pending } = await useFetch(`${config.public.apiBase}/info/`)
</script>
