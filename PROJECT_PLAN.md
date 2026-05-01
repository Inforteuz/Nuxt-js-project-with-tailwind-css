# 🏥 Andijon viloyati sog'liqni saqlash boshqarmasi — Veb-sayt loyihasi

## 📋 Umumiy ma'lumot

| Parametr | Qiymat |
|---|---|
| **Tashkilot** | O'zbekiston Respublikasi sog'liqni saqlash vazirligi — Andijon viloyati hokimligi sog'liqni saqlash boshqarmasi |
| **Manzil** | 710000, Andijon shahar, Amir Umarxon ko'chasi, 19-uy |
| **Telefon/Faks** | (374) 228-42-84 |
| **Email** | andijon.vssb@ssv.uz |
| **Namuna saytlar** | [gov.uz](https://gov.uz), [dermatolog.uz](https://dermatolog.uz) |
| **Server** | 46.224.219.146 (root) |

---

## 🎯 Loyiha maqsadi

1. Andijon viloyati sog'liqni saqlash boshqarmasi uchun zamonaviy, xavfsiz va professional veb-sayt yaratish
2. Gov.uz standartlariga mos davlat muassasasi veb-sayti
3. Keyinchalik **100+ tibbiyot tashkilotlari** uchun rang va dizaynni o'zgartirib ko'paytirish mumkin bo'lgan **universal template** yaratish
4. Yuqori darajadagi xavfsizlik: DDoS himoyasi, IP rate limiting, sayt uzluksiz ishlashi

---

## 🏗️ Texnologiyalar steki

### Frontend
| Texnologiya | Versiya | Maqsad |
|---|---|---|
| **Nuxt.js 3** | ^3.9.1 | SSR/SSG framework |
| **Tailwind CSS** | ^3.4.18 | Asosiy styling |
| **Custom CSS** | - | Qo'shimcha animatsiyalar, effektlar, loader |
| **Vue 3** | Nuxt ichida | Reaktiv UI komponentlari |

### Backend (2-bosqich)
| Texnologiya | Maqsad |
|---|---|
| **Python Django** | REST API, Admin panel |
| **Django REST Framework** | API endpointlar |
| **PostgreSQL** | Ma'lumotlar bazasi |
| **Gunicorn + Nginx** | Production server |

### Xavfsizlik
| Vosita | Maqsad |
|---|---|
| **Nginx rate limiting** | So'rovlarni cheklash |
| **fail2ban** | IP bloklash |
| **Django middleware** | CSRF, XSS, SQL injection himoyasi |
| **Cloudflare (ixtiyoriy)** | DDoS himoyasi |
| **SSL/TLS** | HTTPS shifrlash |
| **Security headers** | Content-Security-Policy, HSTS va boshqalar |

---

## 📐 Sayt arxitekturasi va sahifalar

### Landing page bo'limlari (Single Page + Ichki sahifalar)

```
/ (Bosh sahifa — Landing page)
├── Hero section (Bosh banner + loader animatsiya)
├── Umumiy ma'lumotlar bo'limi
├── Rahbariyat bo'limi
├── Tashkiliy tuzilma bo'limi
├── Yangiliklar bo'limi
├── Statistika bo'limi
├── Bog'lanish bo'limi
└── Footer

/about — Boshqarma haqida
├── To'liq nomi
├── Tashkil etilgan sanasi
├── Vazifa va funksiyalari
└── Huquqiy maqomi

/leadership — Rahbariyat
├── Boshqarma boshlig'i
├── O'rinbosarlar
├── F.I.Sh., Lavozimi
├── Qabul kunlari
└── Bog'lanish ma'lumotlari

/structure — Tashkiliy tuzilma
├── Tashkiliy tuzilma sxemasi
├── Bo'limlar ro'yxati
└── Ularning vazifalari

/documents — Normativ-huquqiy hujjatlar
├── Qonunlar
├── Prezident farmonlari
├── Vazirlar Mahkamasi qarorlari
├── Buyruq va nizomlar
└── Elektron havolalar

/news — Yangiliklar
├── So'nggi yangiliklar
├── E'lonlar
├── Tadbirlar
└── Press-relizlar

/contact — Bog'lanish
├── Manzil va xarita
├── Telefon va email
├── Interaktiv murojaat shakli
├── Virtual qabulxona
└── Murojaat tartibi
```

---

## 🎨 Dizayn konseptsiyasi

### Rang palitrasi (Davlat tibbiyot uslubi)
```
Primary:     #0A4D8C (Quyuq ko'k — davlat ishonchi)
Secondary:   #10B981 (Yashil — tibbiyot, sog'liq)
Accent:      #F59E0B (Oltin — O'zbekiston bayrog'i)
Background:  #F8FAFC (Och kulrang)
Dark:        #0F172A (Matn uchun)
White:       #FFFFFF
Success:     #22C55E
Warning:     #EAB308
Danger:      #EF4444
```

### Dizayn tamoyillari
- **Minimalizm** — Ortiqcha element yo'q, toza interfeys
- **Gov.uz uslubi** — Rasmiy davlat sayti ko'rinishi
- **Dermatolog.uz ilhomi** — Professional tibbiyot dizayni
- **Responsive** — Barcha qurilmalarda to'g'ri ko'rinishi
- **Accessibility** — Imkoniyati cheklangan foydalanuvchilar uchun mos

### Animatsiyalar va effektlar
- **Page loader** — Professional tibbiyot logotipi bilan yuklanish animatsiyasi
- **Scroll animatsiyalar** — Elementlarning asta-sekin paydo bo'lishi (fade-in, slide-up)
- **Hover effektlari** — Kartochkalar va tugmalar uchun
- **Counter animatsiya** — Statistika raqamlari uchun
- **Smooth scroll** — Sahifalar orasida silliq o'tish
- **Parallax** — Hero seksiyada chuqurlik effekti

---

## 📁 Loyiha fayl strukturasi

```
andijon-ssv/
├── app/
│   ├── app.vue                    # Root component (Loader + NuxtPage)
│   ├── components/
│   │   ├── layout/
│   │   │   ├── TheHeader.vue      # Sayt sarlavhasi (header)
│   │   │   ├── TheNavbar.vue      # Navigatsiya paneli
│   │   │   ├── TheFooter.vue      # Pastki qism (footer)
│   │   │   └── TheMobileMenu.vue  # Mobil menyu
│   │   ├── home/
│   │   │   ├── HeroSection.vue    # Bosh banner
│   │   │   ├── AboutPreview.vue   # Boshqarma haqida qisqacha
│   │   │   ├── LeadershipPreview.vue  # Rahbariyat
│   │   │   ├── NewsSection.vue    # Yangiliklar
│   │   │   ├── StatsSection.vue   # Statistika
│   │   │   └── ContactPreview.vue # Bog'lanish
│   │   ├── ui/
│   │   │   ├── AppLoader.vue      # Sahifa yuklanishi
│   │   │   ├── AppBreadcrumb.vue  # Breadcrumb navigatsiya
│   │   │   ├── AppCard.vue        # Universal karta
│   │   │   └── AppButton.vue      # Universal tugma
│   │   └── shared/
│   │       ├── GovLinks.vue       # Davlat saytlari havolalari
│   │       └── SocialLinks.vue    # Ijtimoiy tarmoqlar
│   ├── layouts/
│   │   └── default.vue            # Asosiy layout
│   └── pages/
│       ├── index.vue              # Bosh sahifa
│       ├── about.vue              # Boshqarma haqida
│       ├── leadership.vue         # Rahbariyat
│       ├── structure.vue          # Tashkiliy tuzilma
│       ├── documents.vue          # Hujjatlar
│       ├── news/
│       │   ├── index.vue          # Yangiliklar ro'yxati
│       │   └── [id].vue           # Yangilik tafsilotlari
│       └── contact.vue            # Bog'lanish
├── assets/
│   └── css/
│       ├── tailwind.css           # Tailwind base
│       └── style.css              # Custom animatsiyalar va effektlar
├── public/
│   ├── images/                    # Rasmlar
│   ├── icons/                     # Ikonkalar
│   └── favicon.ico                # Favicon
├── nuxt.config.ts                 # Nuxt konfiguratsiya
├── tailwind.config.js             # Tailwind konfiguratsiya
├── package.json                   # Paketlar
├── PROJECT_PLAN.md                # Shu fayl
└── README.md                      # Loyiha haqida
```

---

## 🔒 Xavfsizlik rejasi

### 1-daraja: Nginx (Frontend)
```nginx
# Rate limiting
limit_req_zone $binary_remote_addr zone=api:10m rate=10r/s;
limit_req_zone $binary_remote_addr zone=login:10m rate=3r/m;
limit_conn_zone $binary_remote_addr zone=addr:10m;

# DDoS himoyasi
client_body_timeout 10;
client_header_timeout 10;
keepalive_timeout 5 5;
send_timeout 10;
client_max_body_size 1m;
```

### 2-daraja: Xavfsizlik headerlari
```
X-Frame-Options: SAMEORIGIN
X-Content-Type-Options: nosniff
X-XSS-Protection: 1; mode=block
Content-Security-Policy: default-src 'self'
Strict-Transport-Security: max-age=31536000; includeSubDomains
Referrer-Policy: strict-origin-when-cross-origin
Permissions-Policy: camera=(), microphone=(), geolocation=()
```

### 3-daraja: Server (2-bosqich — Backend)
- Django CSRF middleware
- Django SecurityMiddleware
- Parameterized SQL queries (ORM)
- Input validation va sanitization
- fail2ban integratsiyasi
- Firewall (UFW) sozlamalari

---

## 🚀 Deploy rejasi

### 1-bosqich: Frontend (HOZIR)
1. ✅ GitHub templatedan clone qilish
2. ⬜ Nuxt.js loyihasini sozlash
3. ⬜ Barcha komponentlarni yaratish
4. ⬜ Landing page dizaynini yaratish
5. ⬜ Animatsiya va loaderlarni qo'shish
6. ⬜ Responsive dizayn
7. ⬜ `nuxt build` bilan production build
8. ⬜ Serverga deploy (Nginx + Node.js)
9. ⬜ SSL sertifikat o'rnatish (agar domen bo'lsa)

