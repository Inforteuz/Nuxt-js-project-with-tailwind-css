export const useLanguage = () => {
  const currentLang = useState('language', () => 'uz_lot')

  // Sync from localStorage ONLY after mount to prevent SSR/CSR hydration mismatch.
  // On the server, currentLang stays 'uz_lot' (default).
  // On the client, onMounted updates it to the user's saved preference.
  onMounted(() => {
    const saved = localStorage.getItem('selected_lang')
    if (saved && saved !== currentLang.value) {
      currentLang.value = saved
    }
  })

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
