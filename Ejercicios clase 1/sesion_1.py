#Pide al usuario el total de una cuenta y el porcentaje de propina (por ejemplo, 10%, 15%, 20%).
#Calcula y muestra en pantalla el total a pagar.

# cuenta = float(input("ingrese el total de su cuenta:"))
# porcentaje = input("Cuanta propina quisiera dar")

# propina = cuenta*(float(porcentaje)/100)

# print('Su total a pagar con propina es:', cuenta+propina)


#Solicita al usuario su nombre completo (asume dos nombres y dos apellidos).
#Luego, el programa generará, su correo con el formato:
#primer_nombre.primer_apellido@keyinstitute.edu.sv

# nombre_completo = str(input('Ingrese su nombre completo:'))
# lista_nombre = list(nombre_completo.split())
# correo_generator = f'{lista_nombre[0]}.{lista_nombre[2]}@keyinstitute.edu.sv'
# print('su correo institucional es:', correo_generator)

#Dados tres enteros a, b y k, imprime el resultado de a / b con k decimales exactos (sin redondear).

# a, b= map(float, input('ingrese dos numeros:').split())
# k = int(input("ingrese la cantidad de decimales que quiere:"))
# num = a/b
# d = f"{num:.{k}f}"
# print(d)

#Dados dos números enteros positivos muy grandes como cadenas de texto A y B. Calcula (A + B) e imprímelo como cadena de texto.
# A, B = map(str, input("ingrese dos numeros:").split())
# print(str(float(A)+float(B)))

#Dado un arreglo de n fracciones (representadas como cadenas "a/b"), calcula la suma total y expresa el resultado como una fracción irreducible.
array = []
fracciones = list(map(float, input('ingrese una fraccion').split()))
array.append(fracciones)

suma = 0
for i in array:
    suma += i

print(suma)

