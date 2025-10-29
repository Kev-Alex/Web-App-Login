#!/usr/bin/env bash
set -euo pipefail
HOST="${HOST:-127.0.0.1}"
USER="${USER:-postgres}"
DB="${DB:-login_db}"
psql -h "$HOST" -U "$USER" -c "CREATE DATABASE $DB;"
psql -h "$HOST" -U "$USER" -d "$DB" -f ./db/db.sql
psql -h "$HOST" -U "$USER" -d "$DB" -f ./db/seed.sql
