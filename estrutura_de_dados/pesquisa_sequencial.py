''' PESQUISA SEQUENCIAL
Vamos supor que você e um amigo estão jogando um jogo de adivinhação de
números, no qual seu amigo gostaria que você adivinhasse o número que está
pensando dentro de um intervalo de 1 a 100 valores. A cada tentativa sua,
seu amigo irá indicar se o valor está baixo ou alto em relação ao que ele
pensou.'''

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
print(dados)
buscando = int(input("Digite o valor que deseja burcar: "))
achou = buscaSequencial(dados, buscando)
if achou == - 1:
    print("Valor não encontrado. ")
else:
    print(f"Valor encontrado na posição {achou}.")