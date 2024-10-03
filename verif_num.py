arrayNum = [0]*10

tam = len(arrayNum)


for r in range(tam):
    arrayNum[r] = input("Digite um número:")

arrayNum2 = input("Digite um novo número:")

quant = 0
for k in range(tam):
    if arrayNum2 == arrayNum[k]:
        quant += 1

print(quant)








