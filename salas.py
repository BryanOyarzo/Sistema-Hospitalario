import pandas as pd

class Sala:
    def __init__(self, numero, capacidad):
        self.numero = numero
        self.capacidad = capacidad

    def __str__(self):
        return f"sala {self.numero} | capacidad: {self.capacidad}"

    def __repr__(self):
        return self.__str__()

    # getters
    def get_numero(self):
        return self.numero

    def get_capacidad(self):
        return self.capacidad

    # setters
    def set_numero(self, nuevo_numero):
        self.numero = nuevo_numero
        return f"el numero de la sala fue actualizado al {self.numero}"

    def set_capacidad(self, nueva_capacidad):
        self.capacidad = nueva_capacidad
        return f"la capacidad de la sala fue cambiada a {self.capacidad}"



    def guardar_las_salas(lista_salas, archivo="salas.csv"):
        data = [{"numero": s.get_numero(), "capacidad": s.get_capacidad()} for s in lista_salas]
        df = pd.DataFrame(data)
        df.to_csv(archivo, index=False, encoding="utf-8")


    def cargar_las_salas(archivo="salas.csv"):
        try:
            df = pd.read_csv(archivo, encoding="utf-8")
            salas = [Sala(str(row["numero"]), str(row["capacidad"])) for _, row in df.iterrows()]
            return salas
        except FileNotFoundError:
            return []
        

if __name__ == "__main__":

    # lista de las salas
    sala1 = Sala("101", 2)
    sala2 = Sala("102", 3)
    sala3 = Sala("103", 1)
    sala4 = Sala("104", 8)
    lista_salas = [sala1, sala2, sala3 , sala4]


    # guardado en csv
    Sala.guardar_las_salas(lista_salas)

    # cargar y mostrar
    for s in Sala.cargar_las_salas():
        print(s)