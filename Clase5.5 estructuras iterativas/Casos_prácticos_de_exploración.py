lista = list(map(int, input("ingrese una lista de numeros:").split()))
a=0
for i in range(len(lista)):
    a+=lista[i]
print(a)