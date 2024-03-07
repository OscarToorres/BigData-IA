
"""
Algoritmo de la colonia de hormigas

Hay un número máximo de iteraciones: maxiter
Dentro de cada iteración un número máximo de saltos: maxtrans
Hay una ciudad objetivo: target
en cada iteración se crean un número de hormigas totalh y se disponen aleatoriamente
por todas las ciudades
En cada arista del grafo se guarda la contidad de feromonas (0<=f<=1) asociadas a la arista
En cada transición cada hormiga elige una ciudad entre las que puede visitar directamente
Esta ciudad tiene que ser una que no haya ya visitado
La elección de la ciudad se basa en dos factores
    alfa: importancia de la feromona acumulada en la arista
    beta: (1-alfa) importancia de la heurística (distancia a la ciudad)
una vez alzanzado el máximo número de saltos:
    Se procede a una evaporación de feromona en las aristas por un factor de gamma
    las hormigas que hubiesen llegado a destino depositan una cantidad de feromona
    finc en su ruta. Esta cantidad es inv. proporcional a la lg de la ruta

"""

import pprint
import random
import Grafo as gr

target = "A Coruña"

totalhormigas = 50 # nº total de hormigas
maxiter = 1000  # máximas iteraciones
maxtrans = 100  # transitos que hace una hormiga en cada iteración
gamma = 0.05    # factor de evaporación de feromonas
alfa = 0.7      # porcentaje de importancia de la feromona en una arista
beta = 1-alfa   # porcentaje de importancia de la distancia en una arista

fero_min = 1    # cantidad minima feromonas en una arista
fero_max = 300  # cantidad máxima feromonas en una arista
finc = (fero_max - fero_min) * 10  # cuanto aumentamos las feromonas en total en un trayecto

g = gr.Grafo()
g.load_grafo("gprovincias.json")

#lista de todas las ciudades
ciudades = ['Almería' ,'Cádiz' ,'Córdoba' ,'Granada' ,'Huelva' ,'Jaén' ,'Málaga' ,'Sevilla' ,'Huesca' ,
            'Teruel' ,'Zaragoza ' ,'Oviedo' ,'Santander' ,'Albacete' ,'Ciudad Real' ,'Cuenca' ,'Guadalajara' ,
            'Toledo' ,'Ávila' ,'Burgos' ,'León' ,'Palencia' ,'Salamanca' ,'Segovia' ,'Soria' ,'Valladolid' ,
            'Zamora' ,'Barcelona' ,'Girona' ,'Lleida' ,'Tarragona' ,'Madrid' ,'Pamplona' ,'Alicante' ,'Castellón' ,
            'Valencia' ,'Badajoz' ,'Cáceres' ,'A Coruña' ,'Lugo' ,'Ourense' ,'Pontevedra' ,'Logroño' ,'Vitoria' ,'Donostia' ,'Bilbao' ,'Murcia']

# poner en todas las aristas la variable feromonas a fero_min
for n in g.nodos:
    g.set_node_attributes(n, fer_min=0)


iter = 0
while iter < maxiter:
    #Asignar a cada hormiga una ciudad aleatoria
    #Crear lista de hormigas
    hormiga = []
    for h in range(totalhormigas):
        hormiga.append(ciudades[random.randint(0,46)])
    
    trans = 0
    while trans < maxtrans:
        g.recorre_grafo(nodo_inicial = "A Coruña",nodo_destino="Cádiz",modo='anchura')
        ruta = g.genera_ruta("Cádiz")
        print(ruta)
        print('==========')
        trans += 1
        break
    iter += 1
    break
        # Para cada hormiga:
        #   si estamos en destino nos quedamos quietas
        #   miramos las ciudades adyacentes que no hayamos visitado
        #   elegimos una en función de su distancia y las feromnas de su arista
        #   nos movemos a ella
    #   evapora un poco de feromona en cada arista
    #   para las hormigas que llegaron a destino:
    #     aumenta las feromonas en el trayecto recorrido