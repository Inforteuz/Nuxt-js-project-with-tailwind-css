<template>
  <div class="pt-24 pb-20 bg-slate-50 min-h-screen">
    <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">

      <NuxtLink to="/news" class="inline-flex items-center gap-2 text-slate-500 hover:text-primary-600 transition-colors mb-8 font-medium">
        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18"/></svg>
        Barcha yangiliklarga qaytish
      </NuxtLink>

      <div v-if="pending" class="flex justify-center items-center py-20">
        <div class="w-12 h-12 border-4 border-primary-200 border-t-primary-600 rounded-full animate-spin"></div>
      </div>

      <div v-else-if="error" class="text-center py-20 text-red-500 bg-red-50 rounded-2xl">
        Yangilik topilmadi yoki xatolik yuz berdi.
      </div>

      <article v-else-if="news" class="bg-white rounded-3xl shadow-sm border border-slate-100 overflow-hidden">
        <div class="relative h-64 md:h-96 w-full bg-slate-100">
          <img :src="news.image || '/images/team.png'" :alt="t(news, 'title')" class="w-full h-full object-cover" />
          <div class="absolute top-6 left-6 bg-white/90 backdrop-blur text-primary-600 text-sm font-bold px-4 py-2 rounded-xl shadow-sm">
            {{ new Date(news.published_at || news.created_at).toLocaleDateString('uz-UZ', { day: '2-digit', month: 'long', year: 'numeric' }) }}
          </div>
        </div>

        <div class="p-8 md:p-12">
          <div class="flex flex-wrap items-center gap-4 text-sm font-medium text-slate-500 mb-6 uppercase tracking-wider">
            <span class="text-secondary-600 bg-secondary-50 px-3 py-1 rounded-full">{{ t(news.category, 'name') || 'Yangilik' }}</span>
            <span v-if="news.views_count" class="flex items-center gap-1.5 ml-auto">
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"/><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"/></svg>
              {{ news.views_count }} marta ko'rildi
            </span>
          </div>

          <h1 class="text-2xl md:text-4xl font-bold text-dark mb-8 leading-tight font-heading">
            {{ t(news, 'title') }}
          </h1>

          <div class="prose prose-lg max-w-none text-slate-600 whitespace-pre-line leading-relaxed">
            {{ t(news, 'content') }}
          </div>

          <div class="mt-12 pt-8 border-t border-slate-100 flex items-center gap-4">
            <span class="text-slate-500 font-medium">Ulashish:</span>
            <button @click="shareToFacebook" class="w-10 h-10 rounded-full bg-blue-50 text-blue-600 hover:bg-blue-600 hover:text-white flex items-center justify-center transition-colors">
              <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24"><path d="M24 12.073c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.99 4.388 10.954 10.125 11.854v-8.385H7.078v-3.47h3.047V9.43c0-3.007 1.792-4.669 4.533-4.669 1.312 0 2.686.235 2.686.235v2.953H15.83c-1.491 0-1.956.925-1.956 1.874v2.25h3.328l-.532 3.47h-2.796v8.385C19.612 23.027 24 18.062 24 12.073z"/></svg>
            </button>
            <button @click="shareToTelegram" class="w-10 h-10 rounded-full bg-sky-50 text-sky-600 hover:bg-sky-600 hover:text-white flex items-center justify-center transition-colors">
              <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24"><path d="M11.944 0A12 12 0 0 0 0 12a12 12 0 0 0 12 12 12 12 0 0 0 12-12A12 12 0 0 0 12 0a12 12 0 0 0-.056 0zm4.962 7.224c.1-.002.321.023.465.14a.506.506 0 0 1 .171.325c.016.093.036.306.02.472-.18 1.898-.962 6.502-1.36 8.627-.168.9-.499 1.201-.82 1.23-.696.065-1.225-.46-1.9-.902-1.056-.693-1.653-1.124-2.678-1.8-1.185-.78-.417-1.21.258-1.91.177-.184 3.247-2.977 3.307-3.23.007-.032.014-.15-.056-.212s-.174-.041-.249-.024c-.106.024-1.793 1.14-5.061 3.345-.48.33-.913.49-1.302.48-.428-.008-1.252-.241-1.865-.44-.752-.245-1.349-.374-1.297-.789.027-.216.325-.437.893-.663 3.498-1.524 5.83-2.529 6.998-3.014 3.332-1.386 4.025-1.627 4.476-1.635z"/></svg>
            </button>
          </div>
        </div>
      </article>

    </div>
  </div>
</template>

<script setup>
import { useRoute, useRuntimeConfig, useFetch, watchEffect } from '#imports'

const route = useRoute()
const config = useRuntimeConfig()
const { t } = useLanguage()

const newsId = route.params.id
const { data: news, pending, error } = await useFetch(`${config.public.apiBase}/news/${newsId}/`)

watchEffect(() => {
  useHead({
    title: news.value ? `${t(news.value, 'title')} - Andijon SSB` : 'Yangilik - Andijon SSB',
  })
})

function shareToFacebook() {
  window.open(`https://www.facebook.com/sharer/sharer.php?u=${encodeURIComponent(window.location.href)}`, '_blank')
}
function shareToTelegram() {
  window.open(`https://t.me/share/url?url=${encodeURIComponent(window.location.href)}&text=${encodeURIComponent(t(news.value, 'title') || '')}`, '_blank')
}
</script>
