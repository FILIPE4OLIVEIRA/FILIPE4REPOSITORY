# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 22:38:09 2019
@author: engoliveira

"""

# Lista de Números Primos

lista_primos = int(input("Digite um Número Limite: "))


odd_numbers = []       # impares
prime_numbers = [2]    # primos

for x in range(2, lista_primos + 1):                # Cria um lista de números Pares e Impares
    if (x % 2 != 0):
        odd_numbers.append(x)

for x in range(2, len(odd_numbers) + 1):
    for y in range(3, len(odd_numbers) + 1):  # Remove todos os múltiplos impares da lista
        z = y * x
        if (z in odd_numbers):
            odd_numbers.remove(z)

for x in odd_numbers:                   # Monta o vetor contendo todos os números
    for y in range(3, lista_primos + 1):        # com resto da divisão igual a zero
        if (x % y == 0):
            prime_numbers.append(x)

print("\n São %.i Números Primos até o Número %.i" % (len(prime_numbers),lista_primos))
print("\n A Lista de Números Primos é: ", str(prime_numbers))
