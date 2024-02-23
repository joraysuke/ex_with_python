c = int(input('Digite a quantidade de colunas da matriz: '))
l = int(input('Digite a quantidade de linhas da matriz: '))

matriz = []


for j in range(l):
    linha = []
    for i in range(c):
        linha.append(int(input()))

    matriz.append(linha)


for k in matriz:
    print(k)

