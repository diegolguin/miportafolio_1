Proyecto: Mi Portafolio (Django)

Cómo ejecutar en local:
1) Clonar el repositorio:
   git clone https://github.com/diegolguin/miportafolio_1.git
   cd miportafolio_1/Diego_Sandoval

2) Instalar dependencias:
   pip install -r requirements.txt

3) Migrar la base de datos:
   python manage.py migrate

4) (Opcional) Crear superusuario:
   python manage.py createsuperuser

5) Levantar el servidor:
   python manage.py runserver
   Abrir: http://127.0.0.1:8000/

Cómo ejecutar en Railway:
1) Railway usa Procfile y requirements.txt automáticamente.
2) Después del deploy, en la consola de Railway correr:
   python manage.py migrate
   python manage.py createsuperuser
3) Acceder desde la URL pública que entrega Railway.
