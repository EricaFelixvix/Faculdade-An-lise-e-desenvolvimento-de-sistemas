def fatorial_iterativo(n):
    # Inicializa a variável fat com 1, que será usada para calcular o fatorial
    fat = 1
    # Verifica se o número é negativo, caso seja retorna None
    if n < 0:
        return None
    # Se o número for 0 ou 1, o fatorial é 1
    elif n == 0 or n == 1:
        return fat
    else:
        # Loop de 1 até n, multiplicando fat por cada número no intervalo
        for i in range(1, n + 1):
            fat = fat * i
        # Retorna o valor do fatorial calculado
        return fat

# Testa a função com o valor 6, imprimindo o resultado
print(fatorial_iterativo(5))


'''
Fatorial Iterativo:

O fatorial de um número é o produto de todos os
inteiros positivos de 1 até esse número. No método
iterativo, usamos um loop para calcular esse produto:'''