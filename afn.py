from estado import Estado

class AFN:
    def __init__(self, inicio=None, aceptacion=None):
        # Estado inicial
        self.inicio = inicio or Estado()
        # Estado de aceptación
        self.aceptacion = aceptacion or Estado()

    # Concatenación (operador .)
    @staticmethod
    def concatenacion(afn1, afn2):
        afn1.aceptacion.agregar_transicion('ε', afn2.inicio)
        return AFN(afn1.inicio, afn2.aceptacion)

    # Unión (operador |)
    @staticmethod
    def union(afn1, afn2):
        nuevo_inicio = Estado()
        nuevo_inicio.agregar_transicion('ε', afn1.inicio)
        nuevo_inicio.agregar_transicion('ε', afn2.inicio)
        nuevo_aceptacion = Estado()
        afn1.aceptacion.agregar_transicion('ε', nuevo_aceptacion)
        afn2.aceptacion.agregar_transicion('ε', nuevo_aceptacion)
        return AFN(nuevo_inicio, nuevo_aceptacion)

    # Estrella de Kleene (operador *)
    @staticmethod
    def kleen(afn):
        nuevo_inicio = Estado()
        nuevo_aceptacion = Estado()
        nuevo_inicio.agregar_transicion('ε', afn.inicio)
        nuevo_inicio.agregar_transicion('ε', nuevo_aceptacion)
        afn.aceptacion.agregar_transicion('ε', afn.inicio)
        afn.aceptacion.agregar_transicion('ε', nuevo_aceptacion)
        return AFN(nuevo_inicio, nuevo_aceptacion)

    # Símbolo 
    @staticmethod
    def simbolo(simbolo):
        inicio = Estado()
        aceptacion = Estado()
        inicio.agregar_transicion(simbolo, aceptacion)
        return AFN(inicio, aceptacion)


# Construcción del AFN a partir de una expresión postfix
def construir_AFN(postfix):
    pila = []
    
    for c in postfix:
        if c.isalnum() or c == 'ε':  # Si es un símbolo
            pila.append(AFN.simbolo(c))
        elif c == '.':  # Concatenación
            afn2 = pila.pop()
            afn1 = pila.pop()
            pila.append(AFN.concatenacion(afn1, afn2))
        elif c == '|':  # Unión
            afn2 = pila.pop()
            afn1 = pila.pop()
            pila.append(AFN.union(afn1, afn2))
        elif c == '*':  # Estrella de Kleene
            afn1 = pila.pop()
            pila.append(AFN.kleen(afn1))
    
    return pila.pop()  # El AFN resultante es el último en la pila
