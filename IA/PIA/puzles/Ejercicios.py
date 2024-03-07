import random
from typing import MutableMapping


def seleccion_numero():
    while True:
        try:
            numero_entrada = int(input("Introduce un numero: "))
            return numero_entrada
        except:
            print("Solo están permitidos números")

def adivina_numero():

    numero_a_adivinar = random.randrange(100)
    print(numero_a_adivinar)
    numero_entrada = seleccion_numero()
    while True:
        if numero_entrada == numero_a_adivinar:
            print("Has adivinado")
            break
        else:
            print("Prueba otra vez!!")
            numero_entrada = seleccion_numero()

## adivina_numero()

def adivina_numero_v2():

    numero_a_adivinar = int(input("Introduce un número para que el ordenador lo adivine entre el 0 y el 100: "))
    a = 0
    b = 100
    numero_entrada = random.randint(a,b)
    contador_intentos = 1
    while a != 100:
        if numero_entrada > numero_a_adivinar:
            print(numero_entrada,"->","El numero es menor")
            b = numero_entrada
            contador_intentos += 1
            numero_entrada = random.randint(a,b)
        elif numero_entrada < numero_a_adivinar:
            print(numero_entrada,"->","El numero es mayor")
            a = numero_entrada
            contador_intentos += 1
            numero_entrada = random.randint(a,b)
        else:
            print(numero_entrada,"->","Lo has conseguido!!")
            print("Numero de intentos: ",contador_intentos)
            break
        
## adivina_numero_v2()

def juego_ppt():

    victorias_usu = 0
    victorias_pc = 0
    empates = 0

    while True:
        opcion_usu = input("Escoge entre piedra, papel o tigera (Escribe 'salir' para terminar la partida): ")

        opciones = ["piedra","papel","tigera"]
        opcion_pc = random.choice(opciones)
        print("Ordenador: ", opcion_pc)
        
        '''
        if opcion_pc == opcion_usu:
            print("Empate")
        elif opcion_pc == "piedra": 
            if opcion_usu == "papel":
                print("Gana el usuario")
            elif opcion_usu == "tigera":
                print("Gana el ordenador")
        elif opcion_pc == "papel": 
            if opcion_usu == "piedra":
                print("Gana el ordenador")
            elif opcion_usu == "tigera":
                print("Gana el usuario")
        elif opcion_pc == "tigera": 
            if opcion_usu == "papel":
                print("Gana el ordenador")
            elif opcion_usu == "piedra":
                print("Gana el usuario")
        '''

        if opcion_usu == "salir":
            break
        elif opcion_pc == opcion_usu:
            print("Empate")
            empates += 1
        elif (opcion_pc == "piedra" and opcion_usu == "tigera") or (opcion_pc == "papel" and opcion_usu == "piedra") or (opcion_pc == "tigera" and opcion_usu == "papel"):
            print("Gana el ordenador")
            victorias_pc += 1
        else:
            print("Gana el usuario")
            victorias_usu += 1

    print("Resultado de la partida: \nUsuario:", victorias_usu, "\nOrdenador:",victorias_pc,"\nEmpates:",empates)

## juego_ppt()


'''
JUEGO DEL AJEDREZ    
'''

def posiciones(posicion):
        
        nueva_posicion = []

        for x in posicion:
            if x == "a":
                nueva_posicion.append(0)
            elif x == "b":
                nueva_posicion.append(1)
            elif x == "c" :
                nueva_posicion.append(2)
            elif x == "d":
                nueva_posicion.append(3)
            elif x == "e":
                nueva_posicion.append(4)
            elif x == "f":
                nueva_posicion.append(5)
            elif x == "g":
                nueva_posicion.append(6)
            elif x == "h":
                nueva_posicion.append(7)
            else:
                nueva_posicion.append(int(x)-1)
        
        return nueva_posicion


def generar_tablero():

    tablero = [["♜","♞","♝","♛","♚","♝","♞","♜"],
               ["♟","♟","♟","♟","♟","♟","♟","♟"],
               ["·","·","·","·","·","·","·","·"],
               ["·","·","·","·","·","·","·","·"],
               ["·","·","·","·","·","·","·","·"],
               ["·","·","·","·","·","·","·","·"],
               ["♙","♙","♙","♙","♙","♙","♙","♙"],
               ["♖","♘","♗","♔","♕","♗","♘","♖"],]


    return tablero

def jugadas(tablero):

    contador = 1
    marca_numerica = 8
    for x in range(len(tablero)):
        print(marca_numerica," ",end="")
        for y in range(len(tablero)):
            if contador == 8:
                print(tablero[x][y])
                contador = 0
            else:
                print(tablero[x][y],end=" ")
            contador += 1
        marca_numerica = marca_numerica - 1
    print("  ","A","B","C","D","E","F","G","H")


def partida_ajedrez():

    tablero = generar_tablero()

    while True:
        jugadas(tablero)
        pieza = input("Escoge la pieza que quieres mover: ")
        jugada = input("Posicion a la que se quiere mover: ")
        
        if (jugada == "salir" or pieza == "salir"):
            break

        pieza_posicion = posiciones(pieza)
        jugada_posicion = posiciones(jugada)

        print("Posicion de la pieza: ", pieza_posicion)
        print("Posicion de la jugada: ", jugada_posicion)
        
        tablero[7-jugada_posicion[0]][jugada_posicion[1]] = tablero[7-pieza_posicion[0]][pieza_posicion[1]]
        tablero[7-pieza_posicion[0]][pieza_posicion[1]] = "·"
        
