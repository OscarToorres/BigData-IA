import pprint
import matplotlib.pyplot as plt
import numpy as np

from Grafo import Grafo

class Plov(Grafo):
  def es_posicion_valida(self, m1,m2,m3,c_remero,c2,c3):
    misioneros = [m1,m2,m3]
    canivales = [c_remero,c2,c3]
    m_0 = 0
    c_0 = 0
    for m,c in misioneros,canivales:
      if m == 0:
        m_0 += 1
      if c == 0:
        c_0 += 1

    if m_0 < c_0: return False
    if 3-m_0 < 3-c_0: return False
    return True

  def genera_sucesores(self, nodo):

    hijos = []
    # Nodo = posicion anterior
    # s = la posicion en la que estas ahora
    for i in range(128):
      s=format(i,'07b')
      #barca quieta
      if s[0]==nodo[0]: 
        continue
      if s[1:] == nodo[1:]:
        continue
      # gente quieta
      #mas canivales que misioneros
      if s[1:4].count('0') and s[1:4].count('0')< s[4:].count('0'):
        continue
      if s[1:4].count('1') and s[1:4].count('1')< s[4:].count('1'):
        continue
      #se mueven como máximo 2
      if s[1:].count('0') > nodo[1:].count('0')+2:
        continue
      if s[1:].count('1') > nodo[1:].count('1')+2:
        continue
      #con la barca no se pueden mover los 2 canivales no remeros o uno de ellos
      direccion_barca=int(s[0])-int(nodo[0])
      #avanza
      #coge si van 2 o si va el 5
      if(direccion_barca==1 and nodo[5]=='0' and s[5]=='1' and s[1:5]==nodo[1:5]):
        continue
      #si va el canival 6 solo
      if(direccion_barca==1 and nodo[6]=='0' and s[6]=='1' and s[1:6]==nodo[1:6]):
        continue
      #coge si van 2 o si va el 5
      if(direccion_barca==-1 and nodo[5]=='1' and s[5]=='0' and s[1:5]==nodo[1:5]):
        continue
      #si va el canival 6 solo
      if(direccion_barca==-1 and nodo[6]=='1' and s[6]=='0' and s[1:6]==nodo[1:6]):
        continue
      
      #si cambia de orilla en distinto orden a barca, es decir van nadando
      a = 0
      for j in range(6):
        if (direccion_barca == 0 - (int(s[j+1])-int(nodo[j+1]))):
          a = 1
          break
      if a == 1:
        continue

      # print(s)
      hijos.append(s)
    print(f"padre: {nodo} hijos: {hijos}")
    return hijos

  def es_solucion(self, nodo_actual):
      return nodo_actual == "1111111"

g = Plov()
g.recorre_grafo(nodo_inicial = "0000000", modo="anchura")
ruta = g.genera_ruta("1111111")
print(ruta)