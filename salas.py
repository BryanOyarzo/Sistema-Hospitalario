import pandas as pd

### la clase sala representa una sala de hospital,
#####cada sala tiene un numero para indentificarlo y una capacidad maxima.
class Sala:
    def __init__(self, numero, capacidad):
        self.numero = numero
        self.capacidad = capacidad

    def __str__(self):
        return f"Sala: {self.numero} | En uso: {self.uso} | Capacidad: {self.capacidad}"

    def __repr__(self):
        return self.__str__()

   # # getters / devuelve el numero de la sala
    def get_numero(self):
        return self.numero
### devuelve la capacidad maxima de la sala
    def get_capacidad(self):
        return self.capacidad

    # setters / actualiza el numero identificador de la sala
    def set_numero(self, nuevo_numero):
        self.numero = nuevo_numero
        return f"el numero de la sala fue actualizado al {self.numero}"
### actualiza la capacidad maxima de la sala 
    def set_capacidad(self, nueva_capacidad):
        self.capacidad = nueva_capacidad
        return f"la capacidad de la sala fue cambiada a {self.capacidad}"

### Guarda una lista Sala en un archivo csv,
##### Contiene el numero indentificado y la capacidad maxima de cada sala
    def guardar_las_salas(lista_salas, archivo="salas.csv"):
        data = [{"Sala": s.get_numero(), "Capacidad": s.get_capacidad()} for s in lista_salas]
        df = pd.DataFrame(data)
        df.to_csv(archivo, index=False, encoding="utf-8")

### Carga las salas desde un archivo csv
##### Entrega una lista de objetos en Sala, 
####### si el archivo no esta te devuelve una lista vacia
    def cargar_las_salas(archivo="salas.csv"):
        try:
            df = pd.read_csv(archivo, encoding="utf-8")
            salas = [Sala(str(row["Sala"]), str(row["Capacidad"])) for _, row in df.iterrows()]
            return salas
        except FileNotFoundError:
            return []

#prueba de salas.py
if __name__ == "__main__": # Esto es para que solamente se ejecute a través del main

    # lista de las salas
    sala1 = Sala("101", 2)
    sala2 = Sala("102", 3)
    sala3 = Sala("103", 1)
    sala4 = Sala("104", 8)
    sala5 = Sala("105", 2)
    sala6 = Sala("106", 3)
    sala7 = Sala("107", 1)
    sala8 = Sala("108", 8)
    sala9 = Sala("109", 2)
    sala10 = Sala("110", 3)
    lista_salas = [
        sala1, sala2, sala3, sala4, sala5,
        sala6, sala7, sala8, sala9, sala10
        ]


    # guardar en csv
    Sala.guardar_las_salas(lista_salas)

    # cargar y imprimir
    for s in Sala.cargar_las_salas():

        print(s)