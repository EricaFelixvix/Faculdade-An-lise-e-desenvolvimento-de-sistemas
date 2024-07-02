'''Implementação Iterativa
A implementação iterativa usa um loop para calcular a sequência, armazenando
os valores intermediários em variáveis.'''

def fibonacci_iterativo(n):
    # Caso base: se n é 0, retorne 0
    if n == 0:
        return 0
    # Caso base: se n é 1, retorne 1
    elif n == 1:
        return 1
    else:
        # Inicializa os dois primeiros números da sequência
        a, b = 0, 1
        # Calcula a sequência até o n-ésimo termo
        for _ in range(2, n+1):
            a, b = b, a + b
        return b

# Testando a função iterativa
for i in range(19):
    print(f"fibonacci_iterativo({i}) = {fibonacci_iterativo(i)}")
