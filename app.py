from flask import Flask
app = Flask(__name__)

@app.route('/')
def hola_mundo():
    return '¡Hola! Esta app está corriendo dentro de un contenedor Docker.'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
