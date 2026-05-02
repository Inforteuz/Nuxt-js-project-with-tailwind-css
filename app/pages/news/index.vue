<template>
  <div class="pt-24 pb-20 bg-slate-50 min-h-screen">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="text-center mb-12">
        <h1 class="text-3xl md:text-4xl font-heading font-bold text-dark mb-4">Yangiliklar</h1>
        <div class="w-20 h-1.5 bg-gradient-to-r from-primary-500 to-secondary-500 rounded-full mx-auto"></div>
      </div>

      <div v-if="pending" class="flex justify-center items-center py-20">
        <div class="w-12 h-12 border-4 border-primary-200 border-t-primary-600 rounded-full animate-spin"></div>
      </div>

      <div v-else-if="error" class="text-center py-20 text-red-500 bg-red-50 rounded-2xl">
        Ma'lumotlarni yuklashda xatolik yuz berdi. Iltimos, keyinroq qayta urinib ko'ring.
      </div>

      <div v-else-if="newsItems && newsItems.length > 0" class="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
        <article v-for="item in newsItems" :key="item.id" class="news-card bg-white rounded-2xl shadow-sm hover:shadow-xl border border-slate-100 transition-all duration-300 transform hover:-translate-y-1 flex flex-col h-full overflow-hidden">
          <div class="relative h-56 overflow-hidden flex-shrink-0">
            <img :src="item.image || '/images/team.png'" :alt="t(item, 'title')" class="w-full h-full object-cover transition-transform duration-700 hover:scale-110" />
            <div class="absolute top-4 left-4 bg-white/90 backdrop-blur text-primary-600 text-xs font-bold px-3 py-1.5 rounded-lg shadow-sm">
              {{ new Date(item.published_at || item.created_at).toLocaleDateString('uz-UZ', { day: '2-digit', month: 'short', year: 'numeric' }) }}
            </div>
          </div>
          <div class="p-6 flex flex-col flex-grow">
            <div class="flex items-center gap-2 text-xs font-medium text-secondary-600 mb-3 uppercase tracking-wider">
              <span>{{ t(item.category, 'name') || 'Yangilik' }}</span>
              <span v-if="item.views_count" class="flex items-center gap-1 text-slate-400 lowercase ml-auto">
                <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"/><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"/></svg>
                {{ item.views_count }}
              </span>
            </div>
            <h3 class="text-xl font-bold text-dark mb-3 line-clamp-2 leading-snug">{{ t(item, 'title') }}</h3>
            <p class="text-slate-600 mb-6 line-clamp-3 text-sm flex-grow">
              {{ t(item, 'content')?.substring(0, 120) + '...' }}
            </p>
            <div class="mt-auto pt-4 border-t border-slate-50">
              <NuxtLink :to="`/news/${item.slug || item.id}`" class="text-primary-500 font-semibold text-sm hover:text-primary-600 flex items-center gap-1 group">
                Batafsil o'qish
                <svg class="w-4 h-4 transform group-hover:translate-x-1 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3"/></svg>
              </NuxtLink>
            </div>
          </div>
        </article>
      </div>

      <div v-else class="text-center py-20 bg-white rounded-2xl shadow-sm border border-slate-100">
        <div class="w-20 h-20 bg-slate-50 rounded-full flex items-center justify-center mx-auto mb-4">
          <svg class="w-10 h-10 text-slate-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 20H5a2 2 0 01-2-2V6a2 2 0 012-2h10a2 2 0 012 2v1m2 13a2 2 0 01-2-2V7m2 13a2 2 0 002-2V9a2 2 0 00-2-2h-2m-4-3H9M7 16h6M7 8h6v4H7V8z"/></svg>
        </div>
        <h3 class="text-xl font-bold text-dark mb-2">Hozircha yangiliklar yo'q</h3>
        <p class="text-slate-500">Tez orada bu yerda ma'lumotlar paydo bo'ladi.</p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useRuntimeConfig, useFetch, computed } from '#imports'

useHead({ title: "Yangiliklar - Andijon SSB" })

const config = useRuntimeConfig()
const { t } = useLanguage()

const { data, pending, error } = await useFetch(`${config.public.apiBase}/news/`)

const newsItems = computed(() => {
  if (!data.value) return []
  return data.value.results || data.value
})
</script>
