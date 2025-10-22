from doctores import Doctor
from hospital import Hospital
import tkinter as tk

lista_doctores = []
w_main = tk.Tk()
w_main.title("Sistema Hospitalario")
w_main.geometry("400x300")

def addDoctor():
    name = e_name.get()
    lastname = e_lastname.get()
    age = e_age.get()
    rut = e_rut.get()

    if any(d.rut == rut for d in lista_doctores):
        print("Doctor ya registrado")
        return
    else: 
        doctor = Doctor(name, lastname, age, rut)
        print(f"Doctor {name} añadido.")
        lista_doctores.append(doctor)
        return doctor

def viewArray():
    for d in lista_doctores:
        print(f"Nombre: {d.name} {d.lastname} | Edad: {d.age} | Rut: {d.rut}")

# /// Labels de la Ventana Principal ///
l_title = tk.Label(w_main, text="Sistema Hospitalario", font=("Times New Roman", 16))
l_title.place(x=110, y=10)

l_description = tk.Label(w_main, text="Agregar Doctor", font=("Times New Roman", 12))
l_description.place(x=150, y=50)

l_name = tk.Label(w_main, text="Nombre: ", font=("Times New Roman", 12))
l_name.place(x=75, y=80)

l_lastname = tk.Label(w_main, text="Apellido: ", font=("Times New Roman", 12))
l_lastname.place(x=75, y=120)

l_rut = tk.Label(w_main, text="Rut: ", font=("Times New Roman", 12))
l_rut.place(x=75, y=200)

l_age = tk.Label(w_main, text="Edad: ", font=("Times New Roman", 12))
l_age.place(x=75, y=160)

# /// Botones de la Ventana Principal ///
b_add = tk.Button(w_main, text="Agregar Doctor", command= lambda: addDoctor())
b_add.place(x=100, y=240)

b_view = tk.Button(w_main, text="Mostrar Lista", command= lambda: viewArray())
b_view.place(x=200, y=240)

# /// Entries de la Ventana Principal ///
e_name = tk.Entry(w_main, width=20)
e_name.place(x=150, y=80)

e_lastname = tk.Entry(w_main, width=20)
e_lastname.place(x=150, y=120)

e_age = tk.Entry(w_main, width=20)
e_age.place(x=150, y=160)

e_rut = tk.Entry(w_main, width=20)
e_rut.place(x=150, y=200)


# Creación de Doctor de Ejemplo
doctor_1 = Doctor("Bryan", "Oyarzo", 19, "22182594-2")
print(doctor_1.get_all_info())
w_main.mainloop()