from flask import Flask
from vistas import registrar_rutas

app = Flask(__name__)
registrar_rutas(app)

if __name__ == "__main__":
    app.run(debug=True)