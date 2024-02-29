class Nodo:
    def __init__(self,datos):
        self.no = None
        self.si = None
        self.datos = datos

    def pregunta_recursivo(self, nodo):
        if nodo.no is None and nodo.si is None:
            print(f"La respuesta es: {nodo.datos}")
            return
        pregunta = nodo.datos
        respuesta = input(pregunta + "-> ")


        if respuesta == "no": self.pregunta_recursivo(nodo.no)
        elif respuesta == "si": self.pregunta_recursivo(nodo.si)



raiz = Nodo("Hojas con forma de aguja (aciculares)")
raiz.si = Nodo("Aciculas largas")
raiz.si.si = Nodo("PINO")
raiz.si.no = Nodo("Acículas reunidas en grupos (verticiliadas)")
raiz.si.no.si = Nodo("CEDRO")
raiz.si.no.no = Nodo("ABETO")
raiz.no = Nodo("Hojas ni escamosas ni imbricadas (limbo plano y ancho)")
raiz.no.si = Nodo("Hojas compuestas")
raiz.no.si.si = Nodo("Hojas palmado-compuestas")
raiz.no.si.si.si = Nodo("CASTAÑO DE INDIAS")
raiz.no.si.si.no = Nodo("Fruto en legumbre")
raiz.no.si.si.no.si = Nodo("FALSA ACACIA")        
raiz.no.si.si.no.no = Nodo("FRESNO")
raiz.no.si.no = Nodo("Hojas duras")
raiz.no.si.no.si = Nodo("El fruto es una bellota")
raiz.no.si.no.si.si = Nodo("ENCINA")
raiz.no.si.no.si.no = Nodo("MADROÑO")
raiz.no.si.no.no = Nodo("Hoja Penninervia")
raiz.no.si.no.no.si = Nodo("Hoja 2 veces mas larga que ancha")
raiz.no.si.no.no.si.si = Nodo("SAUCE LLORÓN")
raiz.no.si.no.no.si.no = Nodo("Borde inferior asimétrico + aserrado + ovalada")
raiz.no.si.no.no.si.no.si = Nodo("OLMO")
raiz.no.si.no.no.si.no.no = Nodo("CHOPO")
raiz.no.si.no.no.no = Nodo("Fruto con dos alas que forman un ángulo")
raiz.no.si.no.no.no.si = Nodo("ARCE")
raiz.no.si.no.no.no.no = Nodo("PLÁTANO DE SOMBRAS")
raiz.no.no = Nodo("CIPRÉS")

raiz.pregunta_recursivo(raiz)
#Nodo.pregunta_recursivo(raiz,raiz)