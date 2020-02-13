
# Constante Kaprekar

import math 

numb1 = int(input("digite um número de 4 digitos: "))
numb = 0
while(numb != 6174):

    lista_numb1 = list(str(numb1))
    lista_numb2 = list(str(numb1))

    lista_numb1.sort()

    lista_numb2.sort()
    lista_numb2.reverse()


    numb1 = int(str(lista_numb1[0]+lista_numb1[1]+lista_numb1[2]+lista_numb1[3]))
    numb2 = int(str(lista_numb2[0]+lista_numb2[1]+lista_numb2[2]+lista_numb2[3]))

    numb = numb2 - numb1  
    
    print("%s - %s = %s" %(str(numb2),str(numb1),str(numb)))
    
    numb1 = numb