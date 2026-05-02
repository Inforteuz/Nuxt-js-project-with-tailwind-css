<template>
  <section class="relative min-h-[90vh] flex items-center pt-24 pb-16 overflow-hidden">
    <!-- Carousel Backgrounds -->
    <div v-for="(slide, index) in slides" :key="index" 
         class="absolute inset-0 z-0 transition-opacity duration-1000 ease-in-out"
         :class="currentSlide === index ? 'opacity-100' : 'opacity-0 pointer-events-none'">
      <img :src="slide.image" :alt="slide.title" class="w-full h-full object-cover transform scale-105" />
      <div class="absolute inset-0 bg-gradient-to-r from-slate-900/95 via-slate-900/80 to-slate-900/40 mix-blend-multiply"></div>
      <div class="absolute inset-0 bg-gradient-to-t from-slate-900 via-transparent to-transparent"></div>
    </div>
    
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10 w-full">
      <div class="grid lg:grid-cols-12 gap-12 lg:gap-8 items-center">
        <!-- Text Content -->
        <div class="lg:col-span-7 text-white">
          <div class="inline-flex items-center gap-2 px-4 py-2 rounded-full bg-white/5 backdrop-blur-md border border-white/10 text-sm font-medium mb-8 shadow-[0_0_15px_rgba(255,255,255,0.05)]">
            <span class="w-2.5 h-2.5 rounded-full bg-secondary-400 animate-pulse"></span>
            Rasmiy veb-sayt
          </div>
          
          <div class="relative min-h-[220px]">
            <transition-group name="slide-fade">
              <div v-for="(slide, index) in slides" :key="'text-'+index" 
                   v-show="currentSlide === index" class="absolute inset-0">
                <h1 class="text-4xl sm:text-5xl lg:text-7xl font-bold font-heading leading-[1.15] mb-6 tracking-tight text-white drop-shadow-lg">
                  {{ t(slide, 'title') }} <br>
                  <span class="text-transparent bg-clip-text bg-gradient-to-r from-secondary-300 via-teal-300 to-primary-300">{{ t(slide, 'subtitle') }}</span>
                </h1>
                
                <p class="text-lg sm:text-xl text-slate-300 mb-10 max-w-2xl leading-relaxed font-light drop-shadow">
                  {{ t(slide, 'description') }}
                </p>
              </div>
            </transition-group>
          </div>
          
          <div class="flex flex-wrap items-center gap-5 mt-8">
            <NuxtLink to="/contact" class="px-8 py-4 bg-gradient-to-r from-secondary-500 to-teal-500 hover:from-secondary-400 hover:to-teal-400 text-white rounded-xl font-bold transition-all shadow-[0_0_30px_rgba(20,184,166,0.3)] hover:shadow-[0_0_40px_rgba(20,184,166,0.5)] hover:-translate-y-1 flex items-center gap-2">
              Onlayn murojaat
              <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"/></svg>
            </NuxtLink>
            <NuxtLink to="/about" class="px-8 py-4 bg-white/5 hover:bg-white/10 text-white border border-white/20 rounded-xl font-semibold transition-all backdrop-blur flex items-center gap-2 group hover:-translate-y-1">
              Batafsil ma'lumot
            </NuxtLink>
          </div>

          <!-- Carousel Controls -->
          <div class="flex items-center gap-4 mt-12">
            <button @click="prevSlide" class="w-12 h-12 rounded-full border border-white/20 bg-white/5 hover:bg-white/20 flex items-center justify-center transition-colors backdrop-blur">
              <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7"/></svg>
            </button>
            <div class="flex items-center gap-2">
              <button v-for="(_, index) in slides" :key="'dot-'+index" 
                      @click="setSlide(index)"
                      class="h-2 rounded-full transition-all duration-300"
                      :class="currentSlide === index ? 'w-8 bg-secondary-400' : 'w-2 bg-white/30 hover:bg-white/50'">
              </button>
            </div>
            <button @click="nextSlide" class="w-12 h-12 rounded-full border border-white/20 bg-white/5 hover:bg-white/20 flex items-center justify-center transition-colors backdrop-blur">
              <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/></svg>
            </button>
          </div>
        </div>
        
        <!-- Interactive Glass Cards -->
        <div class="lg:col-span-5 relative scroll-animate-right hidden lg:block">
          <!-- Decorative glow -->
          <div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-72 h-72 bg-secondary-500/20 rounded-full blur-[80px] animate-pulse-slow"></div>
          
          <div class="flex flex-col gap-6 relative z-10 lg:pl-10">
            <!-- Card 1 -->
            <div class="glass-dark rounded-3xl p-7 border border-white/10 shadow-[0_20px_50px_rgba(0,0,0,0.3)] backdrop-blur-xl transform hover:scale-[1.02] hover:-translate-y-1 transition-all duration-300 w-full bg-slate-900/40 relative overflow-hidden group">
              <div class="absolute top-0 right-0 w-32 h-32 bg-secondary-500/20 rounded-bl-full blur-2xl group-hover:bg-secondary-500/30 transition-colors"></div>
              <div class="flex justify-between items-start mb-5 relative z-10">
                <div class="flex items-center gap-4">
                  <div class="w-14 h-14 bg-gradient-to-br from-secondary-500 to-teal-600 rounded-2xl flex items-center justify-center shadow-inner">
                    <svg class="w-7 h-7 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"/></svg>
                  </div>
                  <div>
                    <h3 class="text-white font-bold text-lg">Ishonch telefoni</h3>
                    <p class="text-sm text-secondary-300 font-medium">Tezkor aloqa xizmati</p>
                  </div>
                </div>
              </div>
              <a href="tel:1003" class="text-5xl font-black font-heading text-white tracking-tight hover:text-secondary-400 transition-colors block mb-4 relative z-10">1003</a>
              <div class="flex justify-between items-center text-sm border-t border-white/10 pt-5 relative z-10">
                <span class="text-slate-400">Ish vaqti:</span>
                <span class="text-secondary-400 font-bold px-3 py-1.5 bg-secondary-500/20 rounded-lg">24/7 rejimida</span>
              </div>
            </div>
            
            <!-- Card 2 -->
            <div class="glass-dark rounded-3xl p-7 border border-white/10 shadow-[0_20px_50px_rgba(0,0,0,0.3)] backdrop-blur-xl transform hover:scale-[1.02] hover:-translate-y-1 transition-all duration-300 w-full lg:-ml-12 bg-slate-900/50 relative overflow-hidden group">
               <div class="absolute -left-4 -bottom-4 w-32 h-32 bg-primary-500/20 rounded-tr-full blur-2xl group-hover:bg-primary-500/30 transition-colors"></div>
              <div class="flex items-center gap-4 mb-5 relative z-10">
                <div class="w-14 h-14 bg-white/5 border border-white/10 rounded-2xl flex items-center justify-center">
                  <svg class="w-7 h-7 text-primary-300" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4"/></svg>
                </div>
                <div>
                  <h3 class="text-white font-bold text-lg">Boshqarma qabuli</h3>
                  <p class="text-sm text-slate-400">Umumiy masalalar uchun</p>
                </div>
              </div>
              <a href="tel:+9983742284284" class="text-3xl font-bold font-heading text-white hover:text-primary-300 transition-colors block relative z-10">(374) 228-42-84</a>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref, onMounted, onUnmounted, computed } from 'vue'
