#Importar funciones
from shunting_yard import shunting_yard
from afn import construir_AFN
from afd import convertir_AFD
from minimizacion import minimizar_AFD
from graficos import graficar

def procesar_expresion(expresion):
    try:
        #Convierte la expresion infix a postfix
        postfix = shunting_yard(expresion)  
        
        
        afn = construir_AFN(postfix)  
        
        # Verifica el contenido de afn
        print(f"AFN generado para la expresión '{expresion}': {afn}")
        print(f"Estados del AFN: {afn.estados}")
        print(f"Estado inicial: {afn.inicio}")
        print(f"Estado de aceptación: {afn.aceptacion}")
        
        #Generar un nombre al archivo para evitar errores
        nombre_archivo = f'AFN_{expresion}'
        print(f"Nombre de archivo generado: {nombre_archivo}")
        
        #Generar los grafos de los automatas
        graficar(afn, nombre_archivo)
    except Exception as e:
        print(f"Error procesando la expresión '{expresion}': {e}")

def procesar_data(ruta_archivo):
    with open(ruta_archivo, 'r') as archivo:
        for linea in archivo:
            #Procesar la expresion regular
            expresion = linea.strip()
            procesar_expresion(expresion)

if __name__ == "__main__":
    #Ruta del archivo
    ruta_archivo = r"C:\Users\javie\Desktop\Tareas\Teoria compu\P1TeoriaCompu\expresiones.txt"
    
    #Leer el archivo
    procesar_data(ruta_archivo)
