import matplotlib.pyplot as plt
import numpy as np
from random import randint
from timeit import timeit

from numpy.lib.function_base import append


plt.style.use('seaborn')
plt.rcParams['figure.figsize'] = (11, 7)


def plot_grafico(entradas, tgma, kara):

    fig, ax = plt.subplots()
    ax.plot(entradas, tgma, '-b', label='Divisão e conquista')
    ax.plot(entradas, kara, '--r', label='Karatsuba')

    ax.set_title('Grafico de tempo de execução')
    plt.legend()

    plt.xlabel('Quantidade de algarismos na entrada')
    plt.ylabel('Tempo de Execução')
    plt.show()


def numgen(n):
    valor = []
    valor.append(str(randint(1, 9)))
    for i in range(n-1):
        valor.append(str(randint(1, 9)))

    return int("".join(valor))


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


vet = []

for i in range(1, 50):
    vet.append(i)

tempos_divide = []
tempos_karatsuba = []

for valor in vet:
    valor = numgen(valor)

    tempos_divide.append(
        timeit(lambda: divide_mult(valor, valor), number=200))

    tempos_karatsuba.append(
        timeit(lambda: karatsuba(valor, valor), number=200))

plot_grafico(vet, tempos_divide, tempos_karatsuba)
