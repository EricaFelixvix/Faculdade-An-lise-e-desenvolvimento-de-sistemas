''' PESQUISA SEQUENCIAL
A pesquisa sequencial, também conhecida como busca linear, é um método simples para encontrar um valor em uma lista. 
Ela funciona verificando cada elemento da lista, um por um, do início ao fim, até encontrar o valor desejado ou até que todos os
elementos tenham sido examinados.
Se o valor for encontrado, a pesquisa retorna a posição do valor na lista; caso contrário, indica que o valor não está presente. 
A pesquisa sequencial tem um tempo de execução deO(n) , onde 
é o número de elementos na lista, o que pode ser ineficiente para listas grandes.
'''

# Programa princípal.
import random
def buscaSequencial(dados, buscando):
    achou = 0
    i = 0

    while(((i < len(dados))) and (achou == 0 )):
        if(dados[i] == buscando):
            achou = 1
        else:
            i = i + 1
    if(achou == 0):
        return - 1
    else:
        return i + 1

# gerando os valores dentro do randon(intervalo).
dados = random.sample(range(10), 10)
dados.sort()
print(dados)
buscando = int(input("Digite o valor que deseja burcar: "))
achou = buscaSequencial(dados, buscando)
if achou == - 1:
    print("Valor não encontrado. ")
else:
    print(f"Valor encontrado na posição {achou}.")