'''Implementação Recursiva
A implementação recursiva usa a definição matemática direta da sequência de Fibonacci.
Ela chama a si mesma até alcançar os casos base.'''

def fibonacci_recursivo(n):
    # Caso base: se n é 0, retorne 0
    if n == 0:
        return 0
    # Caso base: se n é 1, retorne 1
    elif n == 1:
        return 1
    # Caso recursivo: retorne a soma das duas chamadas recursivas
    else:
        return fibonacci_recursivo(n-1) + fibonacci_recursivo(n-2)

# Testando a função recursiva
for i in range(19):
    print(f"fibonacci_recursivo({i}) = {fibonacci_recursivo(i)}")
