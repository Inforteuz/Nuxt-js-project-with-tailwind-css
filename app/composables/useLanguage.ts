import { useState } from '#app'

export const useLanguage = () => {
  const currentLang = useState('language', () => 'uz_lot') // 'uz_lot', 'uz_kr', 'ru'

  const setLanguage = (lang: string) => {
    currentLang.value = lang
    if (process.client) {
      localStorage.setItem('selected_lang', lang)
    }
  }

  const t = (obj: any, field: string) => {
    if (!obj) return ''
    
    let suffix = '_uz'
    if (currentLang.value === 'ru') suffix = '_ru'
    else if (currentLang.value === 'uz_kr') suffix = '_kr' // Assuming suffix _kr for Krill
    
    // Check for specific suffix, then fallback to _uz
    return obj[field + suffix] || obj[field + '_uz'] || obj[field] || ''
  }

  return {
    currentLang,
    setLanguage,
    t
  }
}
