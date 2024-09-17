
from shunting_yard import shunting_yard
from afn import construir_AFN
from afd import convertir_AFD
from minimizacion import minimizar_AFD
from graficos import graficar

def procesar_expresion(expresion):
    # Convierte la expresión infix a postfix
    postfix = shunting_yard(expresion)  
    
    # Construye el AFN usando la función construir_AFN
    afn = construir_AFN(postfix)  
    
    # Convierte el AFN en un AFD usando convertir_AFD
    afd = convertir_AFD(afn)  
    
    # Minimiza el AFD
    afd_minimizado = minimizar_AFD(afd)  
    
    # Generar los grafos de los autómatas
    graficar(afn, f'AFN_{expresion}')
    graficar(afd_minimizado, f'AFD_minimizado_{expresion}')

def procesar_data(ruta_archivo):
    with open(ruta_archivo, 'r') as archivo:
        for linea in archivo:
            # Procesar la expresión regular
            expresion = linea.strip()
            procesar_expresion(expresion)

if __name__ == "__main__":
    # Ruta del archivo
    ruta_archivo = r"C:\Users\javie\Desktop\Tareas\Teoria compu\P1TeoriaCompu\expresiones.txt"
    
    # Leer el archivo
    procesar_data(ruta_archivo)
