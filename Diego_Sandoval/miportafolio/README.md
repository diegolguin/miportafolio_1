 Descripción 

Proyecto de portafolio desarrollado con Django 5.2.5, que incluye ejemplos de rutas, vistas y plantillas. Está configurado para funcionar tanto en local con SQLite como en Railway con PostgreSQL. 

🚀 Ejecución en Local 

1. Clonar el repositorio 

git clone https://github.com/diegolguin/miportafolio_1.git 

cd miportafolio_1/Diego_Sandoval 

2. Crear entorno virtual (opcional pero recomendado) 

python -m venv venv 

.\venv\Scripts\activate   # En Windows 

source venv/bin/activate  # En Linux/Mac 

3. Instalar dependencias 

pip install -r requirements.txt 

4. Migrar la base de datos 

python manage.py migrate 

5. (Opcional) Crear superusuario para el panel admin 

python manage.py createsuperuser 

6. Levantar el servidor 

python manage.py runserver 

Abrir en navegador 👉 http://127.0.0.1:8000 

🌐 Ejecución en Railway 

1. Archivos importantes 

- Procfile → indica cómo iniciar el servidor con Gunicorn. 

- requirements.txt → lista de dependencias necesarias. 

- settings.py → configurado para usar SQLite en local y PostgreSQL en Railway con dj-database-url. 

2. Deploy 

Conectar Railway con GitHub. 

Crear un proyecto en Railway y desplegar desde este repo. 

3. Migraciones en Railway 

python manage.py migrate 

python manage.py createsuperuser 

4. Acceso 

Abrir la URL pública que entrega Railway, por ejemplo: 

https://miportafolio-production.up.railway.app 

🛠 Tecnologías utilizadas 

- Python 3.13.5 

- Django 5.2.5 

- Gunicorn 

- WhiteNoise (archivos estáticos en producción) 

- PostgreSQL (en Railway) / SQLite (en local) 

-------------------------------------------------------------
AUTOR
-------------------------------------------------------------
Diego Sandoval
Estudiante Analista Programador - INACAP