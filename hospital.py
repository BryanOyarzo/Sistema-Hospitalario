import pandas as pd
from doctores import Doctor
class Hospital:
    def __init__(self, name, c_rooms, csv_path="doctores.csv"):
        self.name = name
        self.csv_path = csv_path
        self._c_rooms = c_rooms
        self._doctors = pd.read_csv(csv_path)

    def add_doctors(self, doctor):
        new_doctor = {
            'Nombre': doctor.name,
            'Apellido': doctor.lastname,
            'Edad': doctor.age,
            'Rut': doctor.rut
        }
        # Para evitar que se repitan datos
        if new_doctor['Rut'] in self._doctors['Rut'].values: 
            print("Doctor ya registrado")
            return
        
        # Añadir Doctor
        self._doctors.loc[len(self._doctors)] = new_doctor
        self._doctors.to_csv(self.csv_path, index=False)
        return f"Doctor añadido al DataFrame"

    def get_doctors(self):
        return self._doctors

