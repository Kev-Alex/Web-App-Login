#!/bin/bash
set -e

echo "🏗️ Creando base de datos de testing..."

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" <<-EOSQL
    CREATE USER webuser WITH PASSWORD 'webpass';
    GRANT ALL PRIVILEGES ON DATABASE login_db TO webuser;
    CREATE DATABASE login_test OWNER webuser;
    GRANT ALL PRIVILEGES ON DATABASE login_test TO webuser;
EOSQL

echo "✅ Bases de datos 'login_db' (predeterminada) y 'login_test' creadas correctamente."