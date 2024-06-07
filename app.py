#vamos a crear un minijuego de piedra papel o tijera, donde podra jugar contra la maquina


#Importamos la libreria random, que nos permite generar numeros aleatorios
import random
from flask import Flask, request, render_template # type: ignore

app = Flask(__name__)

@app.route('/')

def jugar():
    #Vamos a crear una lista con las opciones del juego
    opciones = ['piedra', 'papel', 'tijera']
    #Vamos a generar un numero aleatorio entre 0 y 2
    num = random.randint(0, 2)
    #Vamos a guardar la opcion de la maquina
    maquina = opciones[num]
    #Vamos a guardar la opcion del usuario
    usuario = request.args.get('opcion')
    #Vamos a crear una variable que nos permita guardar el resultado del juego
    resultado = ''
    #Vamos a comparar las opciones del usuario y de la maquina
    if usuario == maquina:
        resultado = 'Empate'
    elif usuario == 'piedra' and maquina == 'tijera':
        resultado = 'Ganaste'
    elif usuario == 'tijera' and maquina == 'papel':
        resultado = 'Ganaste'
    elif usuario == 'papel' and maquina == 'piedra':
        resultado = 'Ganaste'
    else:
        resultado = 'Perdiste'
    #Vamos a mostrar la opcion de la maquina
    return f'Maquina: {maquina}, Usuario: {usuario}, Resultado: {resultado}'

@app.route('/')
def index():
    return render_template('index.html')

#Vamos a ejecutar la aplicacion
if __name__ == '__main__':
    app.run(debug=True)
  comandos para subirlo a github
    git init
    git add .
    git commit -m "primer commit"
    git remote add origin
    
