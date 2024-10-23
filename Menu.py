# import app 
import customtkinter as ctk
import tkinter as tk 
from tkinter import messagebox

def salir():
    ventan.quit() 

def acerca_de():
    messagebox.showinfo("Acerca de", "Aplicacion previa")

def enviar_nombre():
    nombre = entrada_nombre.get()
    etiqueta_resultado.configure(text = f"Hola {nombre}")

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

ventan =ctk.CTk()
ventan.title("Aplicacion del Clima B&B")
ventan.geometry("500x300")

menuBar =tk.Menu(ventan)

archivo_menu = tk.Menu(menuBar, tearoff=0)
archivo_menu.add_command(label="Nuevo")
archivo_menu.add_command(label="Abrir")
archivo_menu.add_command(label="Guardar")
archivo_menu.add_separator()
archivo_menu.add_command(label="Salir", command=salir)
menuBar.add_cascade(label="Archivo", menu=archivo_menu)

editar_menu =tk.Menu(menuBar, tearoff=0)
editar_menu.add_command(label="Copiar")
editar_menu.add_command(label="Pegar")
menuBar.add_cascade(label="Editar", menu=editar_menu)

ayuda_menu =tk.Menu(menuBar, tearoff=0)
ayuda_menu.add_command(label="Acerca de", command=acerca_de)
menuBar.add_cascade(label="Editar", menu=ayuda_menu)

ventan.config(menu=menuBar)

etiqueta_instruccion = ctk.CTkLabel(ventan,text="Introduce tu nombre",font=("Arial",14))
etiqueta_instruccion.pack(pady=20)

entrada_nombre = ctk.CTkEntry(ventan,width=250,font=("Arial",14))
entrada_nombre.pack(pady=10)

boton_enviar = ctk.CTkButton(ventan,text="Enviar", command=enviar_nombre, width=200,height=50)
boton_enviar.pack(pady=20)

etiqueta_resultado = ctk.CTkLabel(ventan, text="", font=("Arial", 16))
etiqueta_resultado.pack(pady=20)

ventan.mainloop()

