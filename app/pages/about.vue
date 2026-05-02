<template>
  <div class="pt-24 pb-20 bg-slate-50 min-h-screen">
    <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <!-- Orqaga qaytish -->
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
            <p class="text-slate-500">{{ generalInfo?.name_uz || "Andijon viloyati sog'liqni saqlash boshqarmasi" }}</p>
          </div>
        </div>

        <div v-if="pending" class="flex justify-center py-10">
          <div class="w-10 h-10 border-4 border-primary-200 border-t-primary-600 rounded-full animate-spin"></div>
        </div>
        
        <div v-else class="space-y-10">
          <!-- Boshqarma faoliyati -->
          <section>
            <h2 class="text-xl font-bold text-dark mb-4">Vazifa va funksiyalari</h2>
            <div class="prose prose-slate max-w-none text-slate-600 whitespace-pre-line leading-relaxed">
              {{ generalInfo?.about_uz || "Ma'lumot topilmadi" }}
            </div>
          </section>

          <!-- Tarix -->
          <section v-if="generalInfo?.history_uz">
            <h2 class="text-xl font-bold text-dark mb-4">Boshqarma tarixi</h2>
            <div class="prose prose-slate max-w-none text-slate-600 whitespace-pre-line leading-relaxed p-6 bg-slate-50 rounded-2xl border border-slate-100">
              {{ generalInfo.history_uz }}
            </div>
          </section>
          
          <!-- Nizom -->
          <section v-if="generalInfo?.statute_link" class="pt-6">
            <a :href="generalInfo.statute_link" target="_blank" class="inline-flex items-center gap-2 btn-outline">
              <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/></svg>
              Boshqarma nizomi bilan tanishish
            </a>
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
const { data: generalInfo, pending } = await useFetch(`${config.public.apiBase}/info/`)
</script>
