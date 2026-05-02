#!/bin/bash
# ============================================================
#  Andijon SSB — One-Click Installer
#  Yangi serverga to'liq o'rnatish skripti
#  Foydalanish: bash install.sh
# ============================================================

set -e

# Ranglar
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
BOLD='\033[1m'
NC='\033[0m'

info()    { echo -e "${BLUE}[INFO]${NC} $1"; }
success() { echo -e "${GREEN}[OK]${NC} $1"; }
warn()    { echo -e "${YELLOW}[WARN]${NC} $1"; }
error()   { echo -e "${RED}[ERROR]${NC} $1"; exit 1; }
step()    { echo -e "\n${BOLD}${CYAN}▶ $1${NC}"; }

# ============================================================
# Banner
# ============================================================
echo -e "${CYAN}"
echo "╔══════════════════════════════════════════════════════╗"
echo "║     Andijon SSB — Veb-sayt o'rnatuvchi               ║"
echo "║     Versiya: 1.0                                     ║"
echo "╚══════════════════════════════════════════════════════╝"
echo -e "${NC}"

# Root tekshirish
if [ "$EUID" -ne 0 ]; then
  error "Skriptni root sifatida ishga tushiring: sudo bash install.sh"
fi

# ============================================================
# Konfiguratsiya so'rash
# ============================================================
step "Konfiguratsiya"

read -p "Server IP manzili (masalan: 46.224.219.146): " SERVER_IP
SERVER_IP=${SERVER_IP:-"localhost"}

read -p "Domen nomi (bo'sh qoldiring agar yo'q bo'lsa): " DOMAIN_NAME

read -p "Loyiha GitHub/Git URL (masalan: https://github.com/user/repo): " REPO_URL
if [ -z "$REPO_URL" ]; then
  error "Git URL kiritilishi shart!"
fi

read -p "PostgreSQL parol (bo'sh = admin123): " PG_PASSWORD
PG_PASSWORD=${PG_PASSWORD:-"admin123"}

read -p "Django SECRET_KEY (bo'sh = avtomatik): " DJANGO_SECRET
if [ -z "$DJANGO_SECRET" ]; then
  DJANGO_SECRET=$(python3 -c "import secrets; print(secrets.token_urlsafe(50))" 2>/dev/null || openssl rand -base64 50 | tr -dc 'a-zA-Z0-9' | head -c 50)
fi

read -p "Admin username (default: admin): " ADMIN_USER
ADMIN_USER=${ADMIN_USER:-"admin"}

read -p "Admin email: " ADMIN_EMAIL
ADMIN_EMAIL=${ADMIN_EMAIL:-"admin@example.com"}

read -p "Admin parol: " ADMIN_PASS
if [ -z "$ADMIN_PASS" ]; then
  error "Admin paroli kiritilishi shart!"
fi

# Asosiy o'zgaruvchilar
INSTALL_DIR="/www/wwwroot/andijon-ssv"
DB_NAME="andijon_ssb_db"
DB_USER="postgres"
BACKEND_PORT=8000
FRONTEND_PORT=3000

if [ -n "$DOMAIN_NAME" ]; then
  ALLOWED_HOSTS="${SERVER_IP},${DOMAIN_NAME},localhost"
  CORS_ORIGINS="http://${SERVER_IP},http://${DOMAIN_NAME},https://${DOMAIN_NAME}"
else
  ALLOWED_HOSTS="${SERVER_IP},localhost"
  CORS_ORIGINS="http://${SERVER_IP},http://localhost:${FRONTEND_PORT}"
fi

echo -e "\n${BOLD}Konfiguratsiya:${NC}"
echo "  Server IP:    $SERVER_IP"
echo "  Domen:        ${DOMAIN_NAME:-'Yo\'q'}"
echo "  O'rnatish:    $INSTALL_DIR"
echo "  DB:           $DB_NAME"
echo "  Admin:        $ADMIN_USER"

read -p $'\nDavom etasizmi? (y/N): ' CONFIRM
if [[ ! "$CONFIRM" =~ ^[Yy]$ ]]; then
  echo "Bekor qilindi."
  exit 0
fi

# ============================================================
# Tizim paketlarini yangilash
# ============================================================
step "Tizim yangilanmoqda"
apt-get update -qq
apt-get install -y -qq curl wget git nginx postgresql postgresql-contrib python3 python3-pip python3-venv build-essential libpq-dev
success "Paketlar o'rnatildi"

# ============================================================
# Node.js o'rnatish (v20)
# ============================================================
step "Node.js o'rnatilmoqda"
if ! command -v node &>/dev/null || [[ $(node -v | cut -d. -f1 | tr -d 'v') -lt 18 ]]; then
  curl -fsSL https://deb.nodesource.com/setup_20.x | bash -
  apt-get install -y nodejs
  success "Node.js $(node -v) o'rnatildi"
else
  success "Node.js $(node -v) mavjud"
fi

# ============================================================
# PM2 o'rnatish
# ============================================================
step "PM2 o'rnatilmoqda"
if ! command -v pm2 &>/dev/null; then
  npm install -g pm2 -q
  success "PM2 o'rnatildi"
