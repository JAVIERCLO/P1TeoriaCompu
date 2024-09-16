from estado import Estado

class AFD:
    def __init__(self):
        self.estados = []
        self.transiciones = {}
        self.aceptacion = set()
    #mueve
    @staticmethod
    def mover(estados, simbolo):
        resultado = set()
        for estado in estados:
            if simbolo in estado.transiciones:
                resultado.update(estado.transiciones[simbolo])
        return resultado
    #epsilon
    @staticmethod
    def cerradura_epsilon(estados):
        resultado = set(estados)
        pila = list(estados)
        while pila:
            estado = pila.pop()
            if 'ε' in estado.transiciones:
                for siguiente in estado.transiciones['ε']:
                    if siguiente not in resultado:
                        resultado.add(siguiente)
                        pila.append(siguiente)
        return resultado
#Funcion para convertir el AFN a AFD
def convertir_AFD(afn):
    d0 = AFD.cerradura_epsilon([afn.inicio])
    afd = AFD()
    estados_afd = {frozenset(d0): len(afd.estados)}
    afd.estados.append(d0)
    
    pila = [d0]
    
    while pila:
        estado = pila.pop()
        for simbolo in set.union(*[set(e.transiciones.keys()) for e in estado if e.transiciones]):
            if simbolo == 'ε':  # Ignorar transiciones ε
                continue
            mover_estados = AFD.mover(estado, simbolo)
            cerradura = AFD.cerradura_epsilon(mover_estados)
            cerradura_frozen = frozenset(cerradura)
            
            if cerradura_frozen not in estados_afd:
                estados_afd[cerradura_frozen] = len(afd.estados)
                afd.estados.append(cerradura)
                pila.append(cerradura)
            
            afd.transiciones[(estado, simbolo)] = cerradura_frozen
    
    for estados in afd.estados:
        if afn.aceptacion in estados:
            afd.aceptacion.add(frozenset(estados))
    
    return afd
