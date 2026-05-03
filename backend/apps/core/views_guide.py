from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponse


GUIDE_HTML = """<!DOCTYPE html>
<html lang="uz">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Admin qo'llanma</title>
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body { font-family: 'Segoe UI', Tahoma, sans-serif; background: #f5f6fa; color: #2c3e50; line-height: 1.6; }
  .topbar {
    background: #2c3e50; color: #fff; padding: 16px 28px;
    display: flex; align-items: center; gap: 16px; font-size: 15px;
  }
  .topbar a { color: #ecf0f1; text-decoration: none; font-size: 13px; }
  .topbar a:hover { color: #3498db; }
  .topbar .lang-switch button {
    background: transparent; border: 1px solid #5d6d7e; color: #ecf0f1;
    padding: 5px 12px; margin-left: 4px; border-radius: 6px;
    font-size: 12px; cursor: pointer;
  }
  .topbar .lang-switch button.active { background: #3498db; border-color: #3498db; }
  .topbar .lang-switch button:hover { background: #34495e; }
  .container { max-width: 1100px; margin: 30px auto; padding: 0 20px 60px; }
  h1 { font-size: 24px; color: #2c3e50; margin-bottom: 8px; }
  .subtitle { color: #7f8c8d; font-size: 14px; margin-bottom: 24px; }
  .section { background: #fff; border-radius: 10px; padding: 22px 26px; margin-bottom: 16px;
    border: 1px solid #e1e5ea; box-shadow: 0 1px 3px rgba(0,0,0,.04); }
  .section h2 { font-size: 17px; color: #2c3e50; margin-bottom: 4px;
    display: flex; align-items: center; gap: 12px; }
  .section h2 .num {
    background: #3498db; color: #fff; width: 26px; height: 26px;
    border-radius: 50%; display: inline-flex; align-items: center;
    justify-content: center; font-size: 13px; font-weight: 700;
  }
  .section .where { color: #7f8c8d; font-size: 12px; margin-bottom: 12px; padding-left: 38px; }
  .section .where a { color: #3498db; text-decoration: none; font-weight: 600; }
  .section .where a:hover { text-decoration: underline; }
  .section ul { padding-left: 38px; margin-top: 8px; list-style: none; }
  .section li { font-size: 14px; color: #4a5568; padding: 4px 0 4px 18px;
    position: relative; }
  .section li::before { content: "\\2014"; position: absolute; left: 0; color: #95a5a6; }
  .tip {
    background: #fef9e7; border-left: 4px solid #f1c40f; border-radius: 6px;
    padding: 14px 18px; margin: 18px 0; font-size: 14px; color: #7d6608;
  }
  .tip b { color: #6c5400; }
  .lang-block { display: none; }
  .lang-block.active { display: block; }
  @media (max-width: 600px) { .topbar { flex-wrap: wrap; } .section .where, .section ul { padding-left: 0; margin-top: 12px; } }
</style>
</head>
<body>

<div class="topbar">
  <strong>Andijon SSB &mdash; Boshqaruv qo'llanmasi</strong>
  <span style="flex:1"></span>
  <span class="lang-switch">
    <button id="btn-uz" class="active" onclick="setLang('uz')">O'zbek</button>
    <button id="btn-kr" onclick="setLang('kr')">&#1038;&#1079;&#1073;&#1077;&#1082;</button>
    <button id="btn-ru" onclick="setLang('ru')">&#1056;&#1091;&#1089;&#1089;&#1082;&#1080;&#1081;</button>
  </span>
  <a href="/admin/">&larr; Admin panel</a>
</div>

<div class="container">

<!-- ============ O'ZBEK (LOTIN) ============ -->
<div class="lang-block active" id="lang-uz">
<h1>Saytni qanday boshqarish kerak</h1>
<p class="subtitle">Quyida har bir bo'lim saytning qaysi qismini boshqarishi tushuntirilgan. Tartib bo'yicha o'qing.</p>

<div class="section">
  <h2><span class="num">1</span> Tashkilot ma'lumotlari</h2>
  <p class="where">Qayerda: <a href="/admin/core/generalinfo/">Sayt boshqaruvi &rarr; Umumiy ma'lumot</a></p>
  <ul>
    <li>Tashkilot nomini, manzilini, telefon va elektron pochta yozasiz</li>
    <li>Bu ma'lumotlar saytning yuqori qismida va aloqa sahifasida ko'rinadi</li>
    <li>Telegram, Facebook, Instagram havolalarini kiriting &mdash; sayt ostidagi ikonkalar shu havolalarga olib boradi</li>
    <li>Har bir maydonda 3 ta til varianti bor: O'zbek, Krill, Rus &mdash; uchchalasini ham to'ldiring</li>
  </ul>
</div>

<div class="section">
  <h2><span class="num">2</span> Sayt rangini va logotipni o'zgartirish</h2>
  <p class="where">Qayerda: <a href="/admin/core/sitesettings/">Sayt boshqaruvi &rarr; Sayt sozlamalari</a></p>
  <ul>
    <li>Asosiy rang &mdash; tugmalar, havolalar va bosh sarlavhalar rangi</li>
    <li>Ikkinchi rang &mdash; ikkinchi darajali elementlar uchun</li>
    <li>Aksent rang &mdash; alohida ajratiladigan tugmalar uchun</li>
    <li>Rangni tanlash uchun kvadrat ustiga bosing &mdash; palitra ochiladi</li>
    <li>Logotip va Favicon (brauzer yorlig'i rasmi) ham shu yerda yuklanadi</li>
  </ul>
</div>

<div class="section">
  <h2><span class="num">3</span> Bosh sahifadagi katta rasmlar (slayder)</h2>
  <p class="where">Qayerda: <a href="/admin/core/banner/">Sayt boshqaruvi &rarr; Bannerlar</a></p>
  <ul>
    <li>Bosh sahifaning eng yuqorisida aylanib turadigan katta rasmlar</li>
    <li>Yangi qo'shish &rarr; rasm yuklash, sarlavha va matn yozish &rarr; saqlash</li>
    <li>Tartib raqami kichik bo'lgan banner birinchi ko'rinadi</li>
    <li>"Faol" belgisi olib tashlangan banner saytda ko'rinmaydi</li>
  </ul>
</div>

<div class="section">
  <h2><span class="num">4</span> Yangiliklar</h2>
  <p class="where">Qayerda: <a href="/admin/news/news/">Yangiliklar &rarr; Yangiliklar</a></p>
  <ul>
    <li>Yangi yangilik qo'shish uchun "Yangilik qo'shish" tugmasini bosing</li>
    <li>Sarlavha, matn va rasmni 3 tilda kiriting</li>
    <li>Kategoriya tanlang yoki yangisini yarating</li>
    <li>"Faol" belgini qo'ying &mdash; yangilik darhol saytda paydo bo'ladi</li>
  </ul>
</div>

<div class="section">
  <h2><span class="num">5</span> Rahbariyat</h2>
  <p class="where">Qayerda: <a href="/admin/leadership/leader/">Rahbariyat &rarr; Rahbarlar</a></p>
  <ul>
    <li>Rahbarning rasmi, ism-sharifi, lavozimi, biografiyasi yoziladi</li>
    <li>Qabul kunlari va boshqa ma'lumotlar ham shu yerda</li>
    <li>"Faol" belgisi qo'yilgan rahbar saytda ko'rinadi</li>
    <li>Tartib raqami eng kichik bo'lgan rahbar yuqorida ko'rinadi (boshliq birinchi)</li>
  </ul>
</div>

<div class="section">
  <h2><span class="num">6</span> Tashkiliy tuzilma (bo'limlar)</h2>
  <p class="where">Qayerda: <a href="/admin/structure/department/">Tuzilma &rarr; Bo'limlar</a></p>
  <ul>
    <li>Boshqarmaning ichki bo'limlari ro'yxati</li>
    <li>Har bir bo'limning nomi, boshlig'i va xodimlar soni kiritiladi</li>
    <li>Bo'limni boshqa bo'lim ichiga joylashtirish uchun "Ota bo'lim"ni tanlang</li>
  </ul>
</div>

<div class="section">
  <h2><span class="num">7</span> Hujjatlar</h2>
  <p class="where">Qayerda: <a href="/admin/documents/document/">Hujjatlar &rarr; Hujjatlar</a></p>
  <ul>
    <li>PDF yoki Word formatdagi hujjatlarni yuklash uchun</li>
    <li>Sarlavha, fayl va kategoriya tanlang &mdash; saqlang</li>
    <li>Saytning Hujjatlar sahifasida foydalanuvchilar yuklab olishi mumkin</li>
  </ul>
</div>

<div class="section">
  <h2><span class="num">8</span> Saytning yuqori menyusi</h2>
  <p class="where">Qayerda: <a href="/admin/core/navitem/">Sayt boshqaruvi &rarr; Yuqori menyu havolalari</a></p>
  <ul>
    <li>Saytning eng yuqorisidagi havolalar (Bosh sahifa, Yangiliklar, Bog'lanish va h.k.)</li>
    <li>Yangi havola qo'shish uchun "Qo'shish" tugmasini bosing</li>
    <li>Tartib raqami kichik bo'lgan havola chap tomonda ko'rinadi</li>
  </ul>
</div>

<div class="section">
  <h2><span class="num">9</span> Saytning pastki qismi (Footer)</h2>
  <p class="where">Qayerda: <a href="/admin/core/footerlink/">Sayt boshqaruvi &rarr; Pastki menyu havolalari</a></p>
  <ul>
    <li>Saytning eng ostidagi havolalar (Tezkor havolalar va Davlat saytlari)</li>
    <li>"Tezkor havolalar" &mdash; ichki sahifalar (Yangiliklar, Hujjatlar, Aloqa)</li>
    <li>"Davlat saytlari" &mdash; tashqi havolalar (gov.uz, ssv.uz)</li>
  </ul>
</div>

<div class="section">
  <h2><span class="num">10</span> Murojaatlar (foydalanuvchilardan kelgan xabarlar)</h2>
  <p class="where">Qayerda: <a href="/admin/contact/appeal/">Murojaatlar &rarr; Murojaatlar</a></p>
  <ul>
    <li>Foydalanuvchilar saytdagi "Bog'lanish" formasi orqali yuborgan xabarlar shu yerga keladi</li>
    <li>Har bir murojaatda: F.I.Sh., telefon, hudud, mavzu va matn ko'rsatiladi</li>
    <li>Murojaatni ochib, holatini o'zgartiring: "Yangi" &rarr; "Ko'rib chiqilmoqda" &rarr; "Hal etildi"</li>
    <li>Bu yerda yangi murojaat qo'shib bo'lmaydi &mdash; faqat ko'rish va holat o'zgartirish</li>
    <li>Yuqorida sana va holat bo'yicha filtrlash mumkin</li>
  </ul>
</div>

<div class="section">
  <h2><span class="num">11</span> Yangi xodim (admin) qo'shish va ruxsatlar</h2>
  <p class="where">Qayerda: <a href="/admin/auth/user/">Foydalanuvchilar &rarr; Foydalanuvchilar</a></p>
  <ul>
    <li>"Foydalanuvchi qo'shish" tugmasini bosing &mdash; foydalanuvchi nomi va parolni kiriting</li>
    <li>So'ng "Saqlash va davom ettirish" &mdash; ruxsatlar sahifasi ochiladi</li>
    <li><b>"Xodimlar maqomi" (Staff status)</b> &mdash; bu belgi qo'yilmasa, foydalanuvchi admin paneliga kira olmaydi. Albatta qo'ying.</li>
    <li><b>"Super foydalanuvchi" (Superuser)</b> &mdash; faqat asosiy administrator uchun. Hech qachon oddiy xodimga bermang!</li>
    <li><b>"Guruhlar"</b> &mdash; foydalanuvchini guruhga qo'shing (Yangiliklar muharriri, Murojaatlarni boshqaruvchi va h.k.). Guruhga ruxsat berilgan bo'limlarga kirish hosil bo'ladi.</li>
    <li>Yangi guruh yaratish: <a href="/admin/auth/group/">Foydalanuvchilar &rarr; Guruhlar &rarr; Qo'shish</a></li>
  </ul>
</div>

<div class="section">
  <h2><span class="num">12</span> Saytni boshqa tashkilot uchun moslashtirish</h2>
  <p class="where">Qayerda: <a href="/admin/core/generalinfo/">Umumiy ma'lumot</a> + <a href="/admin/core/sitesettings/">Sayt sozlamalari</a></p>
  <ul>
    <li><b>Tashkilot nomi</b> &mdash; "Umumiy ma'lumot" bo'limidagi 3 tildagi "nomi" maydonlari. Bu nom saytning yuqori qismida, footerda va brauzer yorlig'ida ko'rinadi</li>
    <li><b>Logotip</b> va <b>Favicon</b> &mdash; "Sayt sozlamalari"da yuklanadi. Logotipni 240&times;60 px PNG yoki SVG formatda yuklang</li>
    <li><b>Ranglar</b> &mdash; "Sayt sozlamalari" da Asosiy/Ikkinchi/Aksent rang. Ranglar saqlanganda saytda darhol o'zgaradi (sayfani yangilang)</li>
    <li><b>Manzil, telefon, email</b> &mdash; "Umumiy ma'lumot"da</li>
    <li><b>Ijtimoiy tarmoqlar</b> &mdash; "Umumiy ma'lumot"dagi Telegram/Facebook/Instagram havolalari</li>
    <li><b>Yuqori menyu havolalari</b> &mdash; "Yuqori menyu havolalari"da har bir tashkilot uchun moslab kiritiladi</li>
    <li><b>Bosh sahifa bannerlari</b> &mdash; har bir tashkilot uchun maxsus rasmlar va matnlar yuklanadi</li>
    <li>Bir kalit so'z bilan: barcha matn, rang, rasm, havola admin paneldan o'zgartiriladi &mdash; kodga tegmasdan</li>
  </ul>
</div>

<div class="tip">
  <b>Eslatma:</b> O'zgartirishlar saqlangandan so'ng saytni yangilang (F5) &mdash; o'zgarishlar darhol ko'rinadi.
  Server qayta ishga tushirilishi shart emas. Biror muammo yuzaga kelsa, IT mutaxassisingizga murojaat qiling.
</div>
</div>

<!-- ============ KRILL ============ -->
<div class="lang-block" id="lang-kr">
<h1>Сайтни қандай бошқариш керак</h1>
<p class="subtitle">Қуйида ҳар бир бўлим сайтнинг қайси қисмини бошқариши тушунтирилган.</p>

<div class="section">
  <h2><span class="num">1</span> Ташкилот маълумотлари</h2>
  <p class="where">Қаерда: <a href="/admin/core/generalinfo/">Сайт бошқаруви &rarr; Умумий маълумот</a></p>
  <ul>
    <li>Ташкилот номини, манзилини, телефон ва электрон почта ёзасиз</li>
    <li>Бу маълумотлар сайтнинг юқори қисмида ва алоқа саҳифасида кўринади</li>
    <li>Телеграм, Фейсбук, Инстаграм ҳаволаларини киритинг</li>
    <li>Ҳар бир майдонда 3 та тил варианти бор &mdash; уччаласини ҳам тўлдиринг</li>
  </ul>
</div>

<div class="section">
  <h2><span class="num">2</span> Сайт рангини ва логотипни ўзгартириш</h2>
  <p class="where">Қаерда: <a href="/admin/core/sitesettings/">Сайт бошқаруви &rarr; Сайт созламалари</a></p>
  <ul>
    <li>Асосий ранг &mdash; тугмалар, ҳаволалар ва бош сарлавҳалар ранги</li>
    <li>Ранг танлаш учун квадрат устига босинг &mdash; палитра очилади</li>
    <li>Логотип ва Фавикон ҳам шу ерда юкланади</li>
  </ul>
</div>

<div class="section">
  <h2><span class="num">3</span> Бош саҳифадаги катта расмлар (слайдер)</h2>
  <p class="where">Қаерда: <a href="/admin/core/banner/">Сайт бошқаруви &rarr; Баннерлар</a></p>
  <ul>
    <li>Бош саҳифанинг энг юқорисида айланиб турадиган катта расмлар</li>
    <li>Янги қўшиш &rarr; расм юклаш &rarr; сарлавҳа ва матн ёзиш &rarr; сақлаш</li>
    <li>Тартиб рақами кичик бўлган баннер биринчи кўринади</li>
  </ul>
</div>

<div class="section">
  <h2><span class="num">4</span> Янгиликлар</h2>
  <p class="where">Қаерда: <a href="/admin/news/news/">Янгиликлар &rarr; Янгиликлар</a></p>
  <ul>
    <li>"Янгилик қўшиш" тугмасини босинг</li>
    <li>Сарлавҳа, матн ва расмни 3 тилда киритинг</li>
    <li>"Фаол" белгини қўйинг &mdash; янгилик дарҳол сайтда пайдо бўлади</li>
  </ul>
</div>

<div class="section">
  <h2><span class="num">5</span> Раҳбарият</h2>
  <p class="where">Қаерда: <a href="/admin/leadership/leader/">Раҳбарият &rarr; Раҳбарлар</a></p>
  <ul>
    <li>Раҳбарнинг расми, исм-шарифи, лавозими, биографияси ёзилади</li>
    <li>Қабул кунлари ва бошқа маълумотлар ҳам шу ерда</li>
    <li>Тартиб рақами энг кичик бўлган раҳбар юқорида кўринади</li>
  </ul>
</div>

<div class="section">
  <h2><span class="num">6</span> Ташкилий тузилма (бўлимлар)</h2>
  <p class="where">Қаерда: <a href="/admin/structure/department/">Тузилма &rarr; Бўлимлар</a></p>
  <ul>
    <li>Бошқарманинг ички бўлимлари рўйхати</li>
    <li>Ҳар бир бўлимнинг номи, бошлиғи ва ходимлар сони киритилади</li>
  </ul>
</div>

<div class="section">
  <h2><span class="num">7</span> Ҳужжатлар</h2>
  <p class="where">Қаерда: <a href="/admin/documents/document/">Ҳужжатлар &rarr; Ҳужжатлар</a></p>
  <ul>
    <li>PDF ёки Word форматдаги ҳужжатларни юклаш учун</li>
    <li>Сарлавҳа, файл ва категория танланг &mdash; сақланг</li>
  </ul>
</div>

<div class="section">
  <h2><span class="num">8</span> Сайтнинг юқори менюси</h2>
  <p class="where">Қаерда: <a href="/admin/core/navitem/">Сайт бошқаруви &rarr; Юқори меню ҳаволалари</a></p>
  <ul>
    <li>Сайтнинг энг юқорисидаги ҳаволалар (Бош саҳифа, Янгиликлар ва ҳ.к.)</li>
    <li>Тартиб рақами кичик бўлган ҳавола чап томонда кўринади</li>
  </ul>
</div>

<div class="section">
  <h2><span class="num">9</span> Сайтнинг пастки қисми</h2>
  <p class="where">Қаерда: <a href="/admin/core/footerlink/">Сайт бошқаруви &rarr; Пастки меню ҳаволалари</a></p>
  <ul>
    <li>"Тезкор ҳаволалар" &mdash; ички саҳифалар (Янгиликлар, Ҳужжатлар, Алоқа)</li>
    <li>"Давлат сайтлари" &mdash; ташқи ҳаволалар (gov.uz, ssv.uz)</li>
  </ul>
</div>

<div class="section">
  <h2><span class="num">10</span> Мурожаатлар</h2>
  <p class="where">Қаерда: <a href="/admin/contact/appeal/">Мурожаатлар &rarr; Мурожаатлар</a></p>
  <ul>
    <li>Фойдаланувчилар сайт орқали юборган хабарлар шу ерга келади</li>
    <li>Ҳар бир мурожаатда: Ф.И.Ш., телефон, ҳудуд, мавзу ва матн кўрсатилади</li>
    <li>Ҳолатини ўзгартиринг: "Янги" &rarr; "Кўриб чиқилмоқда" &rarr; "Ҳал этилди"</li>
  </ul>
</div>

<div class="section">
  <h2><span class="num">11</span> Янги ходим (админ) қўшиш ва рухсатлар</h2>
  <p class="where">Қаерда: <a href="/admin/auth/user/">Фойдаланувчилар &rarr; Фойдаланувчилар</a></p>
  <ul>
    <li>"Фойдаланувчи қўшиш" тугмасини босинг, фойдаланувчи номи ва паролни киритинг</li>
    <li><b>"Ходимлар мақоми"</b> белгисини қўйинг &mdash; усиз админ панелига кириб бўлмайди</li>
    <li><b>"Супер фойдаланувчи"</b> &mdash; фақат асосий администратор учун, оддий ходимга берманг</li>
    <li><b>"Гуруҳлар"</b> орқали рухсатлар бериш мумкин (Янгиликлар мухаррири ва ҳ.к.)</li>
    <li>Янги гуруҳ: <a href="/admin/auth/group/">Фойдаланувчилар &rarr; Гуруҳлар</a></li>
  </ul>
</div>

<div class="section">
  <h2><span class="num">12</span> Сайтни бошқа ташкилот учун мослаштириш</h2>
  <p class="where">Қаерда: <a href="/admin/core/generalinfo/">Умумий маълумот</a> + <a href="/admin/core/sitesettings/">Сайт созламалари</a></p>
  <ul>
    <li><b>Ташкилот номи</b> &mdash; "Умумий маълумот" бўлимидаги 3 тилдаги "номи" майдонлари</li>
    <li><b>Логотип</b> ва <b>Фавикон</b> &mdash; "Сайт созламалари"да юкланади</li>
    <li><b>Ранглар</b> &mdash; "Сайт созламалари"да Асосий / Иккинчи / Аксент. Сайтда дарҳол ўзгаради</li>
    <li><b>Манзил, телефон, email</b> &mdash; "Умумий маълумот"да</li>
    <li>Барча матн, ранг, расм ва ҳавола админ панелдан ўзгартирилади &mdash; кодга тегмасдан</li>
  </ul>
</div>

<div class="tip">
  <b>Эслатма:</b> Ўзгартиришлар сақлангандан сўнг сайтни янгиланг (F5) &mdash; ўзгаришлар дарҳол кўринади.
</div>
</div>

<!-- ============ RUSSKIY ============ -->
<div class="lang-block" id="lang-ru">
<h1>Как управлять сайтом</h1>
<p class="subtitle">Ниже объясняется, какой раздел отвечает за какую часть сайта.</p>

<div class="section">
  <h2><span class="num">1</span> Информация об организации</h2>
  <p class="where">Где: <a href="/admin/core/generalinfo/">Управление сайтом &rarr; Общая информация</a></p>
  <ul>
    <li>Введите название, адрес, телефон и email организации</li>
    <li>Эти данные отображаются в шапке сайта и на странице контактов</li>
    <li>Введите ссылки на Telegram, Facebook, Instagram</li>
    <li>В каждом поле есть 3 языковых варианта &mdash; заполните все три</li>
  </ul>
</div>

<div class="section">
  <h2><span class="num">2</span> Изменение цвета сайта и логотипа</h2>
  <p class="where">Где: <a href="/admin/core/sitesettings/">Управление сайтом &rarr; Настройки сайта</a></p>
  <ul>
    <li>Основной цвет &mdash; цвет кнопок, ссылок и заголовков</li>
    <li>Чтобы выбрать цвет, нажмите на квадрат &mdash; откроется палитра</li>
    <li>Логотип и Favicon также загружаются здесь</li>
  </ul>
</div>

<div class="section">
  <h2><span class="num">3</span> Большие изображения на главной (слайдер)</h2>
  <p class="where">Где: <a href="/admin/core/banner/">Управление сайтом &rarr; Баннеры</a></p>
  <ul>
    <li>Большие изображения, которые крутятся вверху главной страницы</li>
    <li>Добавить новый &rarr; загрузить изображение &rarr; написать заголовок и текст &rarr; сохранить</li>
    <li>Баннер с меньшим порядковым номером показывается первым</li>
  </ul>
</div>

<div class="section">
  <h2><span class="num">4</span> Новости</h2>
  <p class="where">Где: <a href="/admin/news/news/">Новости &rarr; Новости</a></p>
  <ul>
    <li>Нажмите кнопку "Добавить новость"</li>
    <li>Введите заголовок, текст и изображение на 3 языках</li>
    <li>Поставьте отметку "Активно" &mdash; новость сразу появится на сайте</li>
  </ul>
</div>

<div class="section">
  <h2><span class="num">5</span> Руководство</h2>
  <p class="where">Где: <a href="/admin/leadership/leader/">Руководство &rarr; Руководители</a></p>
  <ul>
    <li>Фото, ФИО, должность, биография руководителя</li>
    <li>Дни приёма и другая информация также здесь</li>
    <li>Руководитель с наименьшим порядковым номером показывается выше (начальник первым)</li>
  </ul>
</div>

<div class="section">
  <h2><span class="num">6</span> Структура (отделы)</h2>
  <p class="where">Где: <a href="/admin/structure/department/">Структура &rarr; Отделы</a></p>
  <ul>
    <li>Список внутренних отделов управления</li>
    <li>Название каждого отдела, начальник и количество сотрудников</li>
  </ul>
</div>

<div class="section">
  <h2><span class="num">7</span> Документы</h2>
  <p class="where">Где: <a href="/admin/documents/document/">Документы &rarr; Документы</a></p>
  <ul>
    <li>Для загрузки документов в формате PDF или Word</li>
    <li>Введите заголовок, выберите файл и категорию &mdash; сохраните</li>
  </ul>
</div>

<div class="section">
  <h2><span class="num">8</span> Верхнее меню сайта</h2>
  <p class="where">Где: <a href="/admin/core/navitem/">Управление сайтом &rarr; Ссылки верхнего меню</a></p>
  <ul>
    <li>Ссылки в самом верху сайта (Главная, Новости, Контакты и т.д.)</li>
    <li>Ссылка с меньшим порядковым номером показывается слева</li>
  </ul>
</div>

<div class="section">
  <h2><span class="num">9</span> Нижняя часть сайта (футер)</h2>
  <p class="where">Где: <a href="/admin/core/footerlink/">Управление сайтом &rarr; Ссылки нижнего меню</a></p>
  <ul>
    <li>"Быстрые ссылки" &mdash; внутренние страницы (Новости, Документы, Контакты)</li>
    <li>"Госпорталы" &mdash; внешние ссылки (gov.uz, ssv.uz)</li>
  </ul>
</div>

<div class="section">
  <h2><span class="num">10</span> Обращения</h2>
  <p class="where">Где: <a href="/admin/contact/appeal/">Обращения &rarr; Обращения</a></p>
  <ul>
    <li>Сообщения, отправленные пользователями через форму контактов сайта</li>
    <li>В каждом обращении: ФИО, телефон, регион, тема и текст</li>
    <li>Изменяйте статус: "Новое" &rarr; "Рассматривается" &rarr; "Решено"</li>
    <li>Добавлять новые нельзя &mdash; только просмотр и изменение статуса</li>
  </ul>
</div>

<div class="section">
  <h2><span class="num">11</span> Добавление нового сотрудника (админа) и права доступа</h2>
  <p class="where">Где: <a href="/admin/auth/user/">Пользователи &rarr; Пользователи</a></p>
  <ul>
    <li>Нажмите "Добавить пользователя", введите имя пользователя и пароль</li>
    <li>Поставьте галочку <b>"Статус сотрудника"</b> &mdash; без неё пользователь не сможет войти в админку</li>
    <li><b>"Суперпользователь"</b> &mdash; только для главного администратора. Не давайте обычным сотрудникам!</li>
    <li>Через <b>"Группы"</b> можно назначать права (Редактор новостей и т.д.)</li>
    <li>Создание группы: <a href="/admin/auth/group/">Пользователи &rarr; Группы</a></li>
  </ul>
</div>

<div class="section">
  <h2><span class="num">12</span> Адаптация сайта под другую организацию</h2>
  <p class="where">Где: <a href="/admin/core/generalinfo/">Общая информация</a> + <a href="/admin/core/sitesettings/">Настройки сайта</a></p>
  <ul>
    <li><b>Название организации</b> &mdash; в разделе "Общая информация" (3 языка)</li>
    <li><b>Логотип</b> и <b>Favicon</b> загружаются в "Настройках сайта"</li>
    <li><b>Цвета</b> &mdash; Основной / Вторичный / Акцент. Меняются на сайте сразу</li>
    <li><b>Адрес, телефон, email</b> &mdash; в "Общей информации"</li>
    <li>Весь текст, цвета, изображения и ссылки меняются через админ-панель &mdash; без вмешательства в код</li>
  </ul>
</div>

<div class="tip">
  <b>Примечание:</b> После сохранения изменений обновите сайт (F5) &mdash; изменения отобразятся сразу.
</div>
</div>

</div>

<script>
function setLang(lang) {
  document.querySelectorAll('.lang-block').forEach(b => b.classList.remove('active'));
  document.getElementById('lang-' + lang).classList.add('active');
  document.querySelectorAll('.lang-switch button').forEach(b => b.classList.remove('active'));
  document.getElementById('btn-' + lang).classList.add('active');
  try { localStorage.setItem('admin-guide-lang', lang); } catch(e) {}
}
try {
  var saved = localStorage.getItem('admin-guide-lang');
  if (saved && ['uz','kr','ru'].indexOf(saved) >= 0) setLang(saved);
} catch(e) {}
</script>

</body>
</html>
"""


@staff_member_required
def admin_guide(request):
    return HttpResponse(GUIDE_HTML)