else
  success "PM2 mavjud"
fi

# ============================================================
# Loyihani klonlash
# ============================================================
step "Loyiha yuklanmoqda"
if [ -d "$INSTALL_DIR" ]; then
  warn "$INSTALL_DIR mavjud. Yangilanmoqda..."
  cd "$INSTALL_DIR"
  git pull
else
  mkdir -p "$(dirname $INSTALL_DIR)"
  git clone "$REPO_URL" "$INSTALL_DIR"
fi
success "Loyiha: $INSTALL_DIR"

# ============================================================
# PostgreSQL sozlash
# ============================================================
step "PostgreSQL sozlanmoqda"
systemctl start postgresql
systemctl enable postgresql

sudo -u postgres psql <<SQL
DO \$\$
BEGIN
  IF NOT EXISTS (SELECT FROM pg_database WHERE datname = '${DB_NAME}') THEN
    CREATE DATABASE ${DB_NAME};
  END IF;
END
\$\$;
ALTER USER ${DB_USER} PASSWORD '${PG_PASSWORD}';
GRANT ALL PRIVILEGES ON DATABASE ${DB_NAME} TO ${DB_USER};
SQL
success "PostgreSQL: $DB_NAME bazasi tayyor"

# ============================================================
# Backend (Django) sozlash
# ============================================================
step "Backend sozlanmoqda"
cd "$INSTALL_DIR/backend"

# Virtual environment
python3 -m venv venv
source venv/bin/activate

# Paketlarni o'rnatish
pip install -q -r requirements.txt

# .env fayl yaratish
cat > .env <<ENV
SECRET_KEY=${DJANGO_SECRET}
DEBUG=False
ALLOWED_HOSTS=${ALLOWED_HOSTS}
DATABASE_URL=postgres://${DB_USER}:${PG_PASSWORD}@localhost:5432/${DB_NAME}
CORS_ALLOWED_ORIGINS=${CORS_ORIGINS}
MEDIA_URL=/media/
ENV

# Migrations
python manage.py migrate --no-input

# Superuser
echo "from django.contrib.auth import get_user_model; U=get_user_model(); U.objects.filter(username='${ADMIN_USER}').exists() or U.objects.create_superuser('${ADMIN_USER}', '${ADMIN_EMAIL}', '${ADMIN_PASS}')" | python manage.py shell

# Static files
python manage.py collectstatic --no-input -v 0

deactivate
success "Backend tayyor"

# ============================================================
# Frontend (Nuxt.js) sozlash
# ============================================================
step "Frontend sozlanmoqda"
cd "$INSTALL_DIR"

# API URL ni sozlash
if [ -n "$DOMAIN_NAME" ]; then
  API_BASE_URL="https://${DOMAIN_NAME}/api/v1"
else
  API_BASE_URL="http://${SERVER_IP}/api/v1"
fi

cat > .env <<FENV
API_BASE_URL=${API_BASE_URL}
FENV

# Paketlar o'rnatish va build
npm install --quiet
npm run build

success "Frontend build tayyor"

# ============================================================
# PM2 bilan ishga tushirish
# ============================================================
step "PM2 bilan ishga tushirilmoqda"

# Avvalgi jarayonlarni to'xtatish
pm2 delete andijon-ssb-api 2>/dev/null || true
pm2 delete andijon-ssb-web 2>/dev/null || true

# Backend (Gunicorn)
cd "$INSTALL_DIR/backend"
pm2 start "venv/bin/gunicorn config.wsgi:application --bind 127.0.0.1:${BACKEND_PORT} --workers 3 --timeout 120" \
  --name andijon-ssb-api \
  --cwd "$INSTALL_DIR/backend"

# Frontend (Nuxt SSR)
pm2 start "$INSTALL_DIR/.output/server/index.mjs" \
  --name andijon-ssb-web \
  --env production \
  -- --port $FRONTEND_PORT

pm2 save
pm2 startup | tail -1 | bash 2>/dev/null || true
success "PM2 jarayonlari ishga tushdi"

# ============================================================
# Nginx sozlash
# ============================================================
step "Nginx sozlanmoqda"

NGINX_CONF="/etc/nginx/sites-available/andijon-ssb"

if [ -n "$DOMAIN_NAME" ]; then
  SERVER_NAME="$DOMAIN_NAME www.$DOMAIN_NAME $SERVER_IP"
else
  SERVER_NAME="$SERVER_IP"
fi

cat > "$NGINX_CONF" <<NGINX
# Andijon SSB — Nginx konfiguratsiya
# Avtomatik yaratildi: $(date)

upstream nuxt_backend {
  server 127.0.0.1:${FRONTEND_PORT};
}

upstream django_api {
  server 127.0.0.1:${BACKEND_PORT};
}

# Rate limiting
limit_req_zone \$binary_remote_addr zone=api:10m rate=20r/s;
limit_req_zone \$binary_remote_addr zone=contact:10m rate=5r/m;

