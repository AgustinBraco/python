## Crear proyecto desde cero

1. Instalar python3, venv, pip
   `sudo apt install -y python3 python3-venv python3-pip`
2. Dentro del proyecto, crear entorno virtual
   `python3 -m venv .venv`
3. Activar entorno virtual
   `source .venv/bin/activate`
4. Instalar dependencias
   `pip install django dotenv`
5. Crear proyecto
   `django-admin startproject mysite .`
6. Migrar tablas base
   `python manage.py migrate`
7. Crear apps
   `python manage.py startapp name`
8. Generar migraciones
   `python manage.py makemigrations`
9. Aplicar migraciones
   `python manage.py migrate`
10. Crear super usuario
    `python manage.py createsuperuser`
11. Correr servidor
    `python manage.py runserver`
12. Desactivar entorno virtual
    `deactivate`

---

## Adicionales

1. Guardar dependencias con `pip freeze > requirements.txt`.

2. Crear archivo `.gitignore`:

```python
*.pyc
**pycache**/
venv/
env/
.venv
.env
*.sqlite3
db.sqlite3
*.log
/staticfiles/
/media/
.vscode/
.DS_Store
EOF
```

1. Crear archivo `.env`:

   ```python
   DJANGO_SECRET_KEY='django-insecure...'
   ```

2. Configurar `settings.py`:

   ```python
   [settings.py](http://settings.py/)
   -
   from dotenv import load_dotenv
   import os
   load_dotenv()
   SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY")
   ```

---

## Configuracion dentro del proyecto

1. Configurar apps:

   ```python
   project/project/apps/name/apps.py > name = 'apps.name'
   project/project/settings.py > INSTALLED_APPS = [..., 'apps.name']
   ```

2. Organizar apps:

   ```python
   DJANGO_APPS = ['django...']
   LOCAL_APPS = ['apps...']
   THIRD_PARTY_APPS = []
   INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS
   ```

3. Modelos:

   1. Crear:

   ```
   Class Materia(models.Model):
    nombre = models.CharField(max_length=255)

   Class Carrera(models.Model):
    nombre = models.CharField(max_length=255)
   ```

   b. Relacionar:

   ```python
   Class Materia(models.Model):
    nombre = models.CharField(max_length=255)
    carrera = models.ForeignKey('carrera.Carrera', on_delete=models.DO_NOTHING, null=True, related_name='materias')
   ```

   c. Manager:

   ```python
   Model.objects.all()
   Model.objects.first()
   Model.objects.last()
   Model.objects.filter(nombre="name")
   Model.objects.create(data)
   Model.objects.create(nombre="name", carrera=Carrera.objects.get(id=1))
   ```

   d. Admin:

   ```python
   from apps.carrera.models import Carrera

   # Registrar es mostrar en el panel de admin
   @admin.register(Carrera)
   class CategoryAdmin(admin.ModelAdminj):
    list_display = ('name', 'description')

   @admin.register(CategoryItem)
   class CategoryItem(admin.ModelAdmin):
    list_display = ('category', 'item')
   ```

4. Template view:

   ```python
   from django.views.generic import ListView

   class ItemTemplateView(ListView):
     template_name = "items.html"
     model = Item
     context_object_name = "items"
     ordering = ["-name"]
     paginate_by = 2
     queryset = Item.objects.filter(name__icontains="Type")

   from apps.item.views import ItemTemplateView
   ItemTemplateView.as_view()
     .../items/list/?page=2
   ```

---

## Deploy

1. Instalar dependencias:

   ```
   pip install whitenoise # Archivos estáticos
   pip install gunicorn # Servidor WSGI.
   ```

2. Configurar `settings.py`:

   ```
   STATIC_URL = "/static/"
   STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
   MIDDLEWARE: "whitenoise.middleware.WhiteNoiseMiddleware"
   STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
   ```

3. Crear script `create_superuser.py` para crear super usuario:

   ```
   import os
   import django
   from django.contrib.auth.models import User
   from dotenv import load_dotenv
   load_dotenv()
   USERNAME = os.environ.get("USERNAME")
   PASSWORD = os.environ.get("PASSWORD")
   EMAIL = os.environ.get("EMAIL")
   os.environ.setdefault("DJANGO_SETTINGS_MODULE", "helpdesk.settings")
   django.setup()
   if not User.objects.filter(username=USERNAME).exists():
       User.objects.create_superuser(
           username=USERNAME,
           email=EMAIL,
           password=PASSWORD,
       )
       print("Superuser created")
   else:
       print("Superuser already exist")
   ```

4. Configurar PaaS (Render):

   ```
   pip install -r requirements.txt && python manage.py collectstatic --noinput # Build Command
   python manage.py migrate && python create_superuser.py && gunicorn helpdesk.wsgi:application --bind 0.0.0.0:$PORT # Start command
   ```

5. Crear variables de entorno:

   ```
   DJANGO_SECRET_KEY
   HOST
   USERNAME
   PASSWORD
   EMAIL
   ```

6. Pushear.

---
