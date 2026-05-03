<template>
  <div class="page-loader" :class="{ loaded: isLoaded }">
    <div class="loader-content">
      <div class="loader-icon">
        <div class="loader-pulse"></div>
        <div class="loader-pulse"></div>
        <div class="loader-pulse"></div>
        <svg class="loader-cross" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
          <path d="M9 2h6v7h7v6h-7v7H9v-7H2V9h7V2z"/>
        </svg>
      </div>
      <p class="loader-text">{{ loadingText }}</p>
      <div class="loader-bar">
        <div class="loader-bar-inner"></div>
      </div>
    </div>
  </div>
</template>

<script setup>
const { currentLang } = useLanguage()
const isLoaded = ref(false)

const loadingText = computed(() => {
  if (currentLang.value === 'ru') return 'Загрузка'
  if (currentLang.value === 'uz_kr') return 'Юкланмоқда'
  return 'Yuklanmoqda'
})

onMounted(() => {
  setTimeout(() => { isLoaded.value = true }, 2000)
})
</script>