### 2-bosqich: Backend (KEYINCHALIK)
1. ⬜ Django loyihasini yaratish
2. ⬜ PostgreSQL bazasini sozlash
3. ⬜ REST API endpointlarni yaratish
4. ⬜ Admin panel
5. ⬜ Frontend-Backend integratsiya
6. ⬜ Xavfsizlik testlari
7. ⬜ Load testing

---

## 📊 Template ko'paytirish strategiyasi

Bu loyiha **universal template** sifatida yaratiladi:

### O'zgartiriladigan elementlar:
1. **Rang palitrasi** — `tailwind.config.js` dagi ranglar
2. **Logotip va rasmlar** — `public/images/` papkasi
3. **Tashkilot ma'lumotlari** — `config/site.js` yoki `.env` fayli
4. **Kontent** — Backend orqali boshqariladi

### 100+ sayt uchun rejalashtirish:
```
config/site.js yoki .env faylida:
- SITE_NAME = "Tashkilot nomi"
- SITE_ADDRESS = "Manzil"
- SITE_PHONE = "Telefon"
- SITE_EMAIL = "Email"
- PRIMARY_COLOR = "#0A4D8C"
- SECONDARY_COLOR = "#10B981"
```

---

## ⏱️ Taxminiy vaqt jadvali

| Bosqich | Vaqt | Holat |
|---|---|---|
| Reja tuzish | 1 soat | ✅ Tayyor |
| Frontend dizayn | 4-6 soat | ⬜ Jarayonda |
| Animatsiyalar | 2 soat | ⬜ Kutilmoqda |
| Deploy | 1 soat | ⬜ Kutilmoqda |
| Backend | 6-8 soat | ⬜ 2-bosqich |
| Xavfsizlik | 2-3 soat | ⬜ 2-bosqich |

