#Ejercicio 3
from vehiculos import * 
import csv



particular= Particular("Ford", "Fiesta", 4, "180","500",5)
carga= Carga("Daft Truck", "G 38", 10, 120, "1000", "20000")
bicicleta= Bicicleta("Shimano","MT Ranger",2,"Carrera")
motocicleta= Motocicleta("BMW","F800s", 2, "Deportiva", "2T", "Doble Viga", 21)

lista_objetos=[particular, carga, bicicleta, motocicleta]


for i in range(len(lista_objetos)):
    lista_objetos[i].guardar_datos_csv()

print("")

for i in range(len(lista_objetos)):
    lista_objetos[i].leer_datos_csv()
