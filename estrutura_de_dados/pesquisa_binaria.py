
'''Pesquisa Binária
A pesquisa binária é um algoritmo eficiente para encontrar um valor 
em uma lista ordenada. Ela funciona dividindo repetidamente a lista
ao meio e comparando o valor do meio com o valor que está sendo 
buscado. Se o valor buscado for menor que o valor do meio, a busca
continua na metade esquerda; se for maior, continua na metade direita.
Esse processo se repete até encontrar o valor ou até que a 
sublista seja vazia. A pesquisa binária tem um tempo de execução de 
O(logn), o que a torna muito rápida para listas grandes.'''

def buscaBinaria(inicio, fim, dados, buscando):
    while inicio <= fim:
        meio = int((inicio + fim) / 2)
        if buscando > dados[meio]:
            inicio = meio + 1
        elif buscando < dados[meio]:
            fim = meio - 1
        else:
            return meio
    return -1

import random
# Gerando os valores dentro do intervalo.
dados = random.sample(range(10), 10)
dados.sort()  # Ordena os dados para a busca binária
print(dados)
buscando = int(input("Digite o valor que deseja buscar: "))

# Chamando a função de busca binária com os argumentos corretos
achou = buscaBinaria(0, len(dados) - 1, dados, buscando)
if achou == -1:
    print("Valor não encontrado.")
else:
    print(f"Valor encontrado na posição {achou}.")
