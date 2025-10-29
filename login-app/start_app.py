import subprocess
import webbrowser
import time

def is_docker_running():
    """Verifica si Docker está corriendo."""
    try:
        subprocess.run(["docker", "info"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
        return True
    except subprocess.CalledProcessError:
        return False

def run_docker_compose():
    """Ejecuta docker compose up -d de forma segura."""
    if not is_docker_running():
        print("❌ Docker no está corriendo. Por favor, inícialo primero.")
        exit(1)

    try:
        print("🧱 Iniciando contenedores con Docker Compose...")
        subprocess.run(["docker", "compose", "up", "-d"], check=True)
        print("✅ Contenedores iniciados correctamente.")
    except subprocess.CalledProcessError:
        print("❌ Error al iniciar Docker Compose.")
        exit(1)

def open_browser(url="http://127.0.0.1:8080"):
    """Abre el navegador predeterminado de forma multiplataforma."""
    print("🌐 Esperando que el frontend esté disponible...")
    time.sleep(5)
    print(f"🚀 Abriendo navegador en {url} ...")
    webbrowser.open(url)

def main():
    print("🚢 === Lanzando Login App Docker ===")
    run_docker_compose()
    open_browser()

if __name__ == "__main__":
    main()
