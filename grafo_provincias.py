import json
import math
import pprint
import matplotlib.pyplot as plt
import numpy as np

class ErrNodoGrafo(Exception):
  def __init__(self, message='nodo no existe en el grafo'):
    super().__init__(message)


class Grafo:
  def __init__(self):
    self.nodos = {}
    self.abiertos = []
    self.cerrados = []

  def add_node(self, nodo, **kargs):
    if nodo in self.nodos: raise ErrNodoGrafo(message="Nodo Ya Existe!!")
    self.nodos[nodo] = {"edges":{}}
    for k,v in kargs.items():
      self.nodos[nodo][k] = v

  def remove_node(self, nodo):
    if nodo not in self.nodos: raise ErrNodoGrafo
    # desconectarme de todos los nodos con los que tengo aristas
    for n in self.nodos[nodo]["edges"]:
      self.nodos[n]["edges"].pop(nodo)
    self.nodos.pop(nodo)

  def set_node_attributes(self, nodo, **kargs):
    for k,v in kargs.items():
      self.nodos[nodo][k] = v

  def get_node_attribute(self, nodo, attribute, default=None):
    ret = self.nodos[nodo].get(attribute, default)
    return ret

  def add_edge(self, nodo1, nodo2, **kargs):
    if nodo1 not in self.nodos or nodo2 not in self.nodos: raise ErrNodoGrafo
    self.nodos[nodo1]["edges"][nodo2] = kargs
    self.nodos[nodo2]["edges"][nodo1] = kargs

  def remove_edge(self, nodo1, nodo2):
    if nodo1 not in self.nodos or nodo2 not in self.nodos: raise ErrNodoGrafo
    self.nodos[nodo1]["edges"].pop(nodo2, None)
    self.nodos[nodo2]["edges"].pop(nodo1, None)

  def set_edge_attributes(self, nodo1, nodo2, **kargs):
    for k,v in kargs.items():
      self.nodos[nodo1]["edges"][nodo2][k] = v

  def get_edge_attribute(self, nodo1, nodo2, attribute, default=None):
    ret = self.nodos[nodo1]["edges"][nodo2].get(attribute, default)
    return ret

  # returna una lista con los nodos conectados
  def adj(self, nodo):
    adyacentes = [n for n in self.nodos[nodo]["edges"]]
    return adyacentes

  def load_grafo(self, filename):
    with open(filename) as f:
        # Cargar su contenido y crear un diccionario
        self.nodos = json.load(f)

  def dibuja(self):
    fig, ax = plt.subplots()

  # para cada nodo, dibuja un circulo en la posicion Xn, Yn
    for n in self.nodos:
      Xn = self.get_node_attribute(n, "x", 0)
      Yn = self.get_node_attribute(n, "y", 0)
      ax.scatter(Xn, Yn, s=300)
      ax.text(Xn,Yn, n)
      # para cada arista
      for arista in self.nodos[n]["edges"]:
        # mira la posicion del nodo destino Xd, Yd
        Xd = self.get_node_attribute(arista, "x", 0)
        Yd = self.get_node_attribute(arista, "y", 0)
        ax.plot([Xn, Xd], [Yn, Yd], color="b", linewidth=0.5)
        # Escribe el weight en la mitad de camino entre los dos nodos
        ax.text((Xn+Xd)/2, (Yn+Yd)/2, self.get_edge_attribute(n, arista, "weight", 0), alpha=0.5)




  # quita y devuelve un nodo de abiertos,
  # si modo = profundidad devuelve el último en entrar LIFO
  # si modo = anchura devuelve el primero en entrar (FIFO)
  # .....
  def pop_abiertos(self, modo):
    ret = None
    if modo == "profundidad":
      ret = self.abiertos.pop()
    elif modo == "anchura":
      ret = self.abiertos.pop(0)
    elif modo == "dijkstra":
      # escoger de todos los de abiertos el que tenga menor
      # valor de distanciaOrg
      minimo = self.get_node_attribute(self.abiertos[0], "distanciaOrg" )
      orden_minimo = 0
      for i, n in enumerate(self.abiertos):
        valor = self.get_node_attribute(n, "distanciaOrg" )
        if valor < minimo:
          minimo = valor
          orden_minimo = i
      ret = self.abiertos.pop(orden_minimo)
    elif modo == "avaricioso":
      # escoger de todos los de abiertos el que tenga menor
      # valor de distanciaDst
      minimo = self.get_node_attribute(self.abiertos[0], "distanciaDst" )
      orden_minimo = 0
      for i, n in enumerate(self.abiertos):
        valor = self.get_node_attribute(n, "distanciaDst" )
        if valor < minimo:
          minimo = valor
          orden_minimo = i
      ret = self.abiertos.pop(orden_minimo)
    elif modo == "A*":
      #Escoger la media
      pass

    return ret

  # si el nodo es una solución del problema devuelve TRUE
  def es_solucion(self, nodo_actual):
    print(f"Procesando nodo: {nodo_actual}")
    return False

  # devuelve una lista con todos los nodos conectados al nodo actual
  def genera_sucesores(self, nodo_actual):
    return self.adj(nodo_actual)

  # devuelve una lista con los hijos, decidiendo que hacer si ya están en abiertos o cerrados
  def procesa_repetidos(self, hijos_iniciales):
    # print(f"procesa_repetidos: {hijos_iniciales}")
    hijos = [h for h in hijos_iniciales if h not in self.abiertos and h not in self.cerrados]
    return hijos

  # hacer recorridos del grafo en profundidad, anchura, dijkstra ....
  def recorre_grafo(self, nodo_inicial = None,nodo_destino=None, modo="anchura"):
    self.abiertos = []
    self.cerrados = []

    # si no se proporciona inicial escojo el primero que se creó
    if nodo_inicial is None: nodo_inicial = list(self.nodos.keys())[0]

    # poner en todos los nodos un atributo distanciaOrg = inf
    # poner en todos los nodos un atributo distanciaDst = inf
    # excepto en el inicial que es 0
    for nodo in self.nodos:
      if nodo != nodo_inicial:
        self.set_node_attributes(nodo,distanciaOrg=np.inf)
        self.set_node_attributes(nodo,distanciaDst=np.inf)
      else:
        self.set_node_attributes(nodo,distanciaOrg=0)
        self.set_node_attributes(nodo,distanciaDst=0)

      
    # metemos en abiertos el nodo inicial
    self.abiertos.append(nodo_inicial)

    while len(self.abiertos) > 0: # mientras en abiertos existan nodos
      # quitar un nodo
      actual = self.pop_abiertos(modo)

      # mirar si es una solución
      # si tal break
      if self.es_solucion(actual):
        break

      # actual a cerrado
      self.cerrados.append(actual)

      # generar sucesores
      hijos = self.genera_sucesores(actual)
      print(hijos)

      # si estamos en modo dijkstra
      # para cada hijo,
      # Si (distanciaOrg de actual + weight hacia el hijo )   <    distanciaOrg del hijo
      # distanciaOrg del hijo = (distanciaOrg de actual + weight hacia el hijo )

      #if modo == 'dijkstra':

      d_actual = self.get_node_attribute(actual, "distanciaOrg", 0)
      #d_hijo = self.get_node_attribute(hijo, "distanciaDst", 0)

      for hijo in hijos:
        c_hijo = self.get_edge_attribute(actual, hijo, "weight", 0)
        d_hijo = self.get_node_attribute(hijo, "distanciaOrg", 0)
        #d_hijo = self.get_node_attribute(hijo, "distanciaDst", 0)

        if (c_hijo + d_actual) < d_hijo:
          self.set_node_attributes(hijo, distanciaOrg=(c_hijo+d_actual))
          self.set_node_attributes(hijo, antecesor=actual)
        #calcular la distancia a destino de cada hijo y anotarla en el
        if nodo_destino:
          d_destino = self.calcula_distanciaDst(nodo_destino,hijo)
          #actualizar en hijo esta distancia
          self.set_node_attributes(hijo,distanciaDst=d_destino)

        '''
        for n in hijos:
          print("Hijo: ",n)
          distancia = self.nodos[actual]["distanciaOrg"] + self.nodos[actual]["edges"][n]["weight"]
          print("Distancia ", distancia)
          if distancia < self.nodos[n]["distanciaOrg"]:
            self.nodos[n]["distanciaOrg"] = distancia
        '''

      # que hacer con los repetidos
      hijos = self.procesa_repetidos(hijos)


      # insertar los hijos en abiertos
      for hijo in hijos:
        self.abiertos.append(hijo)

  def calcula_distanciaDst(self,destino,origen):
    #retorna una heuristica de la distancia
    x1 = self.get_node_attribute(origen,attribute="x")
    y1 = self.get_node_attribute(origen,attribute="y")
    x2 = self.get_node_attribute(destino,attribute="x")
    y2 = self.get_node_attribute(destino,attribute="y")
    distancia = (math.sqrt((x2-x1)**2 + (y2-y1)**2)) * 111
    return distancia
    

  def genera_ruta(self, inicio, puntero="antecesor"):
    ruta = []
    nodo = inicio
    while nodo is not None and nodo not in ruta:
      ruta.append(nodo)
      nodo = self.get_node_attribute(nodo, puntero)
    return ruta
  
  def dibuja_ruta(self, ruta):
    for i, n in enumerate(ruta):
      if i == 0: continue
      x1 = self.get_node_attribute(ruta[i-1], "x")
      y1 = self.get_node_attribute(ruta[i-1], "y")
      x2 = self.get_node_attribute(ruta[i], "x")
      y2 = self.get_node_attribute(ruta[i], "y")
      plt.plot([x1, x2], [y1, y2], color="k", linewidth=2)
  
  
g = Grafo()
'''
g.add_node("A", x=1, y=5)
g.add_node("B", x=3, y=6)
g.add_node("C", x=2, y=0)
g.add_node("D", x=4, y=2)
g.add_node("E", x=5, y=7)
g.add_edge("A", "B", weight=3)
g.add_edge("A", "C", weight=1)
g.add_edge("B", "C", weight=7)
g.add_edge("C", "D", weight=2)
g.add_edge("B", "D", weight=5)
g.add_edge("B", "E", weight=1)
g.add_edge("D", "E", weight=7)
#pprint.pprint(g.nodos)
g.dibuja()

g.recorre_grafo(nodo_inicial = "A", modo="dijkstra")
pprint.pprint(g.nodos)
plt.show()
'''

#Provincias
g.load_grafo("gprovincias.json")
g.recorre_grafo(nodo_inicial = "A Coruña",nodo_destino="Cádiz", modo = "avaricioso")
ruta = g.genera_ruta("Cádiz")
g.dibuja()
g.dibuja_ruta(ruta)
print(ruta[::-1])
pprint.pprint(g.nodos)
plt.show() 