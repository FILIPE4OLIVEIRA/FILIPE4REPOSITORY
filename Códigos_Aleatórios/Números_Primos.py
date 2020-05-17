# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 22:38:09 2019
@author: engoliveira

"""

# Lista de Números Primos

numb = int(input("Digite um Número Limite: "))

odd_numb = []       # impares
even_numb = []      # pares
prime_numb = [2]    # primos

for x in range(2, numb + 1):                # Cria um lista de números Pares e Impares
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
    for y in range(3, numb + 1):
        if (x % y == 0):
            prime_numb.append(x)

print("\n São %.i Números Primos até o Número %.i" % (len(prime_numb),numb))
print("\n A Lista de Números Primos é: ", str(prime_numb))
