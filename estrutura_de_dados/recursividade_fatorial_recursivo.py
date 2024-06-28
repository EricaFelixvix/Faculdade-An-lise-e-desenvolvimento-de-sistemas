def fatorial_recursivo(n):
    # Inicializa a variável fat com 1, que será usada para os casos base
    fat = 1
    # Verifica se o número é negativo, caso seja retorna None
    if n < 0:
        return None
    # Se o número for 0 ou 1, o fatorial é 1
    elif n == 0 or n == 1:
        return fat
    else:
        # Retorna n multiplicado pelo fatorial de n - 1 (chamada recursiva)
        return n * fatorial_recursivo(n - 1)

# Testa a função com o valor 0, imprimindo o resultado
print(fatorial_recursivo(5))


'''Fatorial Recursivo:

No método recursivo, a função chama a si mesma para
calcular o fatorial:'''
