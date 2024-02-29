class Persona:
  def __init__(self, dni, nombre="Desconocido", edad = 0):
    self.dni = dni
    self.nombre = nombre
    self.edad = edad
    self.izda = None
    self.dcha = None


  def anade(self, otra):
#    print(f"soy {self} e intento insertar a {otra}")
    if otra < self:
#      print("hacia mi rama izda")
      if self.izda is None: self.izda = otra; # print("Hecho")
      else:                 self.izda.anade(otra)
    else:
#      print("hacia mi rama dcha")
      if self.dcha is None: self.dcha = otra; # print("Hecho")
      else:                 self.dcha.anade(otra)

  def busca(self, dni):
    if isinstance(dni, int): dni = str(dni)
    while len(dni) < 8: dni = "0" + dni
    return self.busca_aux(dni)

  def busca_aux(self, dni):
    if self.dni == dni: return self
    if dni < self.dni:
      if self.izda is None: return None
      return self.izda.busca_aux(dni)
    if self.dcha is None: return None
    return self.dcha.busca_aux(dni)

  def recorre_recursivo(self):
    if self.izda: self.izda.recorre_recursivo()
    if self.dcha: self.dcha.recorre_recursivo()
    print(self)

  @property
  def dni(self):
    return self._dni

  @dni.setter
  def dni(self, dni):
    if isinstance(dni, int): dni = str(dni)
    while len(dni) < 8: dni = "0" + dni
    self._dni = dni

  def __eq__(self, otro):
    return self.dni == otro.dni
  def __ne__(self, otro):
    return self.dni != otro.dni
  def __lt__(self, otro):
    return self.dni < otro.dni
  def __gt__(self, otro):
    return self.dni > otro.dni
  def __le__(self, otro):
    return self.dni <= otro.dni
  def __ge__(self, otro):
    return self.dni >= otro.dni

  def __str__(self):
    return f"Persona: dni: {self.dni} nombre: {self.nombre} edad: {self.edad}"

raiz = None
dnis = ["777", "333", "999", "888", "111", "555", "444"]

for d in dnis:
  p = Persona(d, f"", 0)
  if raiz is None: raiz = p
  else: raiz.anade(p)

raiz.recorre_recursivo()