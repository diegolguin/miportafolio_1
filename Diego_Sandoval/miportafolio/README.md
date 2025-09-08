Este proyecto corresponde a la evaluación de Programación Back-End con Django.
Incluye la estructura de vistas, templates y rutas necesarias para ejecutarse correctamente.

-------------------------------------------------------------
INSTRUCCIONES PARA EJECUTAR EL PROYECTO LOCALMENTE
-------------------------------------------------------------
1. Clonar el repositorio desde GitHub:
   git clone https://github.com/diegolguin/miportafolio_1.git
   cd miportafolio_1

2. Crear un entorno virtual (opcional pero recomendado):
   python -m venv venv
   .\venv\Scripts\activate   (Windows)
   source venv/bin/activate    (Linux/Mac)

3. Instalar dependencias:
   pip install -r requirements.txt

4. Aplicar migraciones a la base de datos:
   python manage.py migrate

5. Ejecutar el servidor de desarrollo:
   python manage.py runserver

6. Abrir en el navegador el proyecto en el puerto por defecto (8000):
   http://127.0.0.1:8000/

   - Para acceder al panel de administración (si hay superusuario creado):
     http://127.0.0.1:8000/admin

-------------------------------------------------------------
ACCESO APLICACIÓN DESPLEGADA (Railway)
-------------------------------------------------------------
El proyecto también está desplegado en Railway para facilitar la revisión sin necesidad 
de instalar nada localmente. Puede acceder en el siguiente link:

👉 https://miportafolio1-production.up.railway.app/

-------------------------------------------------------------
NOTAS
-------------------------------------------------------------
- El puerto por defecto en local es el 8000.
- Railway gestiona automáticamente los puertos, por lo que solo se necesita el link.
- El proyecto fue preparado para demostrar conocimientos en:
  ✔️ Modelos y migraciones en Django
  ✔️ Vistas y rutas (urls.py)
  ✔️ Templates para mostrar contenido dinámico
  ✔️ Configuración de despliegue en un servidor real (Railway)

-------------------------------------------------------------
AUTOR
-------------------------------------------------------------
Diego Sandoval
Estudiante Analista Programador - INACAP