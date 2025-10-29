-- ===========================================
-- CREAR TABLA USERS EN LA BASE PRINCIPAL
-- ===========================================
\connect login_db

-- Habilitar extensión necesaria para crypt()
CREATE EXTENSION IF NOT EXISTS pgcrypto;

CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    full_name VARCHAR(255)
);

-- Insertar usuario administrador inicial
INSERT INTO users (email, password, full_name)
VALUES (
    'admin@example.com',
    crypt('admin', gen_salt('bf')),
    'Admin User'
)
ON CONFLICT (email) DO NOTHING;

\echo '✅ Usuario admin insertado correctamente en login_db';
