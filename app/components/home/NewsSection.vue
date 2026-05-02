<template>
  <section class="py-20 bg-white">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex flex-col sm:flex-row justify-between items-end mb-12 scroll-animate">
        <div>
          <h2 class="text-3xl md:text-4xl font-bold font-heading text-dark mb-4">So'nggi yangiliklar</h2>
          <div class="w-20 h-1.5 bg-gradient-to-r from-primary-500 to-secondary-500 rounded-full"></div>
        </div>
        <NuxtLink to="/news" class="hidden sm:inline-flex items-center gap-2 text-primary-500 font-semibold hover:text-primary-600 transition-colors mt-4 sm:mt-0">
          Barcha yangiliklar
          <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3"/></svg>
        </NuxtLink>
      </div>

      <div class="grid md:grid-cols-3 gap-8">
        <!-- News Cards -->
        <article v-for="(item, index) in newsItems" :key="item.id" class="news-card bg-surface border border-slate-100 scroll-animate" :class="`stagger-${index + 1}`">
          <div class="relative h-56 overflow-hidden">
            <img :src="item.image || '/images/team.png'" :alt="item.title_uz" class="w-full h-full object-cover news-image" />
            <div class="absolute top-4 left-4 bg-white/90 backdrop-blur text-primary-600 text-xs font-bold px-3 py-1.5 rounded-lg shadow-sm">
              {{ new Date(item.created_at).toLocaleDateString('uz-UZ', { day: '2-digit', month: 'short', year: 'numeric' }) }}
            </div>
          </div>
          <div class="p-6">
            <div class="flex items-center gap-2 text-xs font-medium text-secondary-600 mb-3 uppercase tracking-wider">
              <span>{{ item.category?.name_uz || 'Yangilik' }}</span>
              <span class="flex items-center gap-1 text-slate-400 lowercase ml-auto">
                <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"/><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"/></svg>
                {{ item.views }}
              </span>
            </div>
            <h3 class="text-xl font-bold text-dark mb-3 line-clamp-2 leading-snug">
              {{ item.title_uz }}
            </h3>
            <p class="text-slate-600 mb-5 line-clamp-3 text-sm">
              {{ item.short_description_uz || item.content_uz?.substring(0, 100) + '...' }}
            </p>
            <NuxtLink :to="`/news/${item.slug || item.id}`" class="text-primary-500 font-semibold text-sm hover:text-primary-600 flex items-center gap-1">
              Batafsil o'qish
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/></svg>
            </NuxtLink>
          </div>
        </article>
        
        <!-- Skeleton Loading if no data yet -->
        <div v-if="pending" v-for="i in 3" :key="'skeleton-'+i" class="news-card bg-surface border border-slate-100 animate-pulse">
          <div class="h-56 bg-slate-200"></div>
          <div class="p-6">
            <div class="h-4 bg-slate-200 w-24 mb-4 rounded"></div>
            <div class="h-6 bg-slate-200 w-full mb-2 rounded"></div>
            <div class="h-6 bg-slate-200 w-2/3 mb-4 rounded"></div>
            <div class="h-4 bg-slate-200 w-full mb-2 rounded"></div>
            <div class="h-4 bg-slate-200 w-full mb-2 rounded"></div>
            <div class="h-4 bg-slate-200 w-3/4 mb-5 rounded"></div>
            <div class="h-5 bg-slate-200 w-32 rounded"></div>
          </div>
        </div>
      </div>

      <div class="mt-10 text-center sm:hidden">
        <NuxtLink to="/news" class="btn-outline inline-block">
          Barcha yangiliklarni ko'rish
        </NuxtLink>
      </div>
    </div>
  </section>
</template>

<script setup>
import { useRuntimeConfig, useFetch, computed } from '#imports'

const config = useRuntimeConfig()

// 3 ta eng so'nggi yangilikni olish
const { data, pending } = await useFetch(`${config.public.apiBase}/news/`)

// Agar API response da count/results bo'lsa, data.value.results dan oladi
const newsItems = computed(() => {
  if (!data.value) return []
  const items = data.value.results || data.value
  return items.slice(0, 3) // Faqat 3 tasini olish
})
</script>
