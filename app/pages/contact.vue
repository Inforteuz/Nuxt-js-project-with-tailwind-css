<template>
  <div class="pt-24 pb-20 bg-slate-50 min-h-screen">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <div class="text-center mb-16">
        <div class="w-16 h-16 bg-primary-50 text-primary-600 rounded-2xl flex items-center justify-center mx-auto mb-6">
          <svg class="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"/></svg>
        </div>
        <h1 class="text-3xl md:text-4xl font-heading font-bold text-dark mb-4">Biz bilan bog'lanish</h1>
        <div class="w-20 h-1.5 bg-gradient-to-r from-primary-500 to-secondary-500 rounded-full mx-auto mb-6"></div>
        <p class="text-slate-600 max-w-2xl mx-auto">
          Sizda savollar, takliflar yoki e'tirozlar bormi? Biz bilan bog'laning yoki onlayn murojaat qoldiring. Biz sizga albatta javob beramiz.
        </p>
      </div>

      <div class="flex flex-col lg:flex-row gap-10 max-w-6xl mx-auto justify-center">
        
        <!-- Aloqa ma'lumotlari -->
        <div class="w-full lg:w-80 flex-shrink-0">
          <div v-if="pendingInfo" class="animate-pulse bg-white p-8 rounded-3xl h-64 border border-slate-100"></div>
          
          <div v-else class="bg-white rounded-3xl shadow-sm border border-slate-100 p-8 space-y-8 h-full">
            <h3 class="text-xl font-bold font-heading text-dark mb-6">Aloqa ma'lumotlari</h3>
            
            <div class="flex items-start gap-4">
              <div class="w-10 h-10 bg-primary-50 text-primary-600 rounded-xl flex items-center justify-center flex-shrink-0">
                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"/><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"/></svg>
              </div>
              <div>
                <p class="text-xs text-slate-500 font-medium mb-1">Manzil</p>
                <p class="text-sm text-slate-800 font-medium leading-snug">{{ generalInfo?.address || "Andijon shahar, Amir Umarxon ko'chasi, 19-uy" }}</p>
              </div>
            </div>

            <div class="flex items-start gap-4">
              <div class="w-10 h-10 bg-secondary-50 text-secondary-600 rounded-xl flex items-center justify-center flex-shrink-0">
                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"/></svg>
              </div>
              <div>
                <p class="text-xs text-slate-500 font-medium mb-1">Telefon</p>
                <a :href="`tel:${(generalInfo?.phone || '+9983742284284').replace(/\D/g,'')}`" class="text-sm text-slate-800 font-medium hover:text-primary-600 transition-colors">{{ generalInfo?.phone || "(374) 228-42-84" }}</a>
              </div>
            </div>

            <div class="flex items-start gap-4">
              <div class="w-10 h-10 bg-teal-50 text-teal-600 rounded-xl flex items-center justify-center flex-shrink-0">
                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"/></svg>
              </div>
              <div>
                <p class="text-xs text-slate-500 font-medium mb-1">Elektron pochta</p>
                <a :href="`mailto:${generalInfo?.email || 'andijon.vssb@ssv.uz'}`" class="text-sm text-slate-800 font-medium hover:text-primary-600 transition-colors">{{ generalInfo?.email || "andijon.vssb@ssv.uz" }}</a>
              </div>
            </div>
            
            <div class="flex items-start gap-4 pt-4 border-t border-slate-100">
              <div class="w-10 h-10 bg-amber-50 text-amber-600 rounded-xl flex items-center justify-center flex-shrink-0">
                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
              </div>
              <div>
                <p class="text-xs text-slate-500 font-medium mb-1">Ish vaqti</p>
                <p class="text-sm text-slate-800 font-medium leading-snug whitespace-pre-line">{{ generalInfo?.work_hours || "Dushanba - Juma: 09:00 - 18:00\nTushlik: 13:00 - 14:00" }}</p>
              </div>
            </div>

          </div>
        </div>

        <!-- Murojaat formasi -->
        <div class="w-full lg:max-w-2xl">
          <div class="bg-white rounded-3xl shadow-sm border border-slate-100 p-8 md:p-10">
            <h3 class="text-2xl font-bold font-heading text-dark mb-6">Onlayn murojaat yo'llash</h3>
            
            <form @submit.prevent="submitForm" class="space-y-6">
              
              <div class="grid md:grid-cols-2 gap-6">
                <div class="space-y-2">
                  <label for="first_name" class="block text-sm font-medium text-slate-700">Ismingiz <span class="text-red-500">*</span></label>
                  <input type="text" id="first_name" v-model="form.first_name" required placeholder="Ismingizni kiriting" class="w-full px-4 py-3 rounded-xl border border-slate-200 focus:border-primary-500 focus:ring-2 focus:ring-primary-500/20 outline-none transition-all bg-slate-50 focus:bg-white" />
                </div>
                
                <div class="space-y-2">
                  <label for="last_name" class="block text-sm font-medium text-slate-700">Familiyangiz <span class="text-red-500">*</span></label>
                  <input type="text" id="last_name" v-model="form.last_name" required placeholder="Familiyangizni kiriting" class="w-full px-4 py-3 rounded-xl border border-slate-200 focus:border-primary-500 focus:ring-2 focus:ring-primary-500/20 outline-none transition-all bg-slate-50 focus:bg-white" />
                </div>
              </div>

              <div class="grid md:grid-cols-2 gap-6">
                <div class="space-y-2">
                  <label for="phone" class="block text-sm font-medium text-slate-700">Telefon raqamingiz <span class="text-red-500">*</span></label>
                  <input type="tel" id="phone" v-model="form.phone" required placeholder="+998" class="w-full px-4 py-3 rounded-xl border border-slate-200 focus:border-primary-500 focus:ring-2 focus:ring-primary-500/20 outline-none transition-all bg-slate-50 focus:bg-white" />
                </div>
                
                <div class="space-y-2">
                  <label for="region" class="block text-sm font-medium text-slate-700">Hududingiz (Tuman/Shahar) <span class="text-red-500">*</span></label>
                  <input type="text" id="region" v-model="form.region" required placeholder="Yashash manzilingizni kiriting" class="w-full px-4 py-3 rounded-xl border border-slate-200 focus:border-primary-500 focus:ring-2 focus:ring-primary-500/20 outline-none transition-all bg-slate-50 focus:bg-white" />
                </div>
              </div>

              <div class="space-y-2">
                <label for="subject" class="block text-sm font-medium text-slate-700">Murojaat mavzusi <span class="text-red-500">*</span></label>
                <input type="text" id="subject" v-model="form.subject" required placeholder="Murojaatingiz nima haqida?" class="w-full px-4 py-3 rounded-xl border border-slate-200 focus:border-primary-500 focus:ring-2 focus:ring-primary-500/20 outline-none transition-all bg-slate-50 focus:bg-white" />
              </div>

              <div class="space-y-2">
                <label for="message" class="block text-sm font-medium text-slate-700">Murojaat matni <span class="text-red-500">*</span></label>
                <textarea id="message" v-model="form.message" required rows="5" placeholder="Murojaatingizni batafsil yozing..." class="w-full px-4 py-3 rounded-xl border border-slate-200 focus:border-primary-500 focus:ring-2 focus:ring-primary-500/20 outline-none transition-all bg-slate-50 focus:bg-white resize-none"></textarea>
              </div>

              <div v-if="submitMessage" :class="`p-4 rounded-xl text-sm font-medium ${submitStatus === 'success' ? 'bg-emerald-50 text-emerald-700 border border-emerald-200' : 'bg-red-50 text-red-700 border border-red-200'}`">
                {{ submitMessage }}
              </div>

              <button type="submit" :disabled="isSubmitting" class="w-full btn-primary py-4 text-lg justify-center relative overflow-hidden group disabled:opacity-70 disabled:cursor-not-allowed">
                <span class="relative z-10 flex items-center gap-2">
                  <span v-if="isSubmitting" class="w-5 h-5 border-2 border-white/30 border-t-white rounded-full animate-spin"></span>
                  {{ isSubmitting ? "Yuborilmoqda..." : "Murojaatni yuborish" }}
                  <svg v-if="!isSubmitting" class="w-5 h-5 transform group-hover:translate-x-1 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"/></svg>
                </span>
              </button>
            </form>
          </div>
        </div>

      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRuntimeConfig, useFetch } from '#imports'

