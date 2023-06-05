from vehiculos import *

particular= Particular("Ford", "Fiesta", 4, "180","500",5)
carga= Carga("Daft Truck", "G 38", 10, 120, "1000", "20000")
bicicleta= Bicicleta("Shimano","MT Ranger",2,"Carrera")
motocicleta= Motocicleta("BMW","F800s", 2, "Deportiva", "2T", "Doble Viga", 21)
lista_objetos=[particular, carga, bicicleta, motocicleta]

while True:
    
    try:
        ejercicio=int(input("¿Qué ejercicio quieres ejecutar?(1,2,3  y 4 para salir): "))
        print("")
        if ejercicio == 1:
            nvehiculos=int(input("¿Cuantos Vehivulos desea insertar?: "))
            garaje= []
            for i in range(1,nvehiculos+1):
                print(f"Vehiculo {i}")
                auto= Automovil(input("Ingrese marca: "), input("Ingrese modelo: "), input("Ingrese nruedas: "),input("Ingrese velocidad: "),input("Ingrese cilindrada: "))
                garaje.append(auto)

            for indice, item in enumerate(garaje):
                print(f'Datos del automóvil {indice+1}: Marca {item.marca}, modelo {item.modelo}, {item.nruedas} ruedas, {item.velocidad} km/h, {item.cilindrada} CC')

        elif ejercicio == 2:
            for i in lista_objetos:
                print(i)
            print("")
            print(f'Motocicleta es instancia con relación a Vehículo: {isinstance(motocicleta,Vehiculo)}')
            print(f'Motocicleta es instancia con relación a Automovil: {isinstance(motocicleta,Automovil)}')
            print(f'Motocicleta es instancia con relación a Vehículo particular: {isinstance(motocicleta, Particular)}') 
            print(f'Motocicleta es instancia con relación a Vehículo de Carga: {isinstance(motocicleta,Carga)}') 
            print(f'Motocicleta es instancia con relación a Bicicleta: {isinstance(motocicleta, Bicicleta)}') 
            print(f'Motocicleta es instancia con relación a Motocicleta: {isinstance(motocicleta, Motocicleta)}')

        elif ejercicio == 3:
            for i in range(len(lista_objetos)):
                lista_objetos[i].guardar_datos_csv()

            print("")

            for i in range(len(lista_objetos)):
                lista_objetos[i].leer_datos_csv()

        elif ejercicio == 4:
            break
        else:
            print("Opción invalida")
    except ValueError:
            print("")
            print("Opción inexistente")
            print("")
print("")
print("Adiós")