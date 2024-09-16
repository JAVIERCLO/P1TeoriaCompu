#Implementacion de shunting yard
def shunting_yard(expresion):
    precedencia = {'*': 3, '.': 2, '|': 1}
    #Pila para exoresuon postfix
    salida = []
    #Pila para procesar precedencia de operadores
    operadores = []
    #Funcion para comprobar si un caracter es operador
    def es_operador(c):
        return c in precedencia
    #Funcion para comprobar precedencia de operadores
    def precedencia_mayor_igual(op1, op2):
        return precedencia.get(op1, 0) >= precedencia.get(op2, 0)
    #Ciclo para procesar la expresion infix
    for c in expresion:
        if c.isalnum() or c == 'ε':
            salida.append(c)
        elif c == '(':
            operadores.append(c)
        elif c == ')':
            while operadores and operadores[-1] != '(':
                salida.append(operadores.pop())
            operadores.pop()
        else:
            while operadores and operadores[-1] != '(' and precedencia_mayor_igual(operadores[-1], c):
                salida.append(operadores.pop())
            operadores.append(c)
    
    while operadores:
        salida.append(operadores.pop())
    #Unir la expresion en una cadena
    return ''.join(salida)