useHead({ title: "Bog'lanish - Andijon SSB" })

const config = useRuntimeConfig()
const { data: generalInfo, pending: pendingInfo } = await useFetch(`${config.public.apiBase}/info/`)

const isSubmitting = ref(false)
const submitStatus = ref(null) // 'success' yoki 'error'
const submitMessage = ref('')

const form = ref({
  first_name: '',
  last_name: '',
  phone: '',
  region: '',
  subject: '',
  message: ''
})

async function submitForm() {
  if (isSubmitting.value) return
  
  isSubmitting.value = true
  submitStatus.value = null
  submitMessage.value = ''
  
  try {
    const response = await $fetch(`${config.public.apiBase}/contact/`, {
      method: 'POST',
      body: form.value
    })
    
    submitStatus.value = 'success'
    submitMessage.value = 'Murojaatingiz muvaffaqiyatli yuborildi! Tez orada siz bilan bog\'lanamiz.'
    
    // Formani tozalash
    form.value = {
      first_name: '',
      last_name: '',
      phone: '',
      region: '',
      subject: '',
      message: ''
    }
    
    setTimeout(() => {
      submitMessage.value = ''
    }, 5000)
    
  } catch (error) {
    submitStatus.value = 'error'
    submitMessage.value = 'Murojaatni yuborishda xatolik yuz berdi. Iltimos, ma\'lumotlarni tekshirib qaytadan urinib ko\'ring.'
  } finally {
    isSubmitting.value = false
  }
}
</script>