##partida_ajedrez()


## JUEGO DEL AHORCADO

def palabras():
    lista_palabras = ["coche","casa","herramienta","paseo","pepinillo","informatica"]
    return random.choice(lista_palabras)

def printAhorcado(vida):
    print("")
    if vida == 5:
        print("+------+")
        print("|/")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
    elif vida == 4:
        print("+------+")
        print("|/     |")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
    elif vida == 3:
        print("+------+")
        print("|/     |")
        print("|      O")
        print("|")
        print("|")
        print("|")
        print("|")
    elif vida == 2:
        print("+------+")
        print("|/     |")
        print("|      O")
        print("|      |")
        print("|")
        print("|")
        print("|")
    elif vida == 1:
        print("+------+")
        print("|/     |")
        print("|      O")
        print("|     /|\\")
        print("|")
        print("|")
        print("|")
    elif vida == 0:
        print("+------+")
        print("|/     |")
        print("|      O")
        print("|     /|\\")
        print("|      |")
        print("|     / \\")
        print("|")        

def ahoracado():

    palabra = palabras()
    print(palabra)
    
    acertada = []
    for x in range(len(palabra)):
        acertada.append("_ ")

    letras_intentadas = []
    letra = ""

    vidas = 5

    while True:
        print("Palabra  a adivinar: ",end="")
        for x in range(len(palabra)):
            if letra == palabra[x]:
                acertada[x] = letra
            else:
                if (letra not in palabra) and (letras_intentadas.__contains__(letra) == False):
                    letras_intentadas.append(letra)
                    vidas -= 1

            print(acertada[x],end=" ")
            
        print("")
        print("Letras intentadas: ",end="")
        for x in range(len(letras_intentadas)):
            print(letras_intentadas[x],end=" ")
        printAhorcado(vidas)
        print("",end="\n\n")

        if acertada.__contains__("_ ") == False:
            break

        while True:
            letra = input("Escribe una letra: ")
            if letras_intentadas.__contains__(letra):
                print("Esa no pelotudo")
            else:
                break


    print("Lo lograste wey")

## ahoracado()

def laberinto():

    '''
    laberinto = [
        [' ', 'X', 'X', 'X', 'X'],
        [' ', 'X', ' ', ' ', ' '],
        [' ', 'X', ' ', 'X', ' '],
        [' ', ' ', ' ', 'X', ' '],
        ['X', 'X', 'X', 'X', ' ']
        ]
        
    laberinto = [
    [' ', 'X', 'X', 'X', 'X', 'X', 'X'],
    [' ', 'X', ' ', ' ', ' ', 'X', ' '],
    [' ', 'X', ' ', 'X', ' ', ' ', ' '],
    [' ', 'X', ' ', 'X', ' ', 'X', ' '],
    [' ', 'X', ' ', 'X', ' ', 'X', ' '],
    [' ', ' ', ' ', 'X', ' ', 'X', ' '],
    ['X', 'X', 'X', 'X', 'X', 'X', ' ']
    ]

    '''
    laberinto = [
        [' ', 'X', 'X', 'X', ' ', 'X', 'X'],
        [' ', 'X', ' ', ' ', ' ', 'X', 'X'],
        [' ', 'X', ' ', 'X', ' ', ' ', 'X'],
        [' ', 'X', ' ', 'X', ' ', 'X', 'X'],
        [' ', 'X', ' ', 'X', ' ', 'X', ' '],
        [' ', ' ', ' ', 'X', ' ', ' ', ' '],
        ['X', 'X', 'X', 'X', 'X', 'X', 'X']
    ]
    
    fila = 0
    columna = 0

    while True:

        print("Entra al while")
        print("Fila",fila)
        print("Columna",columna)

        if fila == 6 and columna == 6:
            laberinto[fila][columna] = '·'
            break
        elif laberinto[fila][columna] == ' ':
            laberinto[fila][columna] = '·'
        elif laberinto[fila+1][columna] == ' ':
            fila += 1
        elif laberinto[fila][columna+1] == ' ':
            columna += 1
        elif laberinto[fila][columna-1] == ' ':
            columna -= 1
        elif laberinto[fila-1][columna]== ' ' or laberinto[fila-1][columna]=='·':
            if laberinto[fila-1][columna]=='·' or laberinto[fila-1][columna]=='-':
                laberinto[fila][columna] = '-'
                fila -= 1
            else:
                fila -= 1
        else:
            break
        
        for x in range(len(laberinto)):
            for y in range(len(laberinto[x])):
                print(laberinto[x][y], end =" ")
            print()
                    
#laberinto()


def suma_cesta_compra(**kargs):

    s = 0
    for k,v in kargs.items():
        s += v
    return s

def una_funcion(*args,**kargs):
    pass

s = suma_cesta_compra(naranjas = 3.5,manzanas=4,uvas=10)
print(s)


