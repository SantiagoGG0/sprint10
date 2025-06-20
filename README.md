# Clínica Veterinaria - Web App

## Requisitos

- Python 3.8+
- pip

## Instalación

1. Instala las dependencias:
   ```
   pip install -r requirements.txt
   ```

2. Realiza migraciones iniciales:
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```

3. Crea el superusuario:
   ```
   python manage.py createsuperuser
   ```

4. Corre el servidor de desarrollo:
   ```
   python manage.py runserver
   ```

5. Accede al panel de administración en `http://localhost:8000/admin/` con el usuario creado.

## Configuración de Base de datos

Por defecto usa SQLite3, no es necesaria configuración adicional.

## Funcionalidades

- Registrar y listar mascotas y propietarios en la interfaz web.
- Gestión total usando el panel de administración de Django.
