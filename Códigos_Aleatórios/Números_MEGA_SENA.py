# -*- coding: utf-8 -*-
"""
Created on Sat Jan 15 22:38:09 2020
@author: engoliveira
"""

# Sorteio de Números da Mega Sena

import random


def numeros_mega(h=30):
    numb = []
    AllNumbs = []
    for i in range(h):
        numb.clear()
        while(len(numb)<6):
            X = random.randint(1,60)
            if(X in numb):
                numb.remove(X)
            else:
                numb.append(X)
                
        numb.sort()
        
        for j in range(6):
            if(numb[j]<10):
                numb[j] = str("0" + str(numb[j]))
            else:
                numb[j] = str(numb[j])
        
        Numb2 = numb.copy()
        AllNumbs.append(Numb2)
        print(numb)
    
    return(AllNumbs)

AllNumbs = numeros_mega(int(input("Quantos Sorteios Deseja Realizar? ")))

ArquivoResult = open(r"C:/PythonCodes/JogosMega.txt","a")
ArquivoResult = open(r"C:/PythonCodes/JogosMega.txt","w+")
for i in range(len(AllNumbs)):
    ArquivoResult.writelines(str(AllNumbs[i]) + "\n")
ArquivoResult.close()
print("FINISH!")