server {
  listen 80;
  server_name ${SERVER_NAME};
  client_max_body_size 50m;

  # Security headers
  add_header X-Frame-Options "SAMEORIGIN" always;
  add_header X-Content-Type-Options "nosniff" always;
  add_header X-XSS-Protection "1; mode=block" always;
  add_header Referrer-Policy "strict-origin-when-cross-origin" always;

  # Django Admin
  location /admin/ {
    proxy_pass http://django_api;
    proxy_set_header Host \$host;
    proxy_set_header X-Real-IP \$remote_addr;
    proxy_set_header X-Forwarded-For \$proxy_add_x_forwarded_for;
    proxy_set_header X-Forwarded-Proto \$scheme;
    limit_req zone=api burst=10 nodelay;
  }

  # Django API
  location /api/ {
    proxy_pass http://django_api;
    proxy_set_header Host \$host;
    proxy_set_header X-Real-IP \$remote_addr;
    proxy_set_header X-Forwarded-For \$proxy_add_x_forwarded_for;
    proxy_set_header X-Forwarded-Proto \$scheme;
    limit_req zone=api burst=30 nodelay;
  }

  # Contact - rate limited
  location /api/v1/contact/ {
    proxy_pass http://django_api;
    proxy_set_header Host \$host;
    limit_req zone=contact burst=3 nodelay;
  }

  # Media fayllar (Django)
  location /media/ {
    alias ${INSTALL_DIR}/backend/media/;
    expires 30d;
    add_header Cache-Control "public, immutable";
  }

  # Static fayllar (Django admin)
  location /static/ {
    alias ${INSTALL_DIR}/backend/staticfiles/;
    expires 30d;
    add_header Cache-Control "public, immutable";
  }

  # Nuxt frontend
  location / {
    proxy_pass http://nuxt_backend;
    proxy_set_header Host \$host;
    proxy_set_header X-Real-IP \$remote_addr;
    proxy_set_header X-Forwarded-For \$proxy_add_x_forwarded_for;
    proxy_set_header X-Forwarded-Proto \$scheme;
    proxy_http_version 1.1;
    proxy_set_header Upgrade \$http_upgrade;
    proxy_set_header Connection 'upgrade';
    proxy_cache_bypass \$http_upgrade;
    proxy_read_timeout 60;
  }
}
NGINX

# Sites-enabled ga bog'lash
ln -sf "$NGINX_CONF" /etc/nginx/sites-enabled/andijon-ssb
rm -f /etc/nginx/sites-enabled/default 2>/dev/null || true

# Nginx test va qayta ishga tushirish
nginx -t && systemctl reload nginx
success "Nginx sozlandi"

# ============================================================
# Yakuniy tekshiruv
# ============================================================
step "Tekshiruv"
sleep 2

BACKEND_STATUS=$(curl -s -o /dev/null -w "%{http_code}" "http://127.0.0.1:${BACKEND_PORT}/api/v1/info/" 2>/dev/null || echo "000")
FRONTEND_STATUS=$(curl -s -o /dev/null -w "%{http_code}" "http://127.0.0.1:${FRONTEND_PORT}" 2>/dev/null || echo "000")

echo ""
echo -e "${BOLD}╔══════════════════════════════════════════════╗${NC}"
echo -e "${BOLD}║           O'rnatish yakunlandi!              ║${NC}"
echo -e "${BOLD}╚══════════════════════════════════════════════╝${NC}"
echo ""
echo -e "  ${GREEN}Sayt:${NC}         http://${SERVER_IP}"
echo -e "  ${GREEN}Admin panel:${NC}  http://${SERVER_IP}/admin/"
echo -e "  ${GREEN}API:${NC}          http://${SERVER_IP}/api/v1/"
echo ""
echo -e "  ${GREEN}Admin login:${NC}  ${ADMIN_USER}"
echo -e "  ${GREEN}Admin parol:${NC}  ${ADMIN_PASS}"
echo ""

if [ "$BACKEND_STATUS" == "200" ]; then
  echo -e "  ${GREEN}✓ Backend:${NC}  Ishlayapti"
else
  echo -e "  ${YELLOW}? Backend:${NC}  Javob kodi: $BACKEND_STATUS (tekshiring: pm2 logs andijon-ssb-api)"
fi

if [ "$FRONTEND_STATUS" == "200" ] || [ "$FRONTEND_STATUS" == "301" ]; then
  echo -e "  ${GREEN}✓ Frontend:${NC} Ishlayapti"
else
  echo -e "  ${YELLOW}? Frontend:${NC} Javob kodi: $FRONTEND_STATUS (tekshiring: pm2 logs andijon-ssb-web)"
fi

echo ""
echo -e "  ${CYAN}Foydali buyruqlar:${NC}"
echo "  pm2 status                 — jarayonlar holati"
echo "  pm2 logs andijon-ssb-api   — backend logs"
echo "  pm2 logs andijon-ssb-web   — frontend logs"
echo "  nginx -t && nginx -s reload — nginx qayta yuklash"
echo ""

if [ -n "$DOMAIN_NAME" ]; then
  echo -e "  ${YELLOW}SSL uchun:${NC} apt install certbot python3-certbot-nginx -y"
  echo "  certbot --nginx -d ${DOMAIN_NAME} -d www.${DOMAIN_NAME}"
  echo ""
fi
