from flask import Flask
import json

aplicacion = Flask(__name__)

mensajes = []

@aplicacion.route('/')
def inicio():
    global mensajes
    mensajes.append("Hola")
    return "Hola desde Flask y el contador es: "+str(mensajes)

@aplicacion.route('/recibe')
def recibe():
    global mensajes
    mensajes.append("Hola")
    return str(mensajes)

if __name__ == '__main__':
    aplicacion.run(debug=True, port=3000)
