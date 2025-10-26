#Librerías de Interfaz
import tkinter as tk
from tkinter import messagebox
# Librerías de Archivos
import csv
# Importación de módulos
from doctores import doctor_1, doctor_2, Doctor

class App:
    # Un init cualquiera...
    def __init__(self):
        self.w_main = tk.Tk()
        self.doctor_array = [doctor_1, doctor_2]
        self.lc = ["Nombre", "Apellido", "Edad", "Rut"]

    # Para ejecutar la ventana
    def windowExe(self):
        self.w_main.title("Sistema Hospitalario")
        self.w_main.geometry("800x350")
        self.w_main.resizable(False,False)

        # Variables para manipular la ubicación de la sección
        y = -30
        x = -50

        #region /// Labels de la Ventana Principal ///
        self.l_title = tk.Label(self.w_main, text="Sistema Hospitalario", font=("Times New Roman", 22))
        self.l_title.place(x=275, y=10)

        self.l_description = tk.Label(self.w_main, text="Agregar Doctor", font=("Times New Roman", 12))
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
        self.b_export.place(x=400+x, y=340+y)

        self.b_import = tk.Button(self.w_main, text="Importar CSV", command= lambda: self.csvImport())
        self.b_import.place(x=500+x, y=340+y)
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

    # Para poder presionar enter y pasar al siguiente entry
    def focusNext(self, event):
        """Mueve el foco al siguiente widget enfocable."""
        event.widget.tk_focusNext().focus()
        return "break"  # Evita que se ejecute la acción por defecto