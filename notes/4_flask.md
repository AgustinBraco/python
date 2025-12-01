## Crear proyecto desde cero

1. Instalar python3, venv, pip
   `sudo apt install -y python3 python3-venv python3-pip`
2. Dentro del proyecto, crear entorno virtual
   `python3 -m venv .venv`
3. Activar entorno virtual
   `source .venv/bin/activate`
4. Instalar dependencias
   `pip install flask dotenv gunicorn`
5. Estructura

   ```python
   proyecto/
   ├─ app.py
   ├─ requirements.txt
   ├─ templates/
   │  └─ index.html
   └─ .gitignore
   ```

6. Configurar `.gitignore`:

   ```python
   .venv/
   venv/
   env/
   .venv
   .env
   __pycache__/
   pycache/
   *.pyc
   db.sqlite3
   *.sqlite3
   *.log
   /staticfiles/
   /media/
   .vscode/
   .DS_Store
   EOF
   ```

7. Configurar `app.py` e `index.html`:

   ```python
   from flask import Flask, render_template

   app = Flask(__name__)

   @app.route("/")
   def home():
       return render_template("index.html")

   if __name__ == "__main__":
       app.run(debug=True)

   -----

   <!DOCTYPE html>
   <html lang="es">
     <head>
       <meta charset="utf-8" />
       <title>Test</title>
     </head>
     <body>
       <h1>Bienvenido</h1>
     </body>
   </html>

   ```

8. Correr servidor
   `python app.py`
9. Desactivar entorno virtual
   `deactivate`

---

## Dotenv

1. Crear archivo `.env`:

   ```python
   SECRET='...'
   ```

2. Uso:

   ```python
   from dotenv import load_dotenv
   import os
   load_dotenv()
   SECRET = os.environ.get("SECRET")
   ```

---

## Deploy (Render)

1. Crear archivo `Procfile`:

   ```python
   web: gunicorn app:app
   ```

2. Configurar Render (web service):
   1. Build command: `pip install -r requirements.txt`
   2. Start command: `gunicorn app:app`

---

## LDAP

Instalar dependencias

`flask ldap3`

---
