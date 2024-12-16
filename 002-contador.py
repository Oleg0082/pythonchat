from flask import Flask

aplicacion = Flask(__name__)

contador = 0

@aplicacion.route('/')
def inicio():
    global contador
    contador += 1
    return "Hola desde Flask y el contador es: "+str(contador)

if __name__ == '__main__':
    aplicacion.run(debug=True, port=3000)
