# Numeros lideres

numeros = list(map(int, input('ingrese conjunto de numeros: ').split()))
lideres = []
i = 0
for i in range(len(numeros)):
    if numeros[i-1]<numeros[i]>numeros[i+1]:
        lideres.append(numeros[i])
print(lideres)