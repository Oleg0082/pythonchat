from flask import Flask
import json
from flask_cors import CORS

aplicacion = Flask(__name__)
CORS(aplicacion)

mensajes = []

@aplicacion.route('/')
def inicio():
    global mensajes
    mensajes.append("Hola")
    return json.dumps(mensajes)

@aplicacion.route('/recibe')
def recibe():
    global mensajes
    mensajes.append("Hola")
    return json.dumps(mensajes)

if __name__ == '__main__':
    aplicacion.run(debug=True, port=3000)
