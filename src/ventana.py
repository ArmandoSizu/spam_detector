import tkinter as tk
from tkinter import messagebox

def mostrar_mensaje():
    messagebox.showinfo("aviso","holabb")

ventana= tk.Tk()
ventana.title("ventana prueba")

label = tk.Label(ventana, text="holabb")
label.pack(pady=10)

boton= tk.Button(ventana,text="holabb",command=mostrar_mensaje)
boton.pack(pady=10)

ventana.mainloop()