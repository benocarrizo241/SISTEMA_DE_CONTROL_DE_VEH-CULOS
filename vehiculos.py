import csv
class Vehiculo():
    def __init__(self, marca, modelo,nruedas):
        self.marca=marca
        self.modelo=modelo
        self.nruedas=nruedas
    def __str__(self):
        return f"Marca {self.marca}, Modelo {self.modelo}, ruedas: {self.nruedas}"
    
    def guardar_datos_csv(self):
        try:
            with open("vehiculos.csv", "a",newline="") as archivo:
                #Se crea un diccionario
                datos = [(self.__class__, self.__dict__)] # se crea una lista de listas, cada una guarda la clase y el diccionario con los datos
                archivo_csv = csv.writer(archivo) 
                archivo_csv.writerows(datos) 
        except FileNotFoundError:
            print("No existe el archivo vehiculos.csv")
        except Exception as e:
            print("Error reportado: ", e)

    def leer_datos_csv(self):
        try:
            with open("vehiculos.csv", "r") as archivos:
                vehiculos= csv.reader(archivos) # se lee todo el contenido del csv, y se guarda en una listas
                print(f"Listas deVehiculos {type(self).__name__}") # se le pregunta la metodo ¿de que clase eres tu?
                #print(str(self.__class__))
                for item in vehiculos:
                    vehiculo_tipo=str(self.__class__)# dedicmos que es la clase de quien llamo (contendra Particular, carga, etc)
                    if vehiculo_tipo in item[0]: # se busca, por ejemplo particular, dentro de la lista, el cual tendra objetos de tipo <class 'Vehiculo.Particular'>,"{'marca': 'Ford', 'modelo': 'Fiesta', 'nro_ruedas': '4', 'velocidad': '180', 'cilindraje': '500', 'nro_puestos': '5'}"
                        print(item[1]) 
                    
        except FileNotFoundError:
                print("No existe el archivo vehiculos.csv")
        except Exception as e:
                print("Error reportado: ", e)
#----------- AUTOMOVIL --------------------------

class Automovil(Vehiculo):
    def __init__(self, marca, modelo,nruedas,velocidad,cilindrada):
        super().__init__( marca, modelo,nruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
    def __str__(self):
        return Vehiculo.__str__(self)+ f" velocidad: {self.velocidad} km/h, cilindraje: {self.modelo} cc"
    

class Carga(Automovil):
    def __init__(self, marca, modelo,nruedas,velocidad,cilindrada,peso):
        super().__init__( marca, modelo,nruedas,velocidad,cilindrada)
        self.peso=peso
    def get_carga(self):
        return self.peso
    
    def set_npuestos(self,peso_new):
        self.peso = peso_new
    
    def __str__(self):
        return Automovil.__str__(self) + f"Carga: {self.peso}"

class Particular(Automovil):
    def __init__(self, marca, modelo,nruedas,velocidad,cilindrada,npuestos):
        super().__init__( marca, modelo,nruedas,velocidad,cilindrada)
        self.npuestos=npuestos
    
    def get_npuestos(self):
        return self.npuestos
    
    def set_npuestos(self,npuesto_new):
        self.npuestos = npuesto_new
    
    def __str__(self):
        return Automovil.__str__(self) + f"Puestos: {self.npuestos}"

#----------- BICICLETA --------------------------

class Bicicleta(Vehiculo):
    def __init__(self, marca, modelo,nruedas,tipo):
        super().__init__( marca, modelo,nruedas)
        self.tipo=tipo
    
    def __str__(self):
        return Vehiculo.__str__(self)+f"Tipo: {self.tipo}"
    
class Motocicleta(Bicicleta):
    def __init__(self, marca, modelo,nruedas,tipo, nro_radio, cuadro, motor):
        super().__init__( marca, modelo,nruedas,tipo)
        self.nro_radio = nro_radio
        self.cuadro = cuadro
        self.motor = motor
    def __str__(self):
        return Bicicleta.__str__(self)+f"N° Radio: {self.nro_radio}, Cuadro: {self.cuadro}, Motor: {self.motor}"