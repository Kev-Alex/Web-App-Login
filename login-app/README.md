# 🚀 WebLogin (FastAPI + PostgreSQL + Nginx)

Aplicación full-stack minimalista con **FastAPI** (backend), **PostgreSQL** (base de datos) y **Nginx** (frontend estático + proxy inverso), totalmente **dockerizada**.

---

## ⚙️ Arranque rápido con Docker

Puedes iniciar la aplicación de dos maneras:

### 🧩 Opción 1 — Manual
```bash
cp .env.example .env
docker compose up -d --build
```

### ⚡ Opción 2 — Automática
Usa el script de inicio:
```bash
python start_app.py
```
> Este comando levantará los contenedores y abrirá automáticamente el navegador.

---

Luego abre tu navegador en:
👉 **http://127.0.0.1:8080**

Credenciales de prueba:
- 📧 `admin@example.com`
- 🔑 `admin`

---

## 🧱 Estructura de servicios

| Servicio   | Descripción                                    | Puerto local |
|-------------|------------------------------------------------|---------------|
| **frontend** | Sirve archivos estáticos y redirige `/api` al backend | 8080 |
| **backend**  | API REST desarrollada en FastAPI               | 8081 |
| **db**       | Base de datos PostgreSQL con datos iniciales (`seed.sql`) | 5432 |

---

## 🧰 Comandos útiles

Ver logs del backend:
```bash
docker compose logs -f backend
```

Reconstruir solo el backend:
```bash
docker compose up -d --build backend
```

Detener y limpiar contenedores:
```bash
docker compose down -v
```

---

## 🧾 Notas

- No es necesario tener **Python** ni **PostgreSQL** instalados localmente (solo **Docker**).
- El archivo `.env` contiene las variables de entorno del proyecto.
- El script `start_app.py` facilita el arranque y apertura automática del navegador.

---

📁 **Stack completo listo para desarrollo, pruebas o despliegue.**
