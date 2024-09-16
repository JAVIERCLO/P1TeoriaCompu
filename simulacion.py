from afd import AFD
#Inicia la simulacion del AFN
def simular_AFN(afn, cadena):
    actuales = AFD.cerradura_epsilon([afn.inicio])
    
    for simbolo in cadena:
        nuevos = set()
        for estado in actuales:
            if simbolo in estado.transiciones:
                nuevos.update(estado.transiciones[simbolo])
        actuales = AFD.cerradura_epsilon(nuevos)
    
    return afn.aceptacion in actuales
#Iicia la simulacion del AFD
def simular_AFD(afd, cadena):
    estado_actual = frozenset(afd.estados[0])
    
    for simbolo in cadena:
        estado_actual = afd.transiciones.get((estado_actual, simbolo), None)
        if estado_actual is None:
            return False
    
    return estado_actual in afd.aceptacion
