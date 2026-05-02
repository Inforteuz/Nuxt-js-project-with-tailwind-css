import paramiko
import time

def run_ssh_command(ssh, command):
    print(f"Running: {command}")
    stdin, stdout, stderr = ssh.exec_command(command)
    exit_status = stdout.channel.recv_exit_status()
    out = stdout.read().decode('utf-8')
    err = stderr.read().decode('utf-8')
    if out: print(out.strip())
    if err: print("ERROR: " + err.strip())
    return exit_status, out, err

try:
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    print("Connecting to 46.224.219.146...")
    ssh.connect('46.224.219.146', username='root', password='12345-inforte')
    
    print("\n--- DEPLOYING FRONTEND ---")
    run_ssh_command(ssh, "cd /www/wwwroot/andijon-ssv && git reset --hard HEAD && git pull origin main")
    run_ssh_command(ssh, "cd /www/wwwroot/andijon-ssv && npm install")
    # Set the apiBase explicitly for production
    run_ssh_command(ssh, "cd /www/wwwroot/andijon-ssv && echo 'NUXT_PUBLIC_API_BASE=http://46.224.219.146:8000/api/v1' > .env")
    run_ssh_command(ssh, "cd /www/wwwroot/andijon-ssv && npm run build")
    
    # Restart PM2
    run_ssh_command(ssh, "pm2 restart andijon-ssb || (cd /www/wwwroot/andijon-ssv && pm2 start .output/server/index.mjs --name andijon-ssb)")
    run_ssh_command(ssh, "pm2 save")

    print("\n--- SETTING UP BACKEND ---")
    run_ssh_command(ssh, "apt-get update && apt-get install -y python3-pip python3-venv postgresql postgresql-contrib nginx curl")
    
    # Create DB if not exists
    db_setup_cmd = """sudo -u postgres psql -tAc "SELECT 1 FROM pg_roles WHERE rolname='postgres'" | grep -q 1 || sudo -u postgres psql -c "ALTER USER postgres PASSWORD 'admin123';"
sudo -u postgres psql -tAc "SELECT 1 FROM pg_database WHERE datname='andijon_ssb_db'" | grep -q 1 || sudo -u postgres psql -c "CREATE DATABASE andijon_ssb_db;"
"""
    run_ssh_command(ssh, db_setup_cmd)

    # Setup Backend Python Environment
    run_ssh_command(ssh, "cd /www/wwwroot/andijon-ssv/backend && python3 -m venv venv")
    run_ssh_command(ssh, "cd /www/wwwroot/andijon-ssv/backend && ./venv/bin/pip install -r requirements.txt")
    run_ssh_command(ssh, "cd /www/wwwroot/andijon-ssv/backend && ./venv/bin/pip install gunicorn psycopg2-binary")
    
    # Setup .env for Backend
    env_content = """SECRET_KEY=dj-secret-key-deploy-12345
DEBUG=True
ALLOWED_HOSTS=46.224.219.146,localhost,127.0.0.1
DATABASE_URL=postgres://postgres:admin123@localhost:5432/andijon_ssb_db
CORS_ALLOWED_ORIGINS=http://46.224.219.146,http://localhost:3000,http://46.224.219.146:3000
"""
    run_ssh_command(ssh, f"cat << 'ENVEOF' > /www/wwwroot/andijon-ssv/backend/.env\n{env_content}\nENVEOF")

    # Migrate and create superuser
    run_ssh_command(ssh, "cd /www/wwwroot/andijon-ssv/backend && ./venv/bin/python manage.py makemigrations")
    run_ssh_command(ssh, "cd /www/wwwroot/andijon-ssv/backend && ./venv/bin/python manage.py migrate")
    
    # We will create superuser using a script so it doesn't prompt
    su_script = """
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.base')
django.setup()
from django.contrib.auth.models import User
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
"""
    run_ssh_command(ssh, f"cat << 'SUEOF' > /www/wwwroot/andijon-ssv/backend/create_su.py\n{su_script}\nSUEOF")
    run_ssh_command(ssh, "cd /www/wwwroot/andijon-ssv/backend && ./venv/bin/python create_su.py")

    # Collect static
    run_ssh_command(ssh, "cd /www/wwwroot/andijon-ssv/backend && ./venv/bin/python manage.py collectstatic --noinput")

    # Start Backend with PM2
    run_ssh_command(ssh, "pm2 delete andijon-ssb-api || true")
    run_ssh_command(ssh, "cd /www/wwwroot/andijon-ssv/backend && pm2 start './venv/bin/gunicorn config.wsgi:application --bind 0.0.0.0:8000 --workers 3' --name andijon-ssb-api")
    run_ssh_command(ssh, "pm2 save")

    print("\n✅ DEPLOYMENT FINISHED SUCCESSFULLY!")
    
except Exception as e:
    print(f"Deployment failed: {e}")
finally:
    ssh.close()
