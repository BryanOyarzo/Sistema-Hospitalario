#Librerías de Interfaz
import tkinter as tk
from tkinter import messagebox
# Librerías de Archivos
import csv
import os
# Modulación
from doctores import Doctor
from salas import Sala
# Librerías Ciencia de Datos
import pandas as pd
class App:
    # Un init cualquiera...
    def __init__(self):
        self.w_main = tk.Tk()
        self.lc = ["Nombre", "Apellido", "Edad", "Rut"]
        self.doctor_array = []

    # Para ejecutar la ventana
    def windowExe(self):
        self.w_main.title("Sistema Hospitalario")
        self.w_main.geometry("800x350")
        self.w_main.resizable(False,False)

        # Variables para manipular la ubicación de la sección
        y = -30
        x = -50

        #region /// Labels de la Ventana Principal ///
        self.l_title = tk.Label(self.w_main, text="Sistema Hospitalario", font=("Arial", 22))
        self.l_title.place(x=275, y=10)

        self.l_description = tk.Label(self.w_main, text="Agregar Doctor", font=("Arial", 12))
        self.l_description.place(x=150+x, y=100+y)

        self.l_name = tk.Label(self.w_main, text="Nombre: ", font=("Arial", 12))
        self.l_name.place(x=75+x, y=130+y)

        self.l_lastname = tk.Label(self.w_main, text="Apellido: ", font=("Arial", 12))
        self.l_lastname.place(x=75+x, y=170+y)

        self.l_rut = tk.Label(self.w_main, text="Rut: ", font=("Arial", 12))
        self.l_rut.place(x=75+x, y=250+y)

        self.l_age = tk.Label(self.w_main, text="Edad: ", font=("Arial", 12))
        self.l_age.place(x=75+x, y=210+y)
        #endregion

        #region /// Botones de la Ventana Principal ///
        self.b_add = tk.Button(self.w_main, text="Agregar Doctor", command= lambda: self.addDoctor())
        self.b_add.place(x=100+x, y=290+y)

        self.b_view = tk.Button(self.w_main, text="Mostrar Lista", command= lambda: self.viewArray())
        self.b_view.place(x=200+x, y=290+y)

        self.b_export = tk.Button(self.w_main, text="Exportar CSV", command= lambda: self.csvExport(self.doctor_array))
        self.b_export.place(x=400+x, y=340+y)

        self.b_import = tk.Button(self.w_main, text="Importar CSV", command= lambda: self.importWindow())
        self.b_import.place(x=500+x, y=340+y)

        self.b_rooms = tk.Button(self.w_main, text="Gestión de Salas", command= lambda: self.roomGest())
        self.b_rooms.place(x=750+x, y=340+y)
        #endregion

        #region /// Textos de la Ventana Principal ///
        self.t_field = tk.Text(self.w_main, height=13, width=60)
        self.t_field.place(x=320+x, y=105+y)
        #endregion

        #region /// Entries de la Ventana Principal ///
        self.e_name = tk.Entry(self.w_main, width=20)
        self.e_name.place(x=150+x, y=130+y)

        self.e_lastname = tk.Entry(self.w_main, width=20)
        self.e_lastname.place(x=150+x, y=170+y)

        self.e_age = tk.Entry(self.w_main, width=20)
        self.e_age.place(x=150+x, y=210+y)

        self.e_rut = tk.Entry(self.w_main, width=20)
        self.e_rut.place(x=150+x, y=250+y)
        #endregion

        for entry in (self.e_name, self.e_lastname, self.e_age, self.e_rut):
            entry.bind("<Return>", self.focusNext)

        self.w_main.mainloop()
    
    # Función para poder importar csv
    def csvImport(self):
        try:
            with open("doctores.csv", newline="", encoding="utf-8") as file:
                content = csv.reader(file) # Llamamos al archivo en genera, ahora debemos separarlo en filas
                next(content) # Para no tomar en cuenta la cabecera del archivo y evitar problemas de formato
                self.t_field.delete("1.0", tk.END) # Borramos el contenido ya existente para mostrar el listado limpio

                # Esta parte de código será la que muestre el listado
                upper = f"{self.lc[0]:<10} | {self.lc[1]:<10} | {self.lc[2]:<5} | {self.lc[3]:<10}"
                self.t_field.insert(tk.END, upper + "\n")

                for row in content: # Separación de Filas del archivo
                    line = f"{row[0]:<10} | {row[1]:<10} | {row[2]:<5} | {row[3]:<10}"
                    self.t_field.insert(tk.END, line + "\n")

                    # Comprobamos si el doctor ya existe (por RUT, que debería ser único)
                    exists = any(doctor.rut == row[3] for doctor in self.doctor_array)

                    if exists:
                        print(f"Doctor con RUT {row[3]} ya existe.")
                    else:
                        # Si no existe, lo agregamos a la lista
                        nuevo_doctor = Doctor(row[0], row[1], row[2], row[3])
                        self.doctor_array.append(nuevo_doctor)

        except FileNotFoundError:
            messagebox.showerror("Error", "No se ha encontrado el archivo buscado, procura crearlo antes")
    
    # Para poder exportar a CSV
    def csvExport(self, doctor_array):
        # Creación del archivo CSV
        with open("doctores.csv", "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Nombre", "Apellido", "Edad", "Rut"])

            for d in doctor_array:
                writer.writerow([d.name, d.lastname, d.age, d.rut])

    # Ventana de Importación
    def importWindow(self):
        # Para la selección del archivo
        def selectedFile(event):
            selected_index = self.listbox.curselection()
            if selected_index:
                file = self.files[selected_index[0]]
                messagebox.showinfo("Archivo Seleccionado", f"Has seleccionado el siguiente archivo: {file}")
                self.w_import.destroy()

                # NO ESTOY SEGURO AÚN DE ESTA PARTE DE CÓDIGO   
                try:
                    with open(file, newline="", encoding="utf-8") as f:
                        content = csv.reader(f) # Llamamos al archivo en genera, ahora debemos separarlo en filas
                        next(content) # Para no tomar en cuenta la cabecera del archivo y evitar problemas de formato
                        self.t_field.delete("1.0", tk.END) # Borramos el contenido ya existente para mostrar el listado limpio

                        # Esta parte de código será la que muestre la cabecilla del listado
                        upper = f"{self.lc[0]:<10} | {self.lc[1]:<10} | {self.lc[2]:<5} | {self.lc[3]:<10}"
                        self.t_field.insert(tk.END, upper + "\n")

                        for row in content: # Separación de Filas del archivo
                            line = f"{row[0]:<10} | {row[1]:<10} | {row[2]:<5} | {row[3]:<10}"
                            self.t_field.insert(tk.END, line + "\n")

                            # Comprobamos si el doctor ya existe (por RUT, que debería ser único)
                            exists = any(doctor.rut == row[3] for doctor in self.doctor_array)

                            if exists:
                                print(f"Doctor con RUT {row[3]} ya existe.")
                            else:
                                # Si no existe, lo agregamos a la lista
                                new_doctor = Doctor(row[0], row[1], row[2], row[3])
                                self.doctor_array.append(new_doctor)

                except FileNotFoundError:
                    messagebox.showinfo("Error", "No se ha encontrado el archivo buscado, procura crearlo antes")
        #region Creación General de la Ventana
        # Creación de la ventana
        self.w_import = tk.Toplevel()
        self.w_import.geometry("375x300")
        self.w_import.title("Explorador de Archivos")

        # Creación de un Frame
        self.frame_place = tk.Frame(self.w_import)
        self.frame_place.pack()

        # Creación de Label
        self.lb_title = tk.Label(self.w_import, text="Explorador de Archivos", font=("Times New Roman", 16))
        self.lb_title.place(x=10, y=10)

        self.lb_desc = tk.Label(self.w_import, text="Selecciona un archivo: ", font=("Times New Roman", 12))
        self.lb_desc.place(x=10, y=30)

        # Creación de ListBox
        self.listbox = tk.Listbox(self.w_import, width=50)
        self.listbox.place(x=10, y=70)
        #endregion
        
        self.path = "./"
        self.extension = ".csv"

        self.files = [f for f in os.listdir(self.path) if f.endswith(self.extension)]

        # Esto insertará archivos en el listbox
        for file in self.files:
            self.listbox.insert(tk.END, file)

        self.listbox.bind("<Double-1>", selectedFile)

    # Para añadir un doctor
    def addDoctor(self):
        name = self.e_name.get()
        lastname = self.e_lastname.get()
        age = self.e_age.get()
        rut = self.e_rut.get()

        if any(d.rut == rut for d in self.doctor_array):
            print("Doctor ya registrado")
            messagebox.showerror("Error: Doctor ya registrado", "El rut introducido ya está registrado")
            return
        else: 
            doctor = Doctor(name, lastname, age, rut)
            print(f"Doctor {name} añadido.")
            messagebox.showinfo("Doctor registrado exitosamente", f"El Doctor {name} ha sido añadido con éxito.")
            self.doctor_array.append(doctor)
            self.t_field.delete("1.0", tk.END)
            self.t_field.insert(tk.END, "Nombre,Apellido,Edad,Rut\n")
            for d in self.doctor_array:
                line = f"{d.name:<10} | {d.lastname:<10} | {d.age:<5} | {d.rut:<10}"
                self.t_field.insert(tk.END, line + "\n")

    # Para poder ver el listado de forma ordenada
    def viewArray(self):
        self.t_field.delete("1.0", tk.END)
        self.t_field.insert(tk.END, "Nombre,Apellido,Edad,Rut\n")
        for d in self.doctor_array:
            line = f"{d.name:<10} | {d.lastname:<10} | {d.age:<5} | {d.rut:<10}"
            self.t_field.insert(tk.END, line + "\n")

    # Para poder presionar enter y pasar al siguiente entry
    def focusNext(self, event):
        """Mueve el foco al siguiente widget enfocable."""
        event.widget.tk_focusNext().focus()
        return "break"  # Evita que se ejecute la acción por defecto
    
    ### Función para poder visualizar y ordenar un DataFrame de salas utilizando Pandas
    ### Para ello crearemos una ventana nueva, la cual se abrirá como consecuencia
    ### de un botón.

    def roomGest(self):

        # Función para organizar los valores 
        def ordered(csv_path="salas.csv"):
            df = pd.read_csv(csv_path)
            ordered_df = df.sort_values(by="Capacidad", ascending=False)

            # Limpiar el campo de texto
            self.t_rooms.delete("1.0", tk.END)

            # Encabezado
            header = f"{'Sala':<10} | {'Capacidad':<10}\n"
            self.t_rooms.insert(tk.END, header)
            self.t_rooms.insert(tk.END, "-" * 25 + "\n")

            # Filas
            for _, row in ordered_df.iterrows():
                line = f"{row['Sala']:<10} | {row['Capacidad']:<10}\n"
                self.t_rooms.insert(tk.END, line)

        self.w_room = tk.Toplevel()
        self.w_room.title("Listado de Salas")
        self.w_room.geometry("300x300")
        self.w_room.resizable(False, False)

        # Campo de Texto para la Ventana
        self.t_rooms = tk.Text(self.w_room, width=30, height=10)
        self.t_rooms.place(x=10, y=50)

        # Label para la ventana
        self.l_title = tk.Label(self.w_room, text="Listado de Salas", font=("Arial", 16))
        self.l_title.place(x=10, y=10)

        # Botones de la Ventana
        self.b_numorg = tk.Button(self.w_room, text="Ordenar por Capacidad", command= ordered)
        self.b_numorg.place(x=50, y=250)

        #region Creación de las Salas
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
        #endregion
        
        # Este es el array que contiene todas las salas
        self.room_array = [
            sala1, sala2, sala3, sala4, sala5,
            sala6, sala7, sala8, sala9, sala10
            ]
        self.room_upper = ["Sala", "Capacidad"]

        # Esto guardará el listado en un archivo CSV, perfecto para su uso.
        Sala.guardar_las_salas(self.room_array)
        try:
            with open("salas.csv", newline="", encoding="utf-8") as f:
                content = csv.reader(f)
                next(content)
                self.t_rooms.delete("1.0", tk.END)

                # Mostrar listado
                upper = f"{self.room_upper[0]:<5} | {self.room_upper[1]:<5}"
                self.t_rooms.insert(tk.END, upper + "\n")

                for row in content:
                    line = f"{row[0]:<5} | {row[1]:<5}"
                    self.t_rooms.insert(tk.END, line + "\n")
                # Se comprueba si el número de la sala se repite
                exists = any(room.numero == row[0] for room in self.room_array)

                if exists:
                    print(f"La sala {row[0]} ya está registrada.")
                else:
                    new_room = Sala(row[0], row[1])
                    self.room_array.append(new_room)
        except FileNotFoundError:
            messagebox.showerror("Error", "No se ha encontrado el archivo, procura crearlo antes")
        