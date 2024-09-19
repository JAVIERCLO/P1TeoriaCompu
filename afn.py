from estado import Estado

class AFN:
    def __init__(self, inicio=None, aceptacion=None):
        #Lista de estados
        self.estados = []
        
        #Estado inicial
        self.inicio = inicio or Estado()
        self.estados.append(self.inicio)
        
        #Estado de aceptacion
        self.aceptacion = aceptacion or Estado()
        self.estados.append(self.aceptacion)

    # Concatenación .
    @staticmethod
    def concatenacion(afn1, afn2):
        afn1.aceptacion.agregar_transicion('ε', afn2.inicio)
        afn1.estados.extend(afn2.estados)  # Combina los estados de ambos autómatas
        return AFN(afn1.inicio, afn2.aceptacion)

    #Union |
    @staticmethod
    def union(afn1, afn2):
        nuevo_inicio = Estado()
        nuevo_aceptacion = Estado()
        
        nuevo_inicio.agregar_transicion('ε', afn1.inicio)
        nuevo_inicio.agregar_transicion('ε', afn2.inicio)
        afn1.aceptacion.agregar_transicion('ε', nuevo_aceptacion)
        afn2.aceptacion.agregar_transicion('ε', nuevo_aceptacion)
        
        #Combina los estados de los automatas con los nuevos
        nuevo_afn = AFN(nuevo_inicio, nuevo_aceptacion)
        nuevo_afn.estados.extend(afn1.estados)
        nuevo_afn.estados.extend(afn2.estados)
        return nuevo_afn

    #Cerradura Kleen *
    @staticmethod
    def kleen(afn):
        nuevo_inicio = Estado()
        nuevo_aceptacion = Estado()
        
        nuevo_inicio.agregar_transicion('ε', afn.inicio)
        nuevo_inicio.agregar_transicion('ε', nuevo_aceptacion)
        afn.aceptacion.agregar_transicion('ε', afn.inicio)
        afn.aceptacion.agregar_transicion('ε', nuevo_aceptacion)
        
        #agragar los nuevos estados al automata
        nuevo_afn = AFN(nuevo_inicio, nuevo_aceptacion)
        nuevo_afn.estados.extend(afn.estados)
        return nuevo_afn

    #Simbolo 
    @staticmethod
    def simbolo(simbolo):
        inicio = Estado()
        aceptacion = Estado()
        inicio.agregar_transicion(simbolo, aceptacion)
        
        #Crear el AFN con los dos estados
        nuevo_afn = AFN(inicio, aceptacion)
        return nuevo_afn


#Construir afn desde postfix
def construir_AFN(postfix):
    pila = []
    
    for c in postfix:
        if c.isalnum() or c == 'ε':
            pila.append(AFN.simbolo(c))
        elif c == '.':  # Concatenacion
            afn2 = pila.pop()
            afn1 = pila.pop()
            pila.append(AFN.concatenacion(afn1, afn2))
        elif c == '|':  # Union
            afn2 = pila.pop()
            afn1 = pila.pop()
            pila.append(AFN.union(afn1, afn2))
        elif c == '*':  # kleen
            afn1 = pila.pop()
            pila.append(AFN.kleen(afn1))
    
    return pila.pop()
