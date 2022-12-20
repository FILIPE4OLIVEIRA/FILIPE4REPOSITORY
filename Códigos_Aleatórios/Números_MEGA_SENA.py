# -*- coding: utf-8 -*-
"""
Created on Sat Jan 15 22:38:09 2020
@author: engoliveira
"""
# Sorteio de Números da Mega Sena

import random

def numeros_mega(h=10):
	lista_numeros = []
	lista_jogos = []
	for i in range(h):
		lista_numeros.clear()
		while(len(lista_numeros)<6):
			X = random.randint(1,60)
			if(X not in lista_numeros):
				lista_numeros.append(X)

		lista_numeros.sort()
		for j in range(6):
			if(lista_numeros[j]<10):
				lista_numeros[j] = str("0" + str(lista_numeros[j]))
			else:
				lista_numeros[j] = str(lista_numeros[j])
		
		lista_string = lista_numeros.copy()
		lista_jogos.append(lista_string)
		lista_jogos.append(lista_string)
	
	index = 0
	while(lista_jogos[index] in lista_jogos):
			lista_jogos.remove(lista_jogos[index])
			if(index + 1 < len(lista_jogos)):
				index = index + 1
			else:
				break

	return(lista_jogos)

def grava_dados(lista_jogos):
	ArquivoResult = open(r"C:/Users/filipe.cardoso/Desktop/JogosMega.txt", "a")
	ArquivoResult = open(r"C:/Users/filipe.cardoso/Desktop/JogosMega.txt","w+")
	for i in range(len(lista_jogos)):
		ArquivoResult.writelines(str(lista_jogos[i]) + "\n")
	ArquivoResult.close()


lista_jogos = numeros_mega(int(input("Quantos Sorteios Deseja Realizar? ")))
grava_dados(lista_jogos)

