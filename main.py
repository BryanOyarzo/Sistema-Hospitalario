from doctores import Doctor
from hospital import Hospital
import tkinter as tk
from tkinter import messagebox
import pandas as pd
import numpy as np
import csv

# Para manipular toda la ubicación de la sección "Añadir Doctor"
y = -30
x = -50

# Creación de unos objetos Doctor para tener una lista de ejemplo predeterminada
doctor_1 = Doctor("Bryan", "Oyarzo", 19, "22182594-2")
doctor_2 = Doctor("Camila", "Hernandéz", 21, "21142467-2")

lista_doctores = [
    doctor_1, doctor_2
]
w_main = tk.Tk()
w_main.title("Sistema Hospitalario")
w_main.geometry("800x350")
w_main.resizable(False,False)

# Para exportar a csv
def csvExport(lista_doctores):

    # Creación del archivo CSV
    with open("doctores.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Nombre", "Apellido", "Edad", "Rut"])

        for d in lista_doctores:
            writer.writerow([d.name, d.lastname, d.age, d.rut])

def csvImport():
    try:
        with open("doctores.csv", newline="", encoding="utf-8") as file:
            content = csv.reader(file) # Llamamos al archivo en genera, ahora debemos separarlo en filas
            t_field.delete("1.0", tk.END) # Borramos el contenido ya existente para mostrar el listado limpio
            for row in content: # Separación de Filas
                line = f"{row[0]:<10} | {row[1]:<10} | {row[2]:<5} | {row[3]:<10}"
                t_field.insert(tk.END, line + "\n")

    except FileNotFoundError:
        messagebox.showinfo("Error", "No se ha encontrado el archivo buscado, procura crearlo antes")

def addDoctor():
    name = e_name.get()
    lastname = e_lastname.get()
    age = e_age.get()
    rut = e_rut.get()

    if any(d.rut == rut for d in lista_doctores):
        print("Doctor ya registrado")
        messagebox.showerror("Error: Doctor ya registrado", "El rut introducido ya está registrado")
        return
    else: 
        doctor = Doctor(name, lastname, age, rut)
        print(f"Doctor {name} añadido.")
        messagebox.showinfo("Doctor registrado exitosamente", f"El Doctor {name} ha sido añadido con éxito.")
        lista_doctores.append(doctor)
        return doctor

def viewArray():
    t_field.delete("1.0", tk.END)
    t_field.insert(tk.END, "Nombre,Apellido,Edad,Rut\n")
    for d in lista_doctores:
        print(f"{d.name},{d.lastname},{d.age},{d.rut}")
        t_field.insert(tk.END, f"{d.name},{d.lastname},{d.age},{d.rut}\n")

#region /// Labels de la Ventana Principal ///
l_title = tk.Label(w_main, text="Sistema Hospitalario", font=("Times New Roman", 22))
l_title.place(x=275, y=10)

l_description = tk.Label(w_main, text="Agregar Doctor", font=("Times New Roman", 12))
l_description.place(x=150+x, y=100+y)

l_name = tk.Label(w_main, text="Nombre: ", font=("Times New Roman", 12))
l_name.place(x=75+x, y=130+y)

l_lastname = tk.Label(w_main, text="Apellido: ", font=("Times New Roman", 12))
l_lastname.place(x=75+x, y=170+y)

l_rut = tk.Label(w_main, text="Rut: ", font=("Times New Roman", 12))
l_rut.place(x=75+x, y=250+y)

l_age = tk.Label(w_main, text="Edad: ", font=("Times New Roman", 12))
l_age.place(x=75+x, y=210+y)
#endregion

#region /// Botones de la Ventana Principal ///
b_add = tk.Button(w_main, text="Agregar Doctor", command= lambda: addDoctor())
b_add.place(x=100+x, y=290+y)

b_view = tk.Button(w_main, text="Mostrar Lista", command= lambda: viewArray())
b_view.place(x=200+x, y=290+y)

b_export = tk.Button(w_main, text="Exportar CSV", command= lambda: csvExport(lista_doctores))
b_export.place(x=400+x, y=340+y)

b_import = tk.Button(w_main, text="Importar CSV", command= lambda: csvImport())
b_import.place(x=500+x, y=340+y)
#endregion

#region /// Textos de la Ventana Principal ///
t_field = tk.Text(w_main, height=13, width=60)
t_field.place(x=320+x, y=105+y)
#endregion

#region /// Entries de la Ventana Principal ///
e_name = tk.Entry(w_main, width=20)
e_name.place(x=150+x, y=130+y)

e_lastname = tk.Entry(w_main, width=20)
e_lastname.place(x=150+x, y=170+y)

e_age = tk.Entry(w_main, width=20)
e_age.place(x=150+x, y=210+y)

e_rut = tk.Entry(w_main, width=20)
e_rut.place(x=150+x, y=250+y)
#endregion

w_main.mainloop()