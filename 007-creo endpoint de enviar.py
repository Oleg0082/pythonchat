from flask import Flask, request
import json
from flask_cors import CORS

# Creo una nueva aplicación de Flask
aplicacion = Flask(__name__)
# LE añado soporte para aceptar conexiones externas
CORS(aplicacion)
# Creo una lista vacia de  mensajes
mensajes = []
# Ruta que atienda a la raiz del dominio
@aplicacion.route('/')
def inicio():
    return "ok"
# Ruta a la que se llama para recibir mensajes
@aplicacion.route('/recibe')
def recibe():
    # Traemos los mensajes a la funcion
    global mensajes
    # Devolvemos los mensajes como json
    return json.dumps(mensajes)
# Ruta la que se llama para enviar un mensaje
@aplicacion.route('/envia')
def envia():
    # Traemos los mensajes a la funcion
    global mensajes
    # A los mensajes les añadimos lo que venga por get
    mensajes.append(request.args.get('mensaje'))
    return True

if __name__ == '__main__':
    aplicacion.run(debug=True, port=3000)
