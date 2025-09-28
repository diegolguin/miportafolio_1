📂 Proyecto Portafolio – Django 

📖 Descripción 

Proyecto de portafolio desarrollado con Django 5.2.5, que incluye ejemplos de rutas, vistas y plantillas. Está configurado para funcionar tanto en local con SQLite como en Railway con PostgreSQL. 

🚀 Ejecución en Local 

Clonar el repositorio: 
 git clone https://github.com/diegolguin/miportafolio_1.git 
 cd miportafolio_1/Diego_Sandoval 

Crear entorno virtual (opcional pero recomendado): 
 python -m venv venv 
 .\venv\Scripts\activate   # En Windows 
 source venv/bin/activate  # En Linux/Mac 

Instalar dependencias: 
 pip install -r requirements.txt 

Migrar la base de datos: 
 python manage.py migrate 

(Opcional) Crear superusuario: 
 python manage.py createsuperuser 

Levantar el servidor: 
 python manage.py runserver 
 Abrir en navegador 👉 http://127.0.0.1:8000 

🌐 Ejecución en Railway 

Archivos importantes: 

- Procfile → indica cómo iniciar el servidor con Gunicorn. 

- requirements.txt → lista de dependencias necesarias. 

- settings.py → configurado para usar SQLite en local y PostgreSQL en Railway con dj-database-url. 

 
Deploy: 

- Conectar Railway con GitHub. 

- Crear un proyecto en Railway y desplegar desde este repo. 

 
Migraciones en Railway: 

python manage.py migrate 

python manage.py createsuperuser 

 
Acceso a producción: 

👉https://miportafolio1-production-26c5.up.railway.app

🛠 Tecnologías utilizadas 

- Python 3.13.5 

- Django 5.2.5 

- Gunicorn 

- WhiteNoise (archivos estáticos en producción) 

- PostgreSQL (en Railway) / SQLite (en local) 

👨‍💻 Autor 

Diego Sandoval 
Estudiante Analista Programador – INACAP 