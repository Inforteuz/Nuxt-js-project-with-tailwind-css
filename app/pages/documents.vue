<template>
  <div class="pt-24 pb-20 bg-slate-50 min-h-screen">
    <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">

      <div class="text-center mb-16">
        <div class="w-16 h-16 bg-primary-50 text-primary-600 rounded-2xl flex items-center justify-center mx-auto mb-6">
          <svg class="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/></svg>
        </div>
        <h1 class="text-3xl md:text-4xl font-heading font-bold text-dark mb-4">Normativ-huquqiy hujjatlar</h1>
        <div class="w-20 h-1.5 bg-gradient-to-r from-primary-500 to-secondary-500 rounded-full mx-auto"></div>
      </div>

      <div v-if="pending" class="flex justify-center py-20">
        <div class="w-12 h-12 border-4 border-primary-200 border-t-primary-600 rounded-full animate-spin"></div>
      </div>

      <div v-else-if="documents && documents.length > 0" class="bg-white rounded-3xl shadow-sm border border-slate-100 overflow-hidden">
        <div class="overflow-x-auto">
          <table class="w-full text-left border-collapse">
            <thead>
              <tr class="bg-slate-50/80 border-b border-slate-100 text-slate-500 font-medium text-sm">
                <th class="py-4 px-6 w-16 text-center">#</th>
                <th class="py-4 px-6 min-w-[200px]">Hujjat nomi va raqami</th>
                <th class="py-4 px-6 w-48">Kategoriya</th>
                <th class="py-4 px-6 w-40">Sana</th>
                <th class="py-4 px-6 w-32 text-center">Fayl</th>
              </tr>
            </thead>
            <tbody class="divide-y divide-slate-100">
              <tr v-for="(doc, index) in documents" :key="doc.id" class="hover:bg-slate-50/50 transition-colors group">
                <td class="py-5 px-6 text-center text-slate-400 font-medium">{{ index + 1 }}</td>
                <td class="py-5 px-6">
                  <div class="font-semibold text-dark mb-1 leading-snug">{{ t(doc, 'title') }}</div>
                  <div class="text-xs text-slate-500" v-if="doc.number">№ {{ doc.number }}</div>
                </td>
                <td class="py-5 px-6">
                  <span class="inline-flex items-center px-2.5 py-1 rounded-md text-xs font-medium bg-slate-100 text-slate-600">
                    {{ t(doc.category, 'name') || 'Hujjat' }}
                  </span>
                </td>
                <td class="py-5 px-6 text-sm text-slate-600">
                  {{ new Date(doc.date).toLocaleDateString('uz-UZ', { day: '2-digit', month: 'short', year: 'numeric' }) }}
                </td>
                <td class="py-5 px-6 text-center">
                  <a v-if="doc.file" :href="doc.file" target="_blank" download class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-primary-50 text-primary-600 hover:bg-primary-600 hover:text-white transition-colors" title="Yuklab olish">
                    <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4"/></svg>
                  </a>
                  <a v-else-if="doc.link" :href="doc.link" target="_blank" class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-slate-100 text-slate-600 hover:bg-slate-200 transition-colors" title="Havolaga o'tish">
                    <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14"/></svg>
                  </a>
                  <span v-else class="text-slate-300">—</span>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

      <div v-else class="text-center py-20 bg-white rounded-2xl shadow-sm border border-slate-100">
        <h3 class="text-xl font-bold text-dark mb-2">Ma'lumot topilmadi</h3>
        <p class="text-slate-500">Tez orada bu yerda hujjatlar paydo bo'ladi.</p>
      </div>

    </div>
  </div>
</template>

<script setup>
import { useRuntimeConfig, useFetch } from '#imports'

useHead({ title: "Hujjatlar - Andijon SSB" })

const config = useRuntimeConfig()
const { t } = useLanguage()
const { data: documents, pending } = await useFetch(`${config.public.apiBase}/documents/`)
</script>
