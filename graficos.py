import graphviz

def graficar(automata, nombre_archivo):
    dot = graphviz.Digraph(comment=nombre_archivo)
    
    for estado in automata.estados:
        dot.node(str(estado.id), shape='doublecircle' if estado == automata.aceptacion else 'circle')
    
    for estado in automata.estados:
        for simbolo, destinos in estado.transiciones.items():
            for destino in destinos:
                dot.edge(str(estado.id), str(destino.id), label=simbolo)
    
    dot.render(nombre_archivo, format='png')
