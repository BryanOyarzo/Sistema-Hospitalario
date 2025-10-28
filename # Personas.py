# Personas.py

class Persona:
    
    def __init__(self, name, lastname, age, rut):
        self._name = name
        self._lastname = lastname
        self._age = age
        # Encapsulamiento del RUT: Se almacena como atributo protegido
        self._rut = self._validar_rut(rut) 

    def _validar_rut(self, rut):
        """Método privado para asegurar que el RUT sea una cadena válida."""
        if not rut or not isinstance(rut, str):
            raise ValueError("El RUT debe ser una cadena de texto no vacía.")
        return rut.upper()

    # Getter para el RUT (Encapsulamiento: solo lectura externa)
    @property
    def rut(self):
        """Getter: Permite acceder al RUT, pero no modificarlo directamente."""
        return self._rut
    
    @property
    def nombre_completo(self):
        """Getter: Retorna el nombre y apellido completo."""
        return f"{self._name} {self._lastname}"
    
    # Método especial __str__
    def __str__(self):
        """Representación en string legible."""
        return f"Nombre: {self._name} {self._lastname}, Edad: {self._age}, RUT: {self.rut}"
    # Pacientes.py

from Personas import Persona
import numpy as np

class Paciente(Persona):
    """
    Clase Paciente que HEREDA de Persona. 
    Gestiona diagnósticos (Encapsulamiento) y calcula el desvío de temperatura (Numpy).
    """
    
    def __init__(self, name, lastname, age, rut, diagnostico_inicial, temperatura_inicial):¿
        # 1. HERENCIA: Llama al constructor de Persona (que ya maneja el encapsulamiento del RUT)
        super().__init__(name, lastname, age, rut) 
        
        # 2. ENCAPSULAMIENTO: Lista de diagnósticos (protegida)
        self._diagnosticos = [diagnostico_inicial] 
        
        # Historial de temperaturas (para el cálculo con Numpy)
        self._historial_temperatura = [temperatura_inicial] 
        
        # Estado del paciente
        self._estado = "Ingresado" 

    # Métodos de Encapsulamiento (Getters controlados)

    @property
    def diagnostico_actual(self):
        """Getter: Retorna el diagnóstico más reciente del paciente."""
        return self._diagnosticos[-1] 

    @property
    def historial_temperatura(self):
        """Getter: Retorna el historial de temperaturas para su uso fuera de la clase."""
        return self._historial_temperatura

    
    def calcular_desvio_temperatura(self):
        """
        Usa la librería Numpy para calcular la desviación estándar de las 
        temperaturas registradas. (REQUISITO NUMPY)
        """
        # El desvío solo es significativo si hay más de una medición.
        if len(self._historial_temperatura) < 2:
            return 0.0
        
        # Convertir la lista a un array de Numpy
        temperaturas_np = np.array(self._historial_temperatura)
        
        # Calcular el desvío estándar (np.std)
        desvio = np.std(temperaturas_np) 
        
        return round(desvio, 2)



    def agregar_diagnostico(self, nuevo_diagnostico):
        """Añade un nuevo diagnóstico al historial médico (Modificador controlado)."""
        self._diagnosticos.append(nuevo_diagnostico)

    def registrar_temperatura(self, temperatura: float):
        """Registra una nueva medición."""
        self._historial_temperatura.append(temperatura)

    def dar_alta(self):
        """Cambia el estado del paciente a 'Alta'."""
        self._estado = "Alta"



    def __str__(self):
        """Sobreescritura: Representación en string que incluye el desvío de Numpy."""
        # Se reutiliza el __str__ de la clase base Persona
        base_str = super().__str__() 
        
        return (f"Paciente | {base_str}, Diagnóstico: {self.diagnostico_actual}, "
                f"Estado: {self._estado}, Desvío Temp (Numpy): {self.calcular_desvio_temperatura()}°C")

