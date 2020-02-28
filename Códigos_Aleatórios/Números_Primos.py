# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 22:38:09 2019
@author: engoliveira

"""

# Lista de Números Primos

import numpy
import matplotlib.pyplot as plt

Numb = int(input("digite um número limite: "))

def Numeros_Primos(Numb):
    
    odd_numb = []       # impares
    even_numb = []      # pares
    prime_numb = [2]    # primos

    for x in range(2, Numb + 1):                # Cria um lista de números Pares e Impares
        if (x % 2 == 0):
            even_numb.append(x)
        else:
            odd_numb.append(x)

    for x in range(2, len(odd_numb) + 1):
        for y in range(3, len(odd_numb) + 1):  # Remove todos os múltiplos impares da lista
            z = y * x
            if (z in odd_numb):
                odd_numb.remove(z)

    for x in odd_numb:                         # Monta o vetor contendo todos os números com resto da divisão igual a zero
        for y in range(3, Numb + 1):
            if (x % y == 0):
                prime_numb.append(x)

    P1 = print("\n São %.i Números Primos até o %.i" % (len(prime_numb),Numb))
    P2 = print(" A lista de numeros primos é: ", str(prime_numb))

    # Plotagem do Gráfico dos Números Primos 
    plt.title('Gráfico dos Números Primos')
    plt.xlabel('EIXO X')
    plt.ylabel('EIXO Y')
    plt.plot(prime_numb, marker = 'H' , label = 'Números Primos', color = 'red', linestyle = 'dotted')
    plt.legend(loc = 'best')
    plt.grid()
    plt.show()

    return(P1,P2)

Numeros_Primos(Numb)
