from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponse

GUIDE_HTML = """<!DOCTYPE html>
<html lang="uz">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Admin Qo'llanma — Andijon SSB</title>
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body { font-family: 'Segoe UI', Arial, sans-serif; background: #f4f6f9; color: #333; }
  .topbar {
    background: #343a40; color: #fff; padding: 14px 28px;
    display: flex; align-items: center; gap: 16px; font-size: 16px;
  }
  .topbar a { color: #adb5bd; text-decoration: none; font-size: 13px; }
  .topbar a:hover { color: #fff; }
  .container { max-width: 1100px; margin: 30px auto; padding: 0 20px 60px; }
  h1 { font-size: 26px; color: #1a1a2e; margin-bottom: 6px; }
  .subtitle { color: #666; font-size: 14px; margin-bottom: 30px; }
  .grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(320px, 1fr)); gap: 20px; }
  .card {
    background: #fff; border-radius: 12px; padding: 20px 22px;
    border: 1px solid #e5e7eb; box-shadow: 0 1px 4px rgba(0,0,0,.06);
    transition: box-shadow .2s;
  }
  .card:hover { box-shadow: 0 4px 16px rgba(0,0,0,.1); }
  .card-header {
    display: flex; align-items: center; gap: 12px; margin-bottom: 12px;
    padding-bottom: 12px; border-bottom: 1px solid #f3f4f6;
  }
  .icon {
    width: 44px; height: 44px; border-radius: 10px;
    display: flex; align-items: center; justify-content: center;
    font-size: 20px; flex-shrink: 0;
  }
  .card-title { font-size: 15px; font-weight: 700; color: #1a1a2e; }
  .card-link { font-size: 12px; color: #6b7280; margin-top: 2px; }
  .card-link a { color: #3b82f6; text-decoration: none; }
  .card-link a:hover { text-decoration: underline; }
  .affects { margin-top: 10px; }
  .affects-title { font-size: 11px; font-weight: 700; text-transform: uppercase;
    letter-spacing: .5px; color: #9ca3af; margin-bottom: 6px; }
  .tag {
    display: inline-block; background: #eff6ff; color: #1d4ed8;
    border: 1px solid #bfdbfe; border-radius: 20px;
    font-size: 11px; padding: 2px 10px; margin: 2px 3px 2px 0;
  }
  .tag.green { background: #f0fdf4; color: #15803d; border-color: #bbf7d0; }
  .tag.yellow { background: #fffbeb; color: #92400e; border-color: #fde68a; }
  .tag.red { background: #fef2f2; color: #991b1b; border-color: #fecaca; }
  .tag.purple { background: #faf5ff; color: #7e22ce; border-color: #e9d5ff; }
  .steps { margin-top: 10px; padding-left: 0; list-style: none; }
  .steps li { font-size: 13px; color: #4b5563; padding: 3px 0 3px 18px; position: relative; line-height: 1.5; }
  .steps li::before { content: "→"; position: absolute; left: 0; color: #9ca3af; }
  .section-divider {
    margin: 32px 0 16px; font-size: 13px; font-weight: 700;
    text-transform: uppercase; letter-spacing: 1px; color: #9ca3af;
    display: flex; align-items: center; gap: 10px;
  }
  .section-divider::after { content: ""; flex: 1; height: 1px; background: #e5e7eb; }
  .color-demo {
    display: flex; gap: 8px; margin-top: 10px; flex-wrap: wrap;
  }
  .color-swatch {
    display: flex; align-items: center; gap: 6px; font-size: 12px; color: #555;
  }
  .swatch {
    width: 28px; height: 28px; border-radius: 6px; border: 2px solid #ddd;
  }
  .tip {
    background: #fffbeb; border: 1px solid #fde68a; border-radius: 8px;
    padding: 12px 16px; margin-top: 24px; font-size: 13px; line-height: 1.7;
  }
  .tip b { color: #92400e; }
</style>
</head>
<body>

<div class="topbar">
  <span>🏛️ <b>Andijon SSB</b> — Boshqaruv paneli</span>
  <span style="flex:1"></span>
  <a href="/admin/">← Admin panelga qaytish</a>
</div>

<div class="container">
  <h1>📖 Admin panel qo'llanmasi</h1>
  <p class="subtitle">Qaysi bo'lim saytning qayeriga ta'sir qilishi haqida to'liq ma'lumot</p>

  <!-- RANG VA KO'RINISH -->
  <div class="section-divider">🎨 Rang va ko'rinish</div>
  <div class="grid">

    <div class="card">
      <div class="card-header">
        <div class="icon" style="background:#fef3c7;">🎨</div>
        <div>
          <div class="card-title">Sayt sozlamalari</div>
          <div class="card-link"><a href="/admin/core/sitesettings/">Tahrirlash →</a></div>
        </div>
      </div>
      <div class="affects">
        <div class="affects-title">Saytda nima o'zgaradi</div>
        <span class="tag yellow">Navbar rangi</span>
        <span class="tag yellow">Tugmalar rangi</span>
        <span class="tag yellow">Sarlavhalar</span>
        <span class="tag yellow">Logotip</span>
        <span class="tag yellow">Favicon</span>
      </div>
      <ul class="steps">
        <li>«Asosiy rang» — navbar, tugmalar va barcha asosiy elementlar rangi</li>
        <li>«Ikkinchi rang» — kategoriya teglari va hover effektlar</li>
        <li>«Aksent rang» — e'lon va muhim belgilar rangi</li>
        <li>Rang tanlash uchun rangli kvadratni bosing → palitra ochiladi</li>
        <li>Logotip PNG/SVG formatida yuklang (240×60 px tavsiya)</li>
      </ul>
      <div class="color-demo">
        <div class="color-swatch">
          <div class="swatch" style="background:#0ea5e9;"></div>
          <span>Asosiy (ko'k)</span>
        </div>
        <div class="color-swatch">
          <div class="swatch" style="background:#14b8a6;"></div>
          <span>Ikkinchi (yashil)</span>
        </div>
        <div class="color-swatch">
          <div class="swatch" style="background:#f59e0b;"></div>
          <span>Aksent (sariq)</span>
        </div>
      </div>
    </div>

    <div class="card">
      <div class="card-header">
        <div class="icon" style="background:#fce7f3;">🖼️</div>
        <div>
          <div class="card-title">Sayt rasmlari</div>
          <div class="card-link"><a href="/admin/core/mediaasset/">Tahrirlash →</a></div>
        </div>
      </div>
      <div class="affects">
        <div class="affects-title">Saytda nima o'zgaradi</div>
        <span class="tag red">Bosh sahifa fon rasmi</span>
        <span class="tag red">«Biz haqimizda» rasmi</span>
        <span class="tag red">Aloqa sahifasi rasmi</span>
      </div>
      <ul class="steps">
        <li>«Joylashuv»ni tanlang: qaysi sahifaga mos rasm ekanini belgilaydi</li>
        <li>Rasm yuklang → saqlang → saytda darhol o'zgaradi</li>
        <li>Tavsiya: 1920×800 px, 300 KB dan oshmasin</li>
      </ul>
    </div>

  </div>

  <!-- TARKIB -->
  <div class="section-divider">📝 Sayt tarkibi</div>
  <div class="grid">

    <div class="card">
      <div class="card-header">
        <div class="icon" style="background:#dbeafe;">ℹ️</div>
        <div>
          <div class="card-title">Umumiy ma'lumot</div>
          <div class="card-link"><a href="/admin/core/generalinfo/">Tahrirlash →</a></div>
        </div>
      </div>
      <div class="affects">
        <div class="affects-title">Saytda nima o'zgaradi</div>
        <span class="tag">Header telefon/email</span>
        <span class="tag">Footer manzil</span>
        <span class="tag">Biz haqimizda sahifasi</span>
        <span class="tag">Aloqa sahifasi</span>
        <span class="tag">Ijtimoiy tarmoqlar</span>
      </div>
      <ul class="steps">
        <li>Tashkilot nomi — barcha sarlavhalarda ko'rinadi</li>
        <li>Telefon/email — headerda va aloqa sahifasida</li>
        <li>Ijtimoiy tarmoqlar — footer ikonkalari va havolalari</li>
        <li>Nizom havolasi — «Biz haqimizda» sahifasidagi yuklab olish tugmasi</li>
      </ul>
    </div>

    <div class="card">
      <div class="card-header">
        <div class="icon" style="background:#dcfce7;">📰</div>
        <div>
          <div class="card-title">Yangiliklar va bannerlar</div>
          <div class="card-link">
            <a href="/admin/news/news/">Yangiliklar →</a> &nbsp;
            <a href="/admin/core/banner/">Bannerlar →</a>
          </div>
        </div>
      </div>
      <div class="affects">
        <div class="affects-title">Saytda nima o'zgaradi</div>
        <span class="tag green">Bosh sahifa karusel</span>
        <span class="tag green">Yangiliklar ro'yxati</span>
        <span class="tag green">Yangilik sahifasi</span>
      </div>
      <ul class="steps">
        <li><b>Bannerlar</b> — bosh sahifadagi slayder (karusel)</li>
        <li>Tartib raqami kichik → bannerni oldinga suriladi</li>
        <li><b>Yangiliklar</b> → yangilik qo'shish → rasm + matn → Faol = Ha → Saqlash</li>
        <li>Yangilik saytda /news sahifasida ko'rinadi</li>
      </ul>
    </div>

    <div class="card">
      <div class="card-header">
        <div class="icon" style="background:#f3e8ff;">👔</div>
        <div>
          <div class="card-title">Rahbariyat</div>
          <div class="card-link"><a href="/admin/leadership/leader/">Tahrirlash →</a></div>
        </div>
      </div>
      <div class="affects">
        <div class="affects-title">Saytda nima o'zgaradi</div>
        <span class="tag purple">Rahbariyat sahifasi (/leadership)</span>
      </div>
      <ul class="steps">
        <li>Lavozim qo'shing → rahbar qo'shing → rasm yuklang</li>
        <li>Tartib raqami — ro'yxatdagi joylashuv</li>
        <li>«Faol» belgisi = saytda ko'rinadi</li>
      </ul>
    </div>

    <div class="card">
      <div class="card-header">
        <div class="icon" style="background:#fef9c3;">🏢</div>
        <div>
          <div class="card-title">Tuzilma (Bo'limlar)</div>
          <div class="card-link"><a href="/admin/structure/department/">Tahrirlash →</a></div>
        </div>
      </div>
      <div class="affects">
        <div class="affects-title">Saytda nima o'zgaradi</div>
        <span class="tag yellow">Tuzilma sahifasi (/structure)</span>
      </div>
      <ul class="steps">
        <li>Har bir bo'lim/department qo'shiladi</li>
        <li>«Ota bo'lim» — ierarxik ko'rinish uchun (ixtiyoriy)</li>
        <li>Bo'lim boshlig'i ismi — struktura kartochkasida ko'rinadi</li>
      </ul>
    </div>

    <div class="card">
      <div class="card-header">
        <div class="icon" style="background:#fce7f3;">📄</div>
        <div>
          <div class="card-title">Hujjatlar</div>
          <div class="card-link"><a href="/admin/documents/document/">Tahrirlash →</a></div>
        </div>
      </div>
      <div class="affects">
        <div class="affects-title">Saytda nima o'zgaradi</div>
        <span class="tag red">Hujjatlar sahifasi (/documents)</span>
      </div>
      <ul class="steps">
        <li>Hujjat kategoriyasini avval yarating</li>
        <li>Hujjat qo'shing → fayl yuklang (PDF/DOCX) → kategoriya tanlang</li>
        <li>«Faol» = saytda yuklab olish uchun ko'rinadi</li>
      </ul>
    </div>

    <div class="card">
      <div class="card-header">
        <div class="icon" style="background:#e0f2fe;">✉️</div>
        <div>
          <div class="card-title">Murojaatlar (Aloqa formi)</div>
          <div class="card-link"><a href="/admin/contact/appeal/">Ko'rish →</a></div>
        </div>
      </div>
      <div class="affects">
        <div class="affects-title">Saytda nima o'zgaradi</div>
        <span class="tag">Faqat o'qish — sayt formasidan keladi</span>
      </div>
      <ul class="steps">
        <li>Saytdagi «Aloqa» formasidan yuborilgan murojaatlar</li>
        <li>Yangi murojaat qo'shib bo'lmaydi — faqat ko'rish mumkin</li>
        <li>«Ko'rildi» statusini belgilash mumkin</li>
      </ul>
    </div>

  </div>

  <!-- NAVIGATSIYA -->
  <div class="section-divider">🧭 Navigatsiya va tuzilma</div>
  <div class="grid">

    <div class="card">
      <div class="card-header">
        <div class="icon" style="background:#dbeafe;">☰</div>
        <div>
          <div class="card-title">Navigatsiya (Navbar)</div>
          <div class="card-link"><a href="/admin/core/navitem/">Tahrirlash →</a></div>
        </div>
      </div>
      <div class="affects">
        <div class="affects-title">Saytda nima o'zgaradi</div>
        <span class="tag">Sayt yuqori menyu havolalari</span>
      </div>
      <ul class="steps">
        <li>Yangi element qo'shish → nomi + havola → tartib → Faol = Ha</li>
        <li>Havola: <code>/news</code>, <code>/about</code>, <code>/contact</code> va h.k.</li>
        <li>Tartib raqami kichik → menyuda oldinda ko'rinadi</li>
      </ul>
    </div>

    <div class="card">
      <div class="card-header">
        <div class="icon" style="background:#dcfce7;">🔗</div>
        <div>
          <div class="card-title">Footer havolalar</div>
          <div class="card-link"><a href="/admin/core/footerlink/">Tahrirlash →</a></div>
        </div>
      </div>
      <div class="affects">
        <div class="affects-title">Saytda nima o'zgaradi</div>
        <span class="tag green">Sayt pastki qismi (footer)</span>
      </div>
      <ul class="steps">
        <li>«Tezkor havolalar» — ichki sahifalar (Yangiliklar, Hujjatlar...)</li>
        <li>«Davlat saytlari» — tashqi havolalar (gov.uz, ssv.uz...)</li>
        <li>«Tashqi havola» = yangi oynada ochiladi</li>
      </ul>
    </div>

    <div class="card">
      <div class="card-header">
        <div class="icon" style="background:#fef3c7;">📦</div>
        <div>
          <div class="card-title">Sahifa bo'limlari</div>
          <div class="card-link"><a href="/admin/core/pagesection/">Tahrirlash →</a></div>
        </div>
      </div>
      <div class="affects">
        <div class="affects-title">Saytda nima o'zgaradi</div>
        <span class="tag yellow">Bosh sahifa qo'shimcha bloklari</span>
        <span class="tag yellow">«Biz haqimizda» qo'shimcha bo'limlari</span>
      </div>
      <ul class="steps">
        <li>Sahifa: <code>home</code> yoki <code>about</code></li>
        <li>Kartochkalar turi → quyida kartochkalar qo'shing</li>
        <li>Matn bloki → faqat sarlavha + matn yetarli</li>
      </ul>
    </div>

  </div>

  <div class="tip">
    💡 <b>Maslahat:</b> Har bir o'zgartirishdan so'ng saytni yangi browser oynasida
    <a href="/" target="_blank">http://46.224.219.146</a> ga o'tib tekshiring.
    O'zgarishlar darhol ko'rinadi — server qayta ishga tushirishni talab qilmaydi.
    <br><br>
    🌐 <b>Til:</b> Har bir maydonda (O'z), (Kr), (Ru) variantlarini to'ldiring.
    Foydalanuvchi saytda til almashtirganda tegishli matn ko'rinadi.
    Agar (Kr) va (Ru) bo'sh qoldirilsa, (O'z) matni ko'rsatiladi.
  </div>

</div>
</body>
</html>
"""


@staff_member_required
def admin_guide(request):
    return HttpResponse(GUIDE_HTML)
