<template>
  <section class="py-20 bg-surface border-t border-slate-100">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="grid lg:grid-cols-2 gap-12 items-center">
        <!-- Content -->
        <div class="scroll-animate-left">
          <h2 class="text-3xl md:text-4xl font-bold font-heading text-dark mb-4">Savol yoki murojaatingiz bormi?</h2>
          <div class="w-20 h-1.5 bg-gradient-to-r from-primary-500 to-secondary-500 rounded-full mb-8"></div>
          
          <p class="text-lg text-slate-600 mb-8 leading-relaxed">
            Bizning mutaxassislarimiz sizning murojaatlaringizga javob berishga va kerakli yordamni ko'rsatishga tayyor. Virtual qabulxona orqali onlayn tarzda murojaat yo'llashingiz mumkin.
          </p>
          
          <div class="space-y-6 mb-10">
            <div class="flex items-center gap-4 bg-white p-4 rounded-xl shadow-sm border border-slate-100 transition-transform hover:-translate-y-1">
              <div class="w-12 h-12 rounded-full bg-primary-50 flex items-center justify-center flex-shrink-0">
                <svg class="w-6 h-6 text-primary-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"/></svg>
              </div>
              <div>
                <p class="text-sm text-slate-500 font-medium">Ishonch telefoni</p>
                <a :href="`tel:${generalInfo?.phone?.replace(/\D/g,'')}`" class="text-lg font-bold text-dark hover:text-primary-500">{{ generalInfo?.phone || '(374) 228-42-84' }}</a>
              </div>
            </div>
            
            <div class="flex items-center gap-4 bg-white p-4 rounded-xl shadow-sm border border-slate-100 transition-transform hover:-translate-y-1">
              <div class="w-12 h-12 rounded-full bg-secondary-50 flex items-center justify-center flex-shrink-0">
                <svg class="w-6 h-6 text-secondary-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"/><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"/></svg>
              </div>
              <div>
                <p class="text-sm text-slate-500 font-medium">Manzil</p>
                <p class="text-base font-semibold text-dark">{{ generalInfo?.address || "Andijon shahar, Amir Umarxon ko'chasi, 19-uy" }}</p>
              </div>
            </div>
          </div>
          
          <NuxtLink to="/contact" class="btn-primary inline-flex items-center gap-2">
            Virtual qabulxonaga o'tish
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"/></svg>
          </NuxtLink>
        </div>
        
        <!-- Image/Map Graphic -->
        <div class="relative h-[400px] lg:h-[500px] rounded-2xl overflow-hidden shadow-2xl scroll-animate-right">
          <img src="/images/building.png" alt="Andijon viloyati SSB binosi" class="w-full h-full object-cover" />
          <div class="absolute inset-0 bg-gradient-to-t from-primary-900/80 via-primary-900/20 to-transparent"></div>
          
          <div class="absolute bottom-0 left-0 right-0 p-8">
            <div class="bg-white/10 backdrop-blur-md border border-white/20 p-6 rounded-xl">
              <h3 class="text-white font-bold text-xl mb-2">Ish vaqti</h3>
              <p v-if="generalInfo?.work_hours" class="text-white whitespace-pre-line">{{ generalInfo.work_hours }}</p>
              <ul v-else class="space-y-2 text-slate-200 text-sm">
                <li class="flex justify-between">
                  <span>Dushanba - Juma:</span>
                  <span class="font-semibold text-white">09:00 - 18:00</span>
                </li>
                <li class="flex justify-between">
                  <span>Tushlik:</span>
                  <span class="font-semibold text-white">13:00 - 14:00</span>
                </li>
                <li class="flex justify-between">
                  <span>Shanba - Yakshanba:</span>
                  <span class="font-semibold text-white">Dam olish kuni</span>
                </li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { useRuntimeConfig, useFetch } from '#imports'

const config = useRuntimeConfig()
const { data: generalInfo } = await useFetch(`${config.public.apiBase}/info/`)
</script>
