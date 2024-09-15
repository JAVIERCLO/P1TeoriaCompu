#Clase para representar cada estado de los automatas
class Estado:
    def __init__(self):
        self.transiciones = {}
        self.id = id(self)
    
    def agregar_transicion(self, simbolo, estado):
        if simbolo not in self.transiciones:
            self.transiciones[simbolo] = []
        self.transiciones[simbolo].append(estado)
