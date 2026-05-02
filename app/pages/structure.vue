<template>
  <div class="pt-24 pb-20 bg-slate-50 min-h-screen">
    <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">

      <div class="text-center mb-16">
        <div class="w-16 h-16 bg-primary-50 text-primary-600 rounded-2xl flex items-center justify-center mx-auto mb-6">
          <svg class="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 5a1 1 0 011-1h14a1 1 0 011 1v2a1 1 0 01-1 1H5a1 1 0 01-1-1V5zM4 13a1 1 0 011-1h6a1 1 0 011 1v6a1 1 0 01-1 1H5a1 1 0 01-1-1v-6zM16 13a1 1 0 011-1h2a1 1 0 011 1v6a1 1 0 01-1 1h-2a1 1 0 01-1-1v-6z"/></svg>
        </div>
        <h1 class="text-3xl md:text-4xl font-heading font-bold text-dark mb-4">Tashkiliy tuzilma</h1>
        <div class="w-20 h-1.5 bg-gradient-to-r from-primary-500 to-secondary-500 rounded-full mx-auto"></div>
      </div>

      <div v-if="pending" class="flex justify-center py-20">
        <div class="w-12 h-12 border-4 border-primary-200 border-t-primary-600 rounded-full animate-spin"></div>
      </div>

      <div v-else-if="departments && departments.length > 0" class="space-y-6">
        <div v-for="dept in departments" :key="dept.id" class="bg-white rounded-2xl p-6 md:p-8 shadow-sm hover:shadow-md border border-slate-100 transition-shadow">
          <div class="flex flex-col md:flex-row gap-6 items-start">
            <div class="w-12 h-12 rounded-full bg-primary-50 flex items-center justify-center flex-shrink-0">
              <span class="text-xl font-bold text-primary-600">{{ t(dept, 'name')?.charAt(0) }}</span>
            </div>
            <div class="flex-1">
              <h3 class="text-xl font-bold font-heading text-dark mb-3">{{ t(dept, 'name') }}</h3>
              <p v-if="t(dept, 'description')" class="text-slate-600 mb-4 whitespace-pre-line text-sm leading-relaxed">{{ t(dept, 'description') }}</p>

              <div v-if="t(dept, 'head_name')" class="inline-flex items-center gap-3 bg-slate-50 px-4 py-2 rounded-lg border border-slate-100">
                <svg class="w-5 h-5 text-slate-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"/></svg>
                <div class="text-sm">
                  <span class="text-slate-500 block text-xs">Bo'lim boshlig'i:</span>
                  <span class="font-semibold text-slate-800">{{ t(dept, 'head_name') }}</span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div v-else class="text-center py-20 bg-white rounded-2xl shadow-sm border border-slate-100">
        <h3 class="text-xl font-bold text-dark mb-2">Ma'lumot topilmadi</h3>
        <p class="text-slate-500">Tez orada bu yerda tuzilma haqida ma'lumotlar paydo bo'ladi.</p>
      </div>

    </div>
  </div>
</template>

<script setup>
import { useRuntimeConfig, useFetch } from '#imports'

useHead({ title: "Tashkiliy tuzilma - Andijon SSB" })

const config = useRuntimeConfig()
const { t } = useLanguage()
const { data: departments, pending } = await useFetch(`${config.public.apiBase}/structure/`)
</script>
