#!/usr/bin/env bash
# Script de build usado pelo Render.
set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate

# O db.sqlite3 não vai para o repositório, então o banco é recriado e
# populado com os dados de exemplo a cada deploy.
python manage.py seed

# Cria o superusuário a partir das variáveis de ambiente
# DJANGO_SUPERUSER_USERNAME, DJANGO_SUPERUSER_EMAIL e DJANGO_SUPERUSER_PASSWORD.
if [ -n "$DJANGO_SUPERUSER_USERNAME" ]; then
  python manage.py createsuperuser --no-input || true
fi
