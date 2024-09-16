from estado import Estado

class AFN:
    def __init__(self, inicio=None, aceptacion=None):
        #Estado inicial
        self.inicio = inicio or Estado()
        #Estado de aceptacion
        self.aceptacion = aceptacion or Estado()

    #Concatenacion .
    @staticmethod
    def concatenacion(afn1, afn2):
        afn1.aceptacion.agregar_transicion('ε', afn2.inicio)
        return AFN(afn1.inicio, afn2.aceptacion)
    #Union |
    @staticmethod
    def union(afn1, afn2):
        nuevo_inicio = Estado()
        nuevo_inicio.agregar_transicion('ε', afn1.inicio)
        nuevo_inicio.agregar_transicion('ε', afn2.inicio)
        nuevo_aceptacion = Estado()
        afn1.aceptacion.agregar_transicion('ε', nuevo_aceptacion)
        afn2.aceptacion.agregar_transicion('ε', nuevo_aceptacion)
        return AFN(nuevo_inicio, nuevo_aceptacion)
    #Cerradura Kleen *
    @staticmethod
    def kleen(afn):
        nuevo_inicio = Estado()
        nuevo_aceptacion = Estado()
        nuevo_inicio.agregar_transicion('ε', afn.inicio)
        nuevo_inicio.agregar_transicion('ε', nuevo_aceptacion)
        afn.aceptacion.agregar_transicion('ε', afn.inicio)
        afn.aceptacion.agregar_transicion('ε', nuevo_aceptacion)
        return AFN(nuevo_inicio, nuevo_aceptacion)
    #Simbolo S
    @staticmethod
    def simbolo(simbolo):
        inicio = Estado()
        aceptacion = Estado()
        inicio.agregar_transicion(simbolo, aceptacion)
        return AFN(inicio, aceptacion)
