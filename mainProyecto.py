from shunting_yard import shunting_yard
from afn import construir_AFN
from afd import convertir_AFD
from minimizacion import minimizar_AFD
from simulacion import simular_AFN, simular_AFD
from graficos import graficar

def procesar_expresion(expresion, cadena):
    postfix = shunting_yard(expresion)
    afn = construir_AFN(postfix)
    afd = convertir_AFD(afn)
    afd_minimizado = minimizar_AFD(afd)
    
    print(f"Simulación AFN: {'Sí' if simular_AFN(afn, cadena) else 'No'}")
    print(f"Simulación AFD: {'Sí' if simular_AFD(afd_minimizado, cadena) else 'No'}")
    
    # Generar grafos de los autómatas
    graficar(afn, 'AFN')
    graficar(afd, 'AFD_minimizado')
#Leer el archivo y procesar cada expresion regular
def procesar_data(ruta_archivo):
    with open(ruta_archivo, 'r') as archivo:
        for linea in archivo:
            #Para una expresion regular y una cadena en cada linea, separadas por ,
            expresion, cadena = linea.strip().split(',')
            procesar_expresion(expresion, cadena)

if __name__ == "__main__":
    # Ruta del archivo
    ruta_archivo = r"C:\Users\javie\Desktop\Tareas\Teoria compu\P1TeoriaCompu\expresiones.txt"
    procesar_data(ruta_archivo)
