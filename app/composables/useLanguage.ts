import { useState } from '#app'

export const useLanguage = () => {
  const currentLang = useState('language', () => 'uz') // 'uz' or 'ru'

  const setLanguage = (lang: string) => {
    currentLang.value = lang
    if (process.client) {
      localStorage.setItem('selected_lang', lang)
    }
  }

  const t = (obj: any, field: string) => {
    if (!obj) return ''
    const langSuffix = currentLang.value === 'ru' ? '_ru' : '_uz'
    return obj[field + langSuffix] || obj[field + '_uz'] || obj[field] || ''
  }

  return {
    currentLang,
    setLanguage,
    t
  }
}
