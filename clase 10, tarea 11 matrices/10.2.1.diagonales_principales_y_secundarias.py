matriz = int(input("ingrese las dimensiones de la matrix"))

matriz_vacia = []

for i in range(matriz):
    tamaño = list(map(int, input().split()))
    matriz_vacia.append(tamaño)

diagonal_principal = []
diagonal_secundaria = []

for i in range(len(matriz_vacia)):
    for j in range(len(matriz_vacia[i])):
        if i==j:
            diagonal_principal.append(matriz_vacia[i][j])
        if i + j == len(matriz_vacia)-1:
            diagonal_secundaria.append(matriz_vacia[i][j])

print(f"Diagonal principal: {diagonal_principal}")
print(f"Diagonal secundaria: {diagonal_secundaria}")