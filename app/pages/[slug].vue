<template>
  <div class="pt-24 pb-20 bg-slate-50 min-h-screen">

    <!-- Loading -->
    <div v-if="pending" class="flex justify-center items-center min-h-[60vh]">
      <div class="text-center">
        <div class="w-12 h-12 border-4 border-primary-200 border-t-primary-600 rounded-full animate-spin mx-auto mb-4"></div>
        <p class="text-slate-400 text-sm">{{ loadingText }}</p>
      </div>
    </div>

    <!-- 404 -->
    <div v-else-if="!page" class="max-w-2xl mx-auto px-4 text-center py-20">
      <div class="w-20 h-20 bg-slate-100 rounded-full flex items-center justify-center mx-auto mb-6">
        <svg class="w-10 h-10 text-slate-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
            d="M9.172 16.172a4 4 0 015.656 0M9 10h.01M15 10h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/>
        </svg>
      </div>
      <h1 class="text-3xl font-heading font-bold text-dark mb-3">404</h1>
      <p class="text-slate-500 mb-8">{{ notFoundText }}</p>
      <NuxtLink to="/" class="inline-flex items-center gap-2 bg-primary-600 text-white px-6 py-3 rounded-xl font-medium hover:bg-primary-700 transition-colors">
        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6"/>
        </svg>
        {{ homeText }}
      </NuxtLink>
    </div>

    <!-- Page content -->
    <div v-else>
      <!-- Page header -->
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 mb-10">
        <NuxtLink to="/"
          class="inline-flex items-center gap-2 text-slate-500 hover:text-primary-600 transition-colors mb-6 font-medium">
          <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18"/>
          </svg>
          {{ backText }}
        </NuxtLink>

        <h1 class="text-3xl md:text-4xl font-heading font-bold text-dark">
          {{ t(page, 'title') }}
        </h1>
        <div class="mt-3 w-16 h-1 bg-primary-500 rounded-full"></div>
      </div>

      <!-- Blocks -->
      <div class="space-y-0">
        <template v-for="block in activeBlocks" :key="block.id">

          <!-- Divider -->
          <div v-if="block.block_type === 'divider'" class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-4">
            <hr class="border-slate-200">
          </div>

          <!-- Text block -->
          <section v-else-if="block.block_type === 'text'"
            class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-10">
            <h2 v-if="t(block, 'title')" class="text-2xl font-heading font-bold text-dark mb-5">
              {{ t(block, 'title') }}
            </h2>
            <div v-if="t(block, 'content')"
              class="prose prose-slate max-w-none text-slate-600 leading-relaxed"
              v-html="t(block, 'content')">
            </div>
            <div v-if="block.link_url && t(block, 'link_text')" class="mt-6">
              <component
                :is="block.link_url.startsWith('http') ? 'a' : 'NuxtLink'"
                :href="block.link_url.startsWith('http') ? block.link_url : undefined"
                :to="!block.link_url.startsWith('http') ? block.link_url : undefined"
                :target="block.link_url.startsWith('http') ? '_blank' : undefined"
                class="inline-flex items-center gap-2 bg-primary-600 text-white px-6 py-3 rounded-xl font-medium hover:bg-primary-700 transition-colors">
                {{ t(block, 'link_text') }}
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3"/>
                </svg>
              </component>
            </div>
          </section>

          <!-- Image + Text block -->
          <section v-else-if="block.block_type === 'image_text'"
            class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
            <div class="grid grid-cols-1 lg:grid-cols-2 gap-10 items-center"
              :class="block.image_position === 'left' ? 'lg:grid-flow-dense' : ''">
              <!-- Image -->
              <div :class="block.image_position === 'left' ? 'lg:col-start-1' : 'lg:order-2'">
                <img v-if="block.image" :src="block.image" :alt="t(block, 'title')"
                  class="w-full rounded-2xl shadow-card object-cover max-h-80">
                <div v-else class="w-full h-60 bg-slate-100 rounded-2xl flex items-center justify-center">
                  <svg class="w-16 h-16 text-slate-300" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"
                      d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z"/>
                  </svg>
                </div>
              </div>
              <!-- Text -->
              <div :class="block.image_position === 'left' ? 'lg:col-start-2' : 'lg:order-1'">
                <h2 v-if="t(block, 'title')" class="text-2xl md:text-3xl font-heading font-bold text-dark mb-4">
                  {{ t(block, 'title') }}
                </h2>
                <div v-if="t(block, 'content')"
                  class="text-slate-600 leading-relaxed space-y-3"
                  v-html="t(block, 'content')">
                </div>
                <div v-if="block.link_url && t(block, 'link_text')" class="mt-6">
                  <component
                    :is="block.link_url.startsWith('http') ? 'a' : 'NuxtLink'"
                    :href="block.link_url.startsWith('http') ? block.link_url : undefined"
                    :to="!block.link_url.startsWith('http') ? block.link_url : undefined"
                    :target="block.link_url.startsWith('http') ? '_blank' : undefined"
                    class="inline-flex items-center gap-2 bg-primary-600 text-white px-6 py-3 rounded-xl font-medium hover:bg-primary-700 transition-colors">
                    {{ t(block, 'link_text') }}
                    <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3"/>
                    </svg>
                  </component>
                </div>
              </div>
            </div>
          </section>

          <!-- Cards block -->
          <section v-else-if="block.block_type === 'cards'"
            class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
            <h2 v-if="t(block, 'title')" class="text-2xl md:text-3xl font-heading font-bold text-dark mb-2 text-center">
              {{ t(block, 'title') }}
            </h2>
            <p v-if="t(block, 'content')" class="text-slate-500 text-center mb-10 max-w-2xl mx-auto"
              v-html="t(block, 'content')">
            </p>
            <div v-else-if="t(block, 'title')" class="mb-10"></div>

            <div v-if="block.cards && block.cards.length"
              class="grid gap-6"
              :class="block.cards.length === 1 ? 'grid-cols-1 max-w-md mx-auto' :
                      block.cards.length === 2 ? 'grid-cols-1 sm:grid-cols-2' :
                      block.cards.length <= 4 ? 'grid-cols-1 sm:grid-cols-2 lg:grid-cols-' + block.cards.length :
                      'grid-cols-1 sm:grid-cols-2 lg:grid-cols-3'">
              <div v-for="card in block.cards" :key="card.id"
                class="bg-white rounded-2xl shadow-card border border-slate-100 p-6 hover:shadow-card-hover transition-shadow">
                <!-- Icon or image -->
                <div v-if="card.icon" class="text-4xl mb-4">{{ card.icon }}</div>
                <div v-else-if="card.image" class="mb-4">
                  <img :src="card.image" :alt="t(card, 'title')"
                    class="w-full h-40 object-cover rounded-xl">
                </div>
                <div v-else class="w-12 h-12 bg-primary-50 rounded-xl mb-4 flex items-center justify-center">
                  <svg class="w-6 h-6 text-primary-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                      d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/>
                  </svg>
                </div>
                <h3 class="font-heading font-bold text-dark text-lg mb-2">{{ t(card, 'title') }}</h3>
                <p v-if="t(card, 'text')" class="text-slate-500 text-sm leading-relaxed">{{ t(card, 'text') }}</p>
                <component v-if="card.link"
                  :is="card.link.startsWith('http') ? 'a' : 'NuxtLink'"
                  :href="card.link.startsWith('http') ? card.link : undefined"
                  :to="!card.link.startsWith('http') ? card.link : undefined"
                  :target="card.link.startsWith('http') ? '_blank' : undefined"
                  class="inline-flex items-center gap-1 mt-4 text-primary-600 hover:text-primary-700 font-medium text-sm transition-colors">
                  {{ moreText }}
                  <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3"/>
                  </svg>
                </component>
              </div>
            </div>
            <p v-else class="text-center text-slate-400 py-6">—</p>
          </section>

          <!-- CTA block -->
          <section v-else-if="block.block_type === 'cta'"
            class="bg-gradient-to-r from-primary-600 to-primary-700 py-16">
            <div class="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
              <h2 v-if="t(block, 'title')" class="text-2xl md:text-3xl font-heading font-bold text-white mb-4">
                {{ t(block, 'title') }}
              </h2>
              <p v-if="t(block, 'content')" class="text-primary-100 text-lg mb-8 leading-relaxed"
                v-html="t(block, 'content')">
              </p>
              <component v-if="block.link_url && t(block, 'link_text')"
                :is="block.link_url.startsWith('http') ? 'a' : 'NuxtLink'"
                :href="block.link_url.startsWith('http') ? block.link_url : undefined"
                :to="!block.link_url.startsWith('http') ? block.link_url : undefined"
                :target="block.link_url.startsWith('http') ? '_blank' : undefined"
                class="inline-flex items-center gap-2 bg-white text-primary-700 px-8 py-4 rounded-xl font-bold text-lg hover:bg-primary-50 transition-colors shadow-lg">
                {{ t(block, 'link_text') }}
                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3"/>
                </svg>
              </component>
            </div>
          </section>

        </template>

        <!-- Empty state (no blocks) -->
        <div v-if="!pending && page && activeBlocks.length === 0"
          class="max-w-2xl mx-auto px-4 text-center py-16">
          <p class="text-slate-400">{{ emptyText }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useRuntimeConfig, useFetch, useRoute, useHead } from '#imports'

