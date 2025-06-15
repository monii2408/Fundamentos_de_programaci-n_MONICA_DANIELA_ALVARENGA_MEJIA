# matriz = int(input("ingrese la proporcion de la matriz: "))

# binaria = []

# new_matriz=[]


# for i in range(matriz):
    #size = list(map(int, input("Ingrese los datos de la matriz: ").split()))
   # binaria.append(size)

#for m in range(len(binaria)):
   # lista_contador=[]
    #for n in range(len(binaria[m])):
        #contador=0

        
        # if m<0 or m>=len(binaria) or n<0 or n>= len(binaria[0]):
        #     contador=False
            
        # movimientos = [(0,-1), (-1,1), (0,1), (1,1), (1,0)]
        # x=binaria[m][n]
        # if binaria[m-1][0]=='1':
        #     contador+=1
        # if binaria[m][0]=='1':
        #     contador+=1
        # if binaria[0][n-1]=='1':
        #     contador+=1
        # if binaria[1][1]=='1':
        #     contador+=1

       # lista_contador.append(contador)

#for i in range(matriz):
    # size = list(map(int, lista_contador.split()))
    # new_matriz.append(size)

#print(binaria)

n=int(input())
m=int(input())

d=[]
for i in range(n):
    d.append(list(map(int, input().split(","))))
