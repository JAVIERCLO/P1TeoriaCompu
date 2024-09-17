def minimizar_AFD(afd):
    # Crear particiones de estados iniciales y de aceptación
    particiones = [afd.aceptacion, set(frozenset(estado) for estado in afd.estados) - afd.aceptacion]
    nueva_particion = []
    
    while True:
        for particion in particiones:
            simbolo_transiciones = {}
            for estado in particion:
                for simbolo in afd.transiciones:
                    if simbolo in estado:
                        simbolo_transiciones[estado] = afd.transiciones.get((estado, simbolo))
            nueva_particion.extend(simbolo_transiciones.values())
        
        if nueva_particion == particiones:
            break
        particiones = nueva_particion[:]

    # Retorna el AFD minimizado
    return afd