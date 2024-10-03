arrayNomes = [0]*5
arraySenha = [0]*5
tam = len(arrayNomes)

for r in range(tam):
    arrayNomes[r] = input("Digite seu nome:")
    arraySenha[r] = input("Digite sua senha:")

for k in range(tam):
    print(k, arrayNomes[k], arraySenha[k])