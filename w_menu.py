#Librerías de Interfaz
import tkinter as tk
from tkinter import messagebox
# Librerías de Archivos
import csv
# Importación de módulos
from doctores import doctor_1, doctor_2, Doctor
from salas import Sala
from pacientes import cargar_pacientes_csv
import os

class App:
    # Un init cualquiera...
    def __init__(self):
        self.w_main = tk.Tk()
        self.doctor_array = [doctor_1, doctor_2]
        self.lc = ["Nombre", "Apellido", "Edad", "Rut"]

        self.salas_array = Sala.cargar_las_salas()

    # Para ejecutar la ventana
    def windowExe(self):
        self.w_main.title("Sistema Hospitalario")
        self.w_main.geometry("800x400")
        self.w_main.resizable(False,False)

        # Variables para manipular la ubicación de la sección
        y = -30
        x = -50

        #region /// Labels de la Ventana Principal ///
        self.l_title = tk.Label(self.w_main, text="Sistema Hospitalario", font=("Times New Roman", 22))
        self.l_title.place(x=275, y=10)

        self.l_description = tk.Label(self.w_main, text="Agregar persona", font=("Times New Roman", 12))
        self.l_description.place(x=150+x, y=100+y)

        self.l_name = tk.Label(self.w_main, text="Nombre: ", font=("Times New Roman", 12))
        self.l_name.place(x=75+x, y=130+y)

        self.l_lastname = tk.Label(self.w_main, text="Apellido: ", font=("Times New Roman", 12))
        self.l_lastname.place(x=75+x, y=170+y)

        self.l_rut = tk.Label(self.w_main, text="Rut: ", font=("Times New Roman", 12))
        self.l_rut.place(x=75+x, y=250+y)

        self.l_age = tk.Label(self.w_main, text="Edad: ", font=("Times New Roman", 12))
        self.l_age.place(x=75+x, y=210+y)
        #endregion

        #region /// Botones de la Ventana Principal ///
        self.b_add = tk.Button(self.w_main, text="Agregar Doctor", command= lambda: self.addDoctor())
        self.b_add.place(x=100+x, y=290+y)

        self.b_view = tk.Button(self.w_main, text="Mostrar Lista", command= lambda: self.viewArray())
        self.b_view.place(x=200+x, y=290+y)

        self.b_export = tk.Button(self.w_main, text="Exportar CSV", command= lambda: self.csvExport(self.doctor_array))
        self.b_export.place(x=400+x, y=370+y)

        self.b_import = tk.Button(self.w_main, text="Importar CSV", command= lambda: self.csvImport())
        self.b_import.place(x=500+x, y=370+y)

        self.b_salas = tk.Button(self.w_main, text="Mostrar Salas", command=self.viewSalas)
        self.b_salas.place(x=400+x, y=330+y)

        self.b_add_paciente = tk.Button(self.w_main, text="Agregar Paciente", command=self.addPaciente)
        self.b_add_paciente.place(x=100+x, y=330+y)

        self.b_pacientes = tk.Button(self.w_main, text="Mostrar Pacientes", command=self.viewPacientes)
        self.b_pacientes.place(x=280+x, y=330+y)
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

    # Para poder exportar a CSV
    def csvExport(self, doctor_array):
        # Creación del archivo CSV
        with open("doctores.csv", "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Nombre", "Apellido", "Edad", "Rut"])

            for d in doctor_array:
                writer.writerow([d.name, d.lastname, d.age, d.rut])
    
    # Para poder importar un CSV
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
            messagebox.showinfo("Error", "No se ha encontrado el archivo buscado, procura crearlo antes")

    # Para poder añadir un Doctor
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
            return doctor

    # Para poder ver el listado
    def viewArray(self):
        self.t_field.delete("1.0", tk.END)
        self.t_field.insert(tk.END, "Nombre,Apellido,Edad,Rut\n")
        for d in self.doctor_array:
            print(f"{d.name},{d.lastname},{d.age},{d.rut}")
            self.t_field.insert(tk.END, f"{d.name},{d.lastname},{d.age},{d.rut}\n")

    # para poder ver la lista de salas
    def viewSalas(self):
        self.t_field.delete("1.0", tk.END)
        self.t_field.insert(tk.END, "numero | capacidad\n")
        self.t_field.insert(tk.END, "-"*30 + "\n")

        if not self.salas_array:
            self.t_field.insert(tk.END, "no hay ninguna sala registrada\n")
        else:
            for s in self.salas_array:
                self.t_field.insert(tk.END, f"{s.get_numero():<10} | {s.get_capacidad():<10}\n")

    def addPaciente(self):
        nombre = self.e_name.get().strip()
        apellido = self.e_lastname.get().strip()
        edad = self.e_age.get().strip()
        rut = self.e_rut.get().strip()

        if not nombre or not apellido or not edad or not rut:
            messagebox.showerror("Error", "Debes completar todos los campos para agregar un paciente.")
            return

        # Valores por defecto
        diagnostico = "Pendiente"
        temperatura = 36.5
        estado = "Ingresado"

        # Verificamos si el archivo existe para escribir el encabezado
        file_exists = os.path.isfile("pacientes.csv")
        
        with open("pacientes.csv", "a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            if not file_exists:
                # Escribimos las 7 columnas
                writer.writerow(["nombre","apellido","edad","rut","diagnostico","temperatura","estado"])
            # Escribimos la fila con todas las columnas en orden
            writer.writerow([nombre, apellido, edad, rut, diagnostico, temperatura, estado])

        messagebox.showinfo("Paciente agregado", f"Paciente {nombre} {apellido} agregado al CSV.")
        
        # Limpiar entradas después de agregar
        self.e_name.delete(0, tk.END)
        self.e_lastname.delete(0, tk.END)
        self.e_age.delete(0, tk.END)
        self.e_rut.delete(0, tk.END)



    def viewPacientes(self):
        try:
            with open("pacientes.csv", newline="", encoding="utf-8") as file:
                reader = csv.reader(file)
                next(reader)  # Saltar cabecera

                self.t_field.delete("1.0", tk.END)
                self.t_field.insert(tk.END, "Nombre | Apellido | Edad | RUT | Diagnóstico | Temp\n")
                self.t_field.insert(tk.END, "-" * 50 + "\n")

                vacio = True
                for row in reader:
                    vacio = False
                    nombre, apellido, edad, rut, diagnostico, temperatura, _ = row
                    linea = f"{nombre:<10} | {apellido:<10} | {edad:<3} | {rut:<12} | {diagnostico:<12} | {temperatura:<5}\n"
                    self.t_field.insert(tk.END, linea)

                if vacio:
                    self.t_field.insert(tk.END, "No hay pacientes registrados.\n")

        except FileNotFoundError:
            messagebox.showwarning("Archivo no encontrado", "No se encontró el archivo 'pacientes.csv'.")

    # Para poder presionar enter y pasar al siguiente entry
    def focusNext(self, event):
        """Mueve el foco al siguiente widget enfocable."""
        event.widget.tk_focusNext().focus()
        return "break"  # Evita que se ejecute la acción por defecto