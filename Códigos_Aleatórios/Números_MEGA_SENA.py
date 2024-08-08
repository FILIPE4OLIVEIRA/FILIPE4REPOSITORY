# -*- coding: utf-8 -*-
"""
Created on Sat Jan 15 22:38:09 2020
@author: engoliveira
"""
# Sorteio de Números da Mega Sena

import random
import os
import itertools
import sys

def gerar_jogos(quantidade=10):
    jogos = []
    
    for _ in range(quantidade):
        numeros = set()
        while len(numeros) < 6:
            numeros.add(random.randint(1, 60))  # Gera números únicos

        jogo = sorted(f"{num:02}" for num in numeros)  # Ordena e formata os números como strings de dois dígitos
        jogos.append(jogo)
    
    return jogos

def obter_caminho_projeto():
    # Retorna o caminho do diretório do script atual
    return os.path.dirname(os.path.abspath(__file__))

def salvar_jogos(jogos):
    caminho_projeto = obter_caminho_projeto() 
    caminho_arquivo = os.path.join(caminho_projeto, "resultados.txt")
    
    # Abre o arquivo para escrita (substitui o conteúdo existente)
    with open(caminho_arquivo, "w") as arquivo_resultado:
        for jogo in jogos:
            linha = " ".join(jogo)  # Junta os números do jogo em uma string separada por espaços
            arquivo_resultado.write(linha + "\n")  # Escreve a linha no arquivo

def contar_tentativas(jogo_alvo):
    jogo_alvo = sorted(f"{int(num):02}" for num in jogo_alvo)  # Ordena e formata os números do jogo alvo
    tentativas = 0
    animacao = itertools.cycle(['|', '/',  '―', '\\'])  # Animação de progresso

    while True:
        tentativas += 1
        jogo_gerado = sorted(f"{random.randint(1, 60):02}" for _ in range(6))
        
        if tentativas % 10000 == 0:  # Atualiza a animação a cada 100.000 tentativas
            sys.stdout.write(f"\rProcurando o Jogo {jogo_alvo} {next(animacao)}")
            sys.stdout.flush()
        
        if jogo_gerado == jogo_alvo:  # Verifica se o jogo gerado é igual ao jogo alvo
            break
    
    print("\nJogo Encontrado!")
    return tentativas  # Retorna o número de tentativas necessárias para encontrar o jogo

def menu_principal():
    print("[1] Gerar Novos Jogos")
    print("[2] Contar Tentativas Para Encontrar um Jogo")
    opcao = input("Escolha uma Opção: ")

    if opcao == '1':
        quantidade = int(input("Quantos Jogos Deseja Gerar? "))
        jogos = gerar_jogos(quantidade)
        salvar_jogos(jogos)
        print(f"{len(jogos)} Jogos Salvos em 'resultados.txt'.")

    elif opcao == '2':
        jogo_alvo = input("Digite os 6 Números (Separados Por Espaço): ").split()
        
        if len(jogo_alvo) != 6:
            print("Erro: Você Deve Digitar Exatamente 6 Números.")
            return
        
        tentativas = contar_tentativas(jogo_alvo)
        print(f"Foram Necessárias {tentativas} Tentativas Para Encontrar o Jogo {jogo_alvo}.")
    else:
        print("Opção Inválida. Tente Novamente.")

if __name__ == "__main__":
    menu_principal()  # Executa o menu principal quando o script é executado diretamente
