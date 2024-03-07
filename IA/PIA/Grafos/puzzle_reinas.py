import random
import time


class Reinas():

    # self.poblacion = []
    def __init__(self,n):
        self.ndamas = n
        self.poblacion = []
        self.errores = []
        self.solucion = []

    def genera_elementos(self):
        contador = 0
        while contador < 100:
            habitante = []
            opciones = []
            for i in range(self.ndamas):
                opciones.append(i)
            for i in range(self.ndamas):
                elemento = random.choice(opciones)
                opciones.remove(elemento)
                habitante.append(elemento)
            self.poblacion.append(habitante)
            contador += 1

    def valora_errores_posicion(self,posicion):
        habitante = posicion
        #Recorro el habitante de la poblacion
        error = 0
        for i in range(len(habitante)):
            #Recorro otra vez el habitante de la poblacion
            for j in range(len(habitante)):
                if (habitante[i] != habitante[j]):
                    # #Comprobacion de columnas
                    # if (habitante[i] == j):
                    #     error = error + 1
                    # #Comprobacion de filas
                    # if(i == habitante[j]):
                    #     error = error + 1
                    #Comprobacion de diagonales inferiores
                    if ((habitante[i] - i) == (habitante[j] - j)):
                        error = error + 1
                    #Comprobacion de diagonales superiores
                    if ((habitante[i] + i) == (habitante[j] + j)):
                        error = error + 1
        if (error == 0):
            self.solucion.append(posicion)
            return error
        else:
            return error

    def comprobarSiContiene(self,individuo):
        nuevo_individuo = individuo
        while len(individuo) < self.ndamas:
            valor = random.randint(0,self.ndamas-1)
            if valor not in individuo:
                nuevo_individuo.append(valor)
        if nuevo_individuo in r.poblacion:
            habitante = []
            opciones = []
            for i in range(self.ndamas):
                opciones.append(i)
            for i in range(self.ndamas):
                elemento = random.choice(opciones)
                opciones.remove(elemento)
                habitante.append(elemento)
            nuevo_individuo = habitante 
            return nuevo_individuo
        else:
            return nuevo_individuo                

random.seed(1)
inicio = time.time()
r = Reinas(n=20)
r.genera_elementos()
contador = 0
while r.solucion == []:
    r.poblacion.sort(key = r.valora_errores_posicion)
    r.poblacion = r.poblacion[:100]
    # print(r.poblacion)
    for i in range(50):
        indice1 = random.randint(0, 99)
        individuo1 = r.poblacion[indice1]
        #=========================
        if (i%2 == 0):
            hijo = r.comprobarSiContiene(individuo=individuo1[:round(r.ndamas*(1-indice1/100))])
            r.poblacion.append(hijo)
        else:
            hijo = r.comprobarSiContiene(individuo=individuo1[round(r.ndamas*(1-indice1/100)):])
            r.poblacion.append(hijo)
        #=========================        
        # if (indice1 <= 15):
        #     hijo = r.comprobarSiContiene(individuo=individuo1[:round(r.ndamas*0.8)])
        #     r.poblacion.append(hijo)
        # elif (indice1 <= 30):
        #     hijo = r.comprobarSiContiene(individuo=individuo1[round(r.ndamas*0.6):])
        #     r.poblacion.append(hijo)
        # elif (indice1 <= 50):
        #     hijo = r.comprobarSiContiene(individuo=individuo1[round(r.ndamas*0.5):])
        #     r.poblacion.append(hijo)                         
        # elif (indice1 > 50):
        #     hijo = r.comprobarSiContiene(individuo=individuo1[:round(r.ndamas*0.5)])
        #     r.poblacion.append(hijo)
        #=========================
        #=========================
        if (indice1 <= 15):
            hijo = r.comprobarSiContiene(individuo=individuo1[:round(r.ndamas*0.8)])
            r.poblacion.append(hijo)
        elif (indice1 > 15) and (indice1 <= 30):
            hijo = r.comprobarSiContiene(individuo=individuo1[round(r.ndamas*0.6):])
            r.poblacion.append(hijo)
        elif (indice1 > 30) and (indice1 <= 50):
            hijo = r.comprobarSiContiene(individuo=individuo1[round(r.ndamas*0.5):])
            r.poblacion.append(hijo)                         
        elif (indice1 > 50) and (indice1 <= 70):
            hijo = r.comprobarSiContiene(individuo=individuo1[:round(r.ndamas*0.4)])
            r.poblacion.append(hijo)
        elif (indice1 > 70):
            hijo = r.comprobarSiContiene(individuo=individuo1[:round(r.ndamas*0.3)])
            r.poblacion.append(hijo)                         
    contador += 1

print('Ejecuciones del bucle:',contador)
print('Solucion',r.solucion)

tablero = []
for i in range(r.ndamas):
    tablero.append(['-'] * r.ndamas)

for i in range(r.ndamas):
    tablero[i][r.solucion[0][i]] = 'R'

for row in tablero:
    print(*row)

executionTime = (time.time () - inicio)
print ('Tiempo de ejecucion: ' + str (executionTime))