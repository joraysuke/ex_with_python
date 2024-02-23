linha = 3
coluna = 3

matriz = []
soma = 1

for i in range(linha):
    linha = []
    for j in range(coluna):
        linha.append(soma)
        soma += 1

    matriz.append(linha)

for k in matriz:
    print(k)




