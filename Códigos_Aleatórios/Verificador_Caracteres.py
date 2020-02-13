# Desafio DSA 1 [string com caracteres iguais]


palavra = input("digite uma palavra:")

tamanho = len(palavra)
var1 = 1
var2 = 0

for x in range(0,tamanho):
	for y in range(var1,tamanho):
		if palavra[x] == palavra[y]:
			print("xpalavra[%d] == ypalavra[%d]" %(x,y))
			var2 = 1
		else:
			print("xpalavra[%d] != ypalavra[%d]" %(x,y))
	var1 = var1 + 1

if var2 == 1:
	print("A palavra possui caracteres iguais!")
else:
	print("A palavra não possui caracteres iguais!")

print(palavra)




