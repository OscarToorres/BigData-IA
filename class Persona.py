class Persona():
    def __init__(self,nombre,edad,dni):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni
    
    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self,n):
        self._nombre = n

    @property
    def edad(self):
        return self._edad
    @edad.setter
    def edad(self,e):
        self._edad = e

    @property
    def dni(self):
        return self._dni
    @dni.setter
    def dni(self,d):
        letras = "TRWAGMYFPDXBNJZSQVHLCKE"
        letra_dni = d[-1]
        print(letra_dni)
        numero_dni = int(d[0:8])
        print(numero_dni)
        print(numero_dni % 23)
        if letras[numero_dni % 23] == letra_dni:
            self._dni = d
            print("DNI válido")

        else:
            self._dni = "?????????"
            print("DNI no válido")

    def __str__(self):
        return f"Persona de nombre {self._nombre}, edad {self._edad}, y con dni {self._dni}"
    
    def esMayorDeEdad(self):
        if self._edad >= 18:
            print(f"{self._nombre} es mayor de edad")
        else:
            print(f"{self._nombre} es menor de edad")

class Cuenta():
        
    def __init__(self,titular, cantidad):
        self.titular = titular
        self.cantidad = cantidad

    @property
    def titular(self):
        return self._titular
    @titular.setter
    def titular(self,t):
        self._titular = t

    @property
    def cantidad(self):
        return self._cantidad
    @cantidad.setter
    def cantidad(self,c):
        self._cantidad = c

    def __str__(self):
        return f"Cuenta de titular {self._titular} y cantidad {self._cantidad}"
    
    def ingresar(self,añadir):
        if añadir >= 0:
            self._cantidad = self._cantidad + añadir
            
        else:
            print("Cantidad no valida")

    def retirar(self,retirar):
        self._cantidad = self._cantidad - retirar

class CuentaJoven(Cuenta):

    def __init__(self, titular, cantidad, bonificacion):
        super().__init__(titular, cantidad)
        self.bonificacion = bonificacion
    
    @property
    def bonificacion(self):
        return self._bonificacion
    @bonificacion.setter
    def bonificacion(self,b):
        self._bonificacion = b
    
    def esTitularValido(self):
        if self.titular.edad >= 18 and self.titular.edad < 25:
            return True
        else:
            return False
    
    def retirar(self,retirar):
        if (self.esTitularValido) and (retirar <= self.cantidad):
            nuevaCantidad = self.cantidad - retirar
            self.cantidad = nuevaCantidad
            print("Operacion realizada con exito, nuevo saldo =",self.cantidad)
        else:
            print("No se puede realizar esa operacion")

    def __str__(self):
        return f"Cuenta Joven de titular {self.titular} y cantidad {self.cantidad}"
    
     
persona = Persona("Pedro",23,"78808084X")
cuenta = Cuenta(persona,14500)
cj = CuentaJoven(persona,10000,0.5)
print(cuenta.__str__())
cuenta.ingresar(1200)
print(cuenta.__str__())
print(persona.__str__())
print(cj.__str__())
print(cj.esTitularValido())
cj.retirar(1000)
persona.dni = '34564562A'
print(persona.__str__())
