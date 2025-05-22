#Solicita una cadena de texto que representa una contraseña, y verifica si la contraseña
#cumple con las siguientes condiciones: tener al menos 8 caracteres, un número y una mayúscula

contra = input('ingrese su contraseña: ')
num= '0123456789'
minus ='abcdefghijklmnñopqrstuvwxyz'
mayus = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'
password = []
hay_numero = False
hay_minuscula=False
hay_mayuscula = False
for caracter in contra:
    if caracter in num:
        password.append(caracter)
        hay_numero = True
    if caracter in minus:
        password.append(caracter)
        hay_minuscula = True
    if caracter in mayus:
        password.append(caracter)
        hay_mayuscula = True
        
    # # # for i in num:
    # # #     for j in minus:
    # # #         for k in mayus:
    # # #              if caracter==i or caracter==j or caracter==k:
    # # #                 password.append(caracter)

print(password)
if hay_minuscula and hay_mayuscula and hay_numero and len(password)==len(contra) and len(contra)>=8:
    print("contraseña segura")
else:
    print("contraseña no segura, intente con otra")



# 2.3.2. Desarrollar un programa en Python que permita calcular el impuesto que debe
# pagar un usuario por el consumo de energía.
# El cálculo debe realizarse basado en la siguiente tabla.
# | Unidades consumidas	|     impuesto  		|
# -------------------------------------------
# |	    0 - 100				  |   sin impuesto	 	|
# |	    101 - 200			  | $0.70 por unidad 	|
# |	    201 o mas			  | $0.70 por unidad 	|

UC = float(input('ingrese cantidad de consumo: '))
if UC<=100:
    print("no debe pagar impuestos")
elif 101<=UC<200:
    print("debe pagar:", UC*0.7)
elif UC>201:
    print("debe pagar:", UC*0.7)
