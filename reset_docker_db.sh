#!/usr/bin/env bash
# Wipes Postgres data and reapplies migrations. Required after CustomUser PK changed
# (old DB had user_id; new schema uses id). Run from project root on your Mac.
set -euo pipefail
cd "$(dirname "$0")"

echo "Stopping containers and removing the Postgres volume (pgdata)..."
docker compose down -v

echo "Starting stack..."
docker compose up -d --build

echo "Waiting for database..."
sleep 8

echo "Applying migrations..."
docker compose exec web python manage.py migrate

echo ""
echo "Done. Create an admin user:"
echo "  docker compose exec web python manage.py createsuperuser"