const config  = useRuntimeConfig()
const route   = useRoute()
const { t, currentLang } = useLanguage()

const slug = route.params.slug

const { data: page, pending } = await useFetch(
  `${config.public.apiBase}/pages/${slug}/`,
  { key: `custom-page-${slug}` }
)

// ── SEO ──────────────────────────────────────────
useHead(() => ({
  title: page.value ? t(page.value, 'title') : slug,
  meta: [
    {
      name: 'description',
      content: page.value?.meta_description_uz || t(page.value, 'title') || '',
    },
  ],
}))

// ── Computed ─────────────────────────────────────
const activeBlocks = computed(() =>
  (page.value?.blocks || []).filter(b => b.is_active)
)

// ── i18n labels ──────────────────────────────────
const loadingText = computed(() => {
  if (currentLang.value === 'ru')    return 'Загрузка...'
  if (currentLang.value === 'uz_kr') return 'Юкланмоқда...'
  return 'Yuklanmoqda...'
})
const notFoundText = computed(() => {
  if (currentLang.value === 'ru')    return 'Страница не найдена'
  if (currentLang.value === 'uz_kr') return 'Саҳифа топилмади'
  return 'Sahifa topilmadi'
})
const homeText = computed(() => {
  if (currentLang.value === 'ru')    return 'На главную'
  if (currentLang.value === 'uz_kr') return 'Бош саҳифага'
  return 'Bosh sahifaga'
})
const backText = computed(() => {
  if (currentLang.value === 'ru')    return 'Вернуться назад'
  if (currentLang.value === 'uz_kr') return 'Орқага қайтиш'
  return 'Orqaga qaytish'
})
const moreText = computed(() => {
  if (currentLang.value === 'ru')    return 'Подробнее'
  if (currentLang.value === 'uz_kr') return 'Батафсил'
  return 'Batafsil'
})
const emptyText = computed(() => {
  if (currentLang.value === 'ru')    return 'Контент ещё не добавлен'
  if (currentLang.value === 'uz_kr') return 'Контент ҳали қўшилмаган'
  return 'Kontent hali qo\'shilmagan'
})
</script>

<style scoped>
/* Allow HTML in v-html blocks to be styled */
:deep(b), :deep(strong) { font-weight: 600; color: #1e293b; }
:deep(i), :deep(em)     { font-style: italic; }
:deep(ul)  { list-style: disc; padding-left: 1.5rem; margin: 0.5rem 0; }
:deep(ol)  { list-style: decimal; padding-left: 1.5rem; margin: 0.5rem 0; }
:deep(li)  { margin: 0.25rem 0; }
:deep(a)   { color: rgb(var(--c-primary-600)); text-decoration: underline; }
:deep(br)  { display: block; content: ''; margin: 0.25rem 0; }
:deep(p)   { margin: 0.5rem 0; }
</style>
