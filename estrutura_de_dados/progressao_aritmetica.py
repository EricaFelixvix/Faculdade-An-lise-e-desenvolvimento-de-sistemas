def pa(a1, r, n):
    """
    Gera os primeiros n termos de uma Progressão Aritmética (PA).

    :param a1: Primeiro termo da PA
    :param r: Razão da PA
    :param n: Número de termos
    :return: Lista dos primeiros n termos da PA
    """
    pa_sequence = []
    for i in range(n):
        an = a1 + i * r
        pa_sequence.append(an)
    return pa_sequence

# Exemplo de uso
primeiro_termo = 2
razao = 3
num_termos = 10

pa_sequence = pa(primeiro_termo, razao, num_termos)
print("Progressão Aritmética (PA):", pa_sequence)

