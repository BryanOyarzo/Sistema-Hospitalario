import pandas as pd

class Doctor:
    def __init__(self, name, lastname, age, rut):
        self.name = name
        self.lastname = lastname
        self.age = age
        self.rut = rut

    # Getters --- Estos métodos son para que el cliente pueda consultar la información del doctor !
    #region ///// Métodos de obtención individuales de cada atributo /////
    def get_name(self):
        return f"Nombre del Doctor: {self.name} {self.lastname}"
    
    def get_age(self):
        return f"Edad del Doctor {self.name}: {self.age}"
    
    def get_rut(self):
        return f"Rut del Doctor {self.name}: {self.rut}"
    #endregion

    # ///// Método para poder visualizar toda la información del personal /////
    def get_all_info(self):
        return f"""
    DATOS DE PERSONAL
    Nombre: {self.name}
    Apellido: {self.lastname}
    Edad: {self.age}
    Rut: {self.rut}"""

    #region ///// Setters de cada método correspondiente /////
    
    def set_name(self, new_name):
        self.name = new_name
        return f"Nombre cambiado a {self.name}"

    def set_lastname(self, new_lstname):
        self.lastname = new_lstname
        return f"Apellido cambiado a {self.lastname}"

    def set_age(self, new_age):
        self.age = new_age
        return f"Edad actualizada a {self.age}"

    def set_run(self, new_rut):
        self.rut = new_rut
        return f"Rut Actualizado: {self.rut}"

    #endregion