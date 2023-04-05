import tkinter as tk

ventana = tk.Tk()
ventana.geometry("300x300")
etiqueta = tk.Label(ventana, text="¡Hola, mundo!")
boton = tk.Button(ventana, text="Haz clic aquí")
entrada = tk.Entry(ventana)

etiqueta.pack()
boton.pack()
entrada.pack()


ventana.mainloop()