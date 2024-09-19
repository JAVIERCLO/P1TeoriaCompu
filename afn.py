from estado import Estado

class AFN:
    def __init__(self, inicio=None, aceptacion=None):
        # Lista de todos los estados del AFN
        self.estados = []
        
        # Estado inicial
        self.inicio = inicio or Estado()
        self.estados.append(self.inicio)
        
        # Estado de aceptación
        self.aceptacion = aceptacion or Estado()
        self.estados.append(self.aceptacion)

    # Concatenación (operador .)
    @staticmethod
    def concatenacion(afn1, afn2):
        afn1.aceptacion.agregar_transicion('ε', afn2.inicio)
        afn1.estados.extend(afn2.estados)  # Combina los estados de ambos autómatas
        return AFN(afn1.inicio, afn2.aceptacion)

    # Unión (operador |)
    @staticmethod
    def union(afn1, afn2):
        nuevo_inicio = Estado()
        nuevo_aceptacion = Estado()
        
        nuevo_inicio.agregar_transicion('ε', afn1.inicio)
        nuevo_inicio.agregar_transicion('ε', afn2.inicio)
        afn1.aceptacion.agregar_transicion('ε', nuevo_aceptacion)
        afn2.aceptacion.agregar_transicion('ε', nuevo_aceptacion)
        
        # Combina los estados de ambos autómatas más los nuevos estados
        nuevo_afn = AFN(nuevo_inicio, nuevo_aceptacion)
        nuevo_afn.estados.extend(afn1.estados)
        nuevo_afn.estados.extend(afn2.estados)
        return nuevo_afn

    # Estrella de Kleene (operador *)
    @staticmethod
    def kleen(afn):
        nuevo_inicio = Estado()
        nuevo_aceptacion = Estado()
        
        nuevo_inicio.agregar_transicion('ε', afn.inicio)
        nuevo_inicio.agregar_transicion('ε', nuevo_aceptacion)
        afn.aceptacion.agregar_transicion('ε', afn.inicio)
        afn.aceptacion.agregar_transicion('ε', nuevo_aceptacion)
        
        # Añade los nuevos estados al autómata
        nuevo_afn = AFN(nuevo_inicio, nuevo_aceptacion)
        nuevo_afn.estados.extend(afn.estados)
        return nuevo_afn

    # Símbolo 
    @staticmethod
    def simbolo(simbolo):
        inicio = Estado()
        aceptacion = Estado()
        inicio.agregar_transicion(simbolo, aceptacion)
        
        # Crear el AFN con los dos estados
        nuevo_afn = AFN(inicio, aceptacion)
        return nuevo_afn


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
