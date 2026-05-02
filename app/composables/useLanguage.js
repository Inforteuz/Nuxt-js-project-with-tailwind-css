export const useLanguage = () => {
  const currentLang = useState('language', () => 'uz_lot')

  if (process.client) {
    const saved = localStorage.getItem('selected_lang')
    if (saved) currentLang.value = saved
  }

  const setLanguage = (lang) => {
    currentLang.value = lang
    if (process.client) {
      localStorage.setItem('selected_lang', lang)
    }
  }

  const t = (obj, field) => {
    if (!obj) return ''
    const lang = currentLang.value
    if (lang === 'ru') {
      return obj[field + '_ru'] || obj[field + '_uz'] || obj[field] || ''
    }
    if (lang === 'uz_kr') {
      return obj[field + '_kr'] || obj[field + '_uz'] || obj[field] || ''
    }
    // uz_lot (default)
    return obj[field + '_uz'] || obj[field] || ''
  }

  return { currentLang, setLanguage, t }
}
