def pg(a1, q, n):
    """
    Gera os primeiros n termos de uma Progressão Geométrica (PG).
    
    :param a1: Primeiro termo da PG
    :param q: Razão da PG
    :param n: Número de termos
    :return: Lista dos primeiros n termos da PG
    """
    pg_sequence = []
    for i in range(n):
        an = a1 * (q ** i)
        pg_sequence.append(an)
    return pg_sequence

# Exemplo de uso
primeiro_termo = 3
razao = 2
num_termos = 10

pg_sequence = pg(primeiro_termo, razao, num_termos)
print("Progressão Geométrica (PG):", pg_sequence)
