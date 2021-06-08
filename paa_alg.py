import matplotlib.pyplot as plt
from random import randint
from timeit import timeit
import pandas as pd

from numpy.lib.function_base import append
from pandas.core.indexes import multi


plt.style.use('seaborn')


# Plot do gráfico
def plot_grafico(entradas, tgma, kara):

    fig, ax = plt.subplots()
    ax.plot(entradas, tgma, '-b', label='Divisão e conquista')
    ax.plot(entradas, kara, '--r', label='Karatsuba')

    ax.set_title('Grafico de tempo de execução')
    plt.legend()

    plt.xlabel('Quantidade de digitos na entrada')
    plt.ylabel('Tempo de Execução(ms)')
    plt.show()


# Retorna um número aleatório de n digitos
def numgen(n):
    valor = []
    valor.append(str(randint(1, 9)))
    for i in range(n-1):
        valor.append(str(randint(1, 9)))

    return int("".join(valor))


# Multiplicação com algoritmo de karatsuba
def karatsuba(a, b):
    if a < 10 or b < 10:
        return a*b
    else:
        a = str(a)
        b = str(b)

        n = max(len(a), len(b))
        n2 = n//2

        a_split = len(a)-n2
        b_split = len(b)-n2

        a_esq = int(a[:a_split])
        a_dir = int(a[a_split:])
        b_esq = int(b[:b_split])
        b_dir = int(b[b_split:])

        x1 = karatsuba(a_esq, b_esq)
        x2 = karatsuba(a_esq+a_dir, b_esq+b_dir)
        x3 = karatsuba(a_dir, b_dir)

        return x1 * 10**(2*n2) + (x2-x1-x3) * 10**n2 + x3


# Multiplicação por divisão e conquista
def divide_mult(a, b):
    if a < 10 or b < 10:
        return a*b
    else:
        a = str(a)
        b = str(b)

        n = max(len(a), len(b))
        n2 = n//2

        a_lens = len(a)-n2
        b_lens = len(b)-n2

        a_esq = int(a[:a_lens])
        a_dir = int(a[a_lens:])
        b_esq = int(b[:b_lens])
        b_dir = int(b[b_lens:])

        x1 = divide_mult(a_esq, b_esq)
        x2 = divide_mult(a_esq, b_dir)
        x3 = divide_mult(a_dir, b_esq)
        x4 = divide_mult(a_dir, b_dir)

        return x1*10**(2*n2)+(x2+x3)*10**n2+x4


# execução principal
def main(n):
    df = pd.DataFrame(columns=['digitos', 'num', 'multi', 'karatsuba'])

    for i in range(n+1):
        if i > 1:
            val = numgen(i)

            a = timeit(lambda: divide_mult(val, val), number=1)*1000
            b = timeit(lambda: karatsuba(val, val), number=1)*1000
            df.loc[i, :] = [i, val, a, b]

    plot_grafico(df['digitos'], df['multi'], df['karatsuba'])


main(500)
