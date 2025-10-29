import numpy as np
import csv

#clase paciente se encargar de gestionar los datos basicos,
### almacena la temperatura del paciente y diagnosticos
class Paciente:
    def __init__(self, nombre, apellido, edad, rut, diagnostico_inicial, temperatura_inicial):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.rut = rut.upper()      
        self._diagnosticos = [diagnostico_inicial]
        self._historial_temperatura = [temperatura_inicial]
        self._estado = "Ingresado"




###getterss 
    def diagnostico_actual(self):
        """Retorna el diagnóstico más reciente."""
        return self._diagnosticos[-1]

    def historial_temperatura(self):
        """Retorna el historial de temperaturas."""
        return self._historial_temperatura

    def estado(self):
        """Retorna el estado actual."""
        return self._estado

# metodoss
    def calcular_desvio_temperatura(self):
        """Calcula el desvío estándar de las temperaturas con Numpy."""
        if len(self._historial_temperatura) < 2:
            return 0.0
        return round(np.std(np.array(self._historial_temperatura)), 2)

    def agregar_diagnostico(self, nuevo_diagnostico):
        """Agrega un nuevo diagnóstico al historial."""
        self._diagnosticos.append(nuevo_diagnostico)

    def registrar_temperatura(self, temperatura):
        """Registra una nueva temperatura."""
        self._historial_temperatura.append(temperatura)

    def dar_alta(self):
        """Cambia el estado del paciente a 'Alta'."""
        self._estado = "Alta"

#### string
    def __str__(self):
        return (f"Paciente: {self.nombre} {self.apellido}, Edad: {self.edad}, RUT: {self.rut}, "
                f"Diagnóstico actual: {self.diagnostico_actual()}, Estado: {self._estado}, "
                f"Desvío Temp: {self.calcular_desvio_temperatura()}°C")
    
def cargar_pacientes_csv(ruta):
    """Carga pacientes desde un archivo CSV y devuelve una lista de objetos Paciente."""
    lista_pacientes = []
    try:
        with open(ruta, newline='', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                paciente = Paciente(
                    nombre=fila["nombre"],
                    apellido=fila["apellido"],
                    edad=int(fila["edad"]),
                    rut=fila["rut"],
                    diagnostico_inicial=fila["diagnostico"],
                    temperatura_inicial=float(fila["temperatura"])
                )
                if fila.get("estado") == "Alta":
                    paciente.dar_alta()
                lista_pacientes.append(paciente)
    except FileNotFoundError:
        print(f"⚠️ No se encontró el archivo {ruta}. Se creará al guardar.")
    return lista_pacientes


def guardar_pacientes_csv(ruta, lista_pacientes):
    """Guarda la lista de pacientes en un archivo CSV."""
    with open(ruta, mode="w", newline='', encoding='utf-8') as archivo:
        campos = ["nombre", "apellido", "edad", "rut", "diagnostico", "temperatura", "estado"]
        escritor = csv.DictWriter(archivo, fieldnames=campos)
        escritor.writeheader()

        for p in lista_pacientes:
            escritor.writerow({
                "nombre": p.nombre,
                "apellido": p.apellido,
                "edad": p.edad,
                "rut": p.rut,
                "diagnostico": p.diagnostico_actual(),
                "temperatura": p.historial_temperatura()[-1],
                "estado": p.estado()
            })
