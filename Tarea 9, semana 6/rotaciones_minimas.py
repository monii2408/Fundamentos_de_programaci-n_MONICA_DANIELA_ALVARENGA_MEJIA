# Rotaciones minimas

numeros = list(map(int, input('ingrese conjunto de numeros: ').split()))
i = 0
numero_rotaciones=0
ordenado = numeros.sort()

while numeros != ordenado:
    a = numeros[0]
    numeros.remove(numeros[0])
    numeros.append(a)
    numero_rotaciones+=1
    if numero_rotaciones>len(numeros) and numeros!=ordenado:
        print("-1")
        break

if numeros == ordenado:
    print(numero_rotaciones)