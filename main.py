#Ejercicio 1
from vehiculos import *

nvehiculos=int(input("¿Cuantos Vehivulos desea insertar?: "))

garaje= []
for i in range(1,nvehiculos+1):
    print(f"Vehiculo {i}")
    auto= Automovil(input("Ingrese marca: "), input("Ingrese modelo: "), input("Ingrese nruedas: "),input("Ingrese velocidad: "),input("Ingrese cilindrada: "))
    garaje.append(auto)

for indice, item in enumerate(garaje):
     print(f'Datos del automóvil {indice+1}: Marca {item.marca}, modelo {item.modelo}, {item.nruedas} ruedas, {item.velocidad} km/h, {item.cilindrada} CC')