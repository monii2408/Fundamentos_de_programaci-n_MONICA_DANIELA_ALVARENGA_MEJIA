import numpy as np

consumo = np.array([
    [12.5, 13.2, 11.9, 14.0, 13.5, 15.0, 14.3],
    [10.1, 10.5, 10.0, 11.2, 11.5, 12.0, 11.8],
    [14.0, 14.2, 13.9, 15.5, 15.1, 16.0, 15.8],
    [9.0, 9.2, 8.9, 9.5, 9.8, 10.0, 9.7],
    [16.2, 16.5, 16.0, 17.1, 17.4, 18.0, 17.8],
    [11.0, 11.3, 11.1, 12.0, 12.4, 12.8, 12.5],
    [13.5, 13.8, 13.2, 14.1, 14.6, 15.0, 14.9],
    [10.8, 11.0, 10.6, 11.5, 11.8, 12.2, 12.0],
    [15.1, 15.5, 15.0, 16.0, 16.4, 17.0, 16.7],
    [8.5, 8.7, 8.4, 9.0, 9.2, 9.5, 9.3],
])


print("Dimensiones:", consumo.ndim)                   
print("Forma:", consumo.shape)                        
print("Tipo de datos:", consumo.dtype)    #float64 (decimales)
print("Consumo primer hogar:", consumo[0])   #todos los datos de la fila 0
print("Consumo el miercoles (dia 3):",consumo[:,2])  #todos los datos de la columna 2

promedio_por_hogar = np.mean(consumo, axis=1)    #axis = 0 es para "column wise"
promedio_por_dia = np.mean(consumo, axis = 0)    #axis = 1 es para "row wise"
total_consumo = np.sum(consumo)

print(promedio_por_hogar)
print(promedio_por_dia)
print(total_consumo)

maximos = np.max(consumo, axis=1)
minimos = np.min(consumo, axis=0)
desviacion = np.std(consumo)

print(maximos)
print(minimos)
print(desviacion)

consumo_total_hogar = np.sum(consumo, axis=1)
hogar_mayor_consumo = np.argmax(consumo_total_hogar)
hogar_mas_eficiente = np.argmin(consumo_total_hogar)

print(consumo_total_hogar)
print(hogar_mayor_consumo)
print(hogar_mas_eficiente)

consumo_total_hogar = np.sum(consumo, axis=1)
print(f"Consumo total de cada hogar durante la semana: {consumo_total_hogar}")

altos = consumo_total_hogar > 100

consumo_mayor_100 = np.where(altos)[0]

print(f"ids de hogares con consumo mayor a 100: {consumo_mayor_100}")

consumo_normalizado = (consumo - consumo.min()) / (consumo.max() - consumo.min())

print(consumo_normalizado)

#CUESTIONARIO DE TRABAJO

#1. ¿Cuál es el consumo del hogar 5 el viernes (día 5)?
hogar5_viernes = consumo[4,4]
print(f"El consumo del hogar 5 el dia viernes fue de {hogar5_viernes} kWh")

#2. Usando indexación, muestra el consumo de los últimos 3 hogares el domingo.
ultimos_3hogares_domingo = consumo[[7, 8, 9], 6]
print(f"el consumo de los últimos 3 hogares el domingo fue: {ultimos_3hogares_domingo}")

# 3. Calcula el promedio de consumo los fines de semana (sábado y domingo, columnas 5 y 6).
promedio_sabado_domingo = np.mean(consumo[:,[5,6]], axis = 0)
print(f"El promedio de consumo los fines de semana es de: {promedio_sabado_domingo}")

# 4. ¿Qué día de la semana tiene la mayor desviación estándar entre hogares? Explica qué indica esto.
dias={0 : "lunes", 1 : "martes", 2:"miercoles", 3:"jueves", 4:"viernes", 5:"sabado", 6:"domingo"}
desviacion_por_dia = np.std(consumo, axis=0)
desviacion_mayor = max(desviacion_por_dia)
indice_mayor_desviacion = np.where(desviacion_por_dia == desviacion_mayor)[0]
for i in indice_mayor_desviacion:
    print(f"La desviacion mayor es el dia  {dias[i]}") 
 #Esto indica que tanto varian los datos por dia, es decir que el dia sabado cada hogar tiene consumos muy diferentes entre ellos, es decir algunos consumieron muchos, y otros muy poco.

# 5. Identifica los 3 hogares con menor consumo total durante la semana. Muestra sus índices y valores.
#ya esta el consumo total por dia
hogares_menor_consumo = np.argsort(consumo_total_hogar)[:3] #para agarrar los primeros 3
#para mostrar los 3
print("los 3 hogares con menor consumo")
for i in hogares_menor_consumo:
   print(f"hogar {i} = {consumo_total_hogar[i]}")
# 6. Si el hogar 3 aumenta su consumo en un 10% cada día, ¿cuál sería su nuevo consumo total semanal?
hogar3 = consumo[2]
hogar3_aumento = hogar3 + (hogar3/10)
print(f"Si el consumo del hogar 3 aumentara un 10% cada dia, su nuevo total de consumo semanal fuese de {np.sum(hogar3_aumento)}")