import { useRuntimeConfig, useFetch } from '#imports'

const config = useRuntimeConfig()
const { t, currentLang } = useLanguage()

const { data: bannerData, pending } = await useFetch(`${config.public.apiBase}/banners/`)

const currentSlide = ref(0)
const slides = computed(() => {
  if (bannerData.value && bannerData.value.length > 0) {
    return bannerData.value
  }
  // Fallback slides
  return [
    {
      image: '/images/hero-bg.png',
      title_uz: "Sog'ligingiz —",
      title_ru: "Ваше здоровье —",
      subtitle_uz: "bizning e'tiborimizda",
      subtitle_ru: "в нашем внимании",
      description_uz: "Andijon viloyati sog'liqni saqlash boshqarmasi aholiga sifatli, tezkor va zamonaviy tibbiy xizmatlarni taqdim etish uchun xizmat qiladi.",
      description_ru: "Управление здравоохранения Андижанской области служит для предоставления населению качественных, оперативных и современных медицинских услуг."
    },
    {
      image: '/images/equipment.png',
      title_uz: "Zamonaviy —",
      title_ru: "Современное —",
      subtitle_uz: "tibbiy uskunalar",
      subtitle_ru: "медицинское оборудование",
      description_uz: "Viloyatimizdagi shifoxonalar eng so'nggi rusumdagi tibbiy jihozlar va texnologiyalar bilan ta'minlanmoqda.",
      description_ru: "Больницы нашей области оснащаются самым современным медицинским оборудованием и технологиями."
    }
  ]
})

let timer
onMounted(() => {
  timer = setInterval(() => {
    nextSlide()
  }, 6000)
})

onUnmounted(() => {
  clearInterval(timer)
})

function nextSlide() {
  if (slides.value.length > 0) {
    currentSlide.value = (currentSlide.value + 1) % slides.value.length
  }
}

function prevSlide() {
  if (slides.value.length > 0) {
    currentSlide.value = (currentSlide.value - 1 + slides.value.length) % slides.value.length
  }
}

function setSlide(index) {
  currentSlide.value = index
}
</script>

<style scoped>
.slide-fade-enter-active,
.slide-fade-leave-active {
  transition: all 0.5s ease-out;
}

.slide-fade-enter-from {
  opacity: 0;
  transform: translateX(30px);
}

.slide-fade-leave-to {
  opacity: 0;
  transform: translateX(-30px);
}
</style>
