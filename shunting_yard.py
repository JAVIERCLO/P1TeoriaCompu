def shunting_yard(expresion):
    precedencia = {'*': 3, '.': 2, '|': 1}
    salida = []
    operadores = []
    
    def es_operador(c):
        return c in precedencia
    
    def precedencia_mayor_igual(op1, op2):
        return precedencia.get(op1, 0) >= precedencia.get(op2, 0)
    
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
    
    return ''.join(salida)