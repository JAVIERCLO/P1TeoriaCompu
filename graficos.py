import re
import graphviz

def limpiar_nombre_archivo(nombre):
    # Reemplazar caracteres con _ para evitar errores
    return re.sub(r'[^\w\-_\. ]', '_', nombre)

def graficar(automata, nombre_archivo):
    dot = graphviz.Digraph(comment=nombre_archivo)
    
    for estado in automata.estados:
        dot.node(str(estado.id), shape='doublecircle' if estado == automata.aceptacion else 'circle')
    
    for estado in automata.estados:
        for simbolo, destinos in estado.transiciones.items():
            for destino in destinos:
                dot.edge(str(estado.id), str(destino.id), label=simbolo)
    
    #Limpia el nombre del archivo antes de guardarlo
    nombre_archivo = limpiar_nombre_archivo(nombre_archivo)
    
    #Imprime el nombre del archivo para verificar
    print(f"Guardando archivo: {nombre_archivo}")
    
    dot.render(nombre_archivo, format='png')