---

## 🖥️ Server ma'lumotlari

| Parametr | Qiymat |
|---|---|
| **IP** | 46.224.219.146 |
| **SSH** | `ssh root@46.224.219.146` |
| **Password** | `12345-inforte` |
| **OS** | Ubuntu (aaPanel o'rnatilgan) |
| **Frontend port** | 3000 (Nuxt SSR) |
| **Backend port** | 8000 (Django/Gunicorn) |
| **Web server** | Nginx (reverse proxy) |

### Deploy yo'riqnomasi (Frontend)
```bash
# 1. Serverga ulanish
ssh root@46.224.219.146

# 2. Loyihani serverga yuklash
cd /www/wwwroot/
git clone <repo-url> andijon-ssv
cd andijon-ssv

# 3. Node.js o'rnatish (agar yo'q bo'lsa)
curl -fsSL https://deb.nodesource.com/setup_20.x | bash -
apt-get install -y nodejs

# 4. Paketlarni o'rnatish va build
npm install
npm run build

# 5. PM2 bilan ishga tushirish
npm install -g pm2
pm2 start .output/server/index.mjs --name andijon-ssb
pm2 save
pm2 startup

# 6. Nginx konfiguratsiya
# /etc/nginx/sites-available/andijon-ssb.conf -> port 3000 ga reverse proxy
```

---

## 🐍 Backend strukturasi (Django — 2-bosqich)

### Server ma'lumotlari
| Parametr | Qiymat |
|---|---|
| **Python** | 3.11+ |
| **Django** | 5.x |
| **DRF** | Django REST Framework |
| **WSGI** | Gunicorn |
| **Port** | 8000 |

### PostgreSQL ma'lumotlari
| Parametr | Qiymat |
|---|---|
| **Host** | localhost (127.0.0.1) |
| **Port** | 5432 |
| **Database nomi** | andijon_ssb_db |
| **User** | postgres |
| **Root password** | `admin123` |
| **Encoding** | UTF-8 |

### Django loyiha strukturasi
```
backend/
├── manage.py
├── requirements.txt
├── .env                          # SECRET_KEY, DB credentials
├── config/                       # Asosiy konfiguratsiya
│   ├── __init__.py
│   ├── settings/
│   │   ├── __init__.py
│   │   ├── base.py               # Umumiy sozlamalar
│   │   ├── development.py        # Dev sozlamalar
│   │   └── production.py         # Prod sozlamalar (xavfsiz)
│   ├── urls.py                   # Asosiy URL routing
│   ├── wsgi.py
│   └── asgi.py
├── apps/
│   ├── core/                     # Umumiy ma'lumotlar (tashkilot info)
│   │   ├── models.py             # SiteConfig, GeneralInfo
│   │   ├── serializers.py
│   │   ├── views.py
│   │   └── admin.py
│   ├── leadership/               # Rahbariyat
│   │   ├── models.py             # Leader, Position
│   │   ├── serializers.py
│   │   ├── views.py
│   │   └── admin.py
│   ├── structure/                # Tashkiliy tuzilma
│   │   ├── models.py             # Department, Division
│   │   ├── serializers.py
│   │   ├── views.py
│   │   └── admin.py
│   ├── documents/                # Normativ-huquqiy hujjatlar
│   │   ├── models.py             # Document, DocumentCategory
│   │   ├── serializers.py
│   │   ├── views.py
│   │   └── admin.py
│   ├── news/                     # Yangiliklar
│   │   ├── models.py             # News, Event, Announcement
│   │   ├── serializers.py
│   │   ├── views.py
│   │   └── admin.py
│   └── contact/                  # Aloqa va murojaatlar
│       ├── models.py             # ContactMessage, Appeal
│       ├── serializers.py
│       ├── views.py
│       └── admin.py
├── media/                        # Yuklangan fayllar
└── static/                       # Statik fayllar
```

### API endpointlar
```
GET  /api/v1/info/              — Tashkilot umumiy ma'lumotlari
GET  /api/v1/leaders/           — Rahbariyat ro'yxati
GET  /api/v1/structure/         — Tashkiliy tuzilma
GET  /api/v1/documents/         — Hujjatlar ro'yxati
GET  /api/v1/news/              — Yangiliklar
GET  /api/v1/news/:id/          — Bitta yangilik
POST /api/v1/contact/           — Murojaat yuborish
GET  /api/v1/stats/             — Statistika
```

### Django .env fayli namunasi
```env
SECRET_KEY=<random-secret-key-bu-yerda>
DEBUG=False
ALLOWED_HOSTS=46.224.219.146,localhost
DATABASE_URL=postgres://postgres:admin123@localhost:5432/andijon_ssb_db
CORS_ALLOWED_ORIGINS=http://46.224.219.146,http://localhost:3000
```

### Backend deploy yo'riqnomasi
```bash
# 1. Python virtual env
cd /www/wwwroot/andijon-ssv/backend
python3 -m venv venv
source venv/bin/activate

# 2. Paketlar o'rnatish
pip install -r requirements.txt

# 3. PostgreSQL baza yaratish
sudo -u postgres psql
CREATE DATABASE andijon_ssb_db;
ALTER USER postgres PASSWORD 'admin123';
\q

# 4. Migratsiya
python manage.py migrate
python manage.py createsuperuser

# 5. Gunicorn bilan ishga tushirish
gunicorn config.wsgi:application --bind 0.0.0.0:8000 --workers 3

# 6. PM2 bilan daemonize qilish
pm2 start "gunicorn config.wsgi:application --bind 0.0.0.0:8000 --workers 3" --name andijon-ssb-api
```

---

> **Muhim eslatma:** Bu loyiha O'zbekiston Respublikasi sog'liqni saqlash vazirligi standartlariga mos ravishda yaratiladi. Gov.uz platformasi bilan integratsiya 2-bosqichda amalga oshiriladi.

> **Boshqa AI uchun:** Agar siz bu loyihani davom ettirayotgan bo'lsangiz, avval `PROJECT_PLAN.md` ni to'liq o'qing. Frontend Nuxt.js 3 + Tailwind CSS da, Backend Django + PostgreSQL da. Server: `ssh root@46.224.219.146` (password: `12345-inforte`). PostgreSQL root password: `admin123`.
