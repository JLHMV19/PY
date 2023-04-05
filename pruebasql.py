import mysql.connector
import tkinter as tk
#ventana
window = tk.Tk()
window.geometry("300x100")
window.title("trae unas cawamas")

def llamada(): 
    mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="BadLands2045.",
  database="cawamonga"
)
    mycursor = mydb.cursor()
    sql = "INSERT INTO cawameros (nombre, apellido) VALUES (%s, %s)"
    val = str(valor1.get()), str(valor2.get())
    mycursor.execute(sql, val)
    mydb.commit()

def erradicacion():
    valor1.delete(0, tk.END)
    valor2.delete(0, tk.END)

def combi():
    llamada()
    erradicacion()

#valores a insertar
valor1l=tk.Label(window, text="inserta el nombre del cawamero")
valor1=tk.Entry(window)
valor1l.grid(row=0, column=0)
valor1.grid(row=0, column=1)
valor2l=tk.Label(window, text="inserta el apellido del cawamero")
valor2=tk.Entry(window)
valor2l.grid(row=1, column=0)
valor2.grid(row=1, column=1)
#botones
botoncito=tk.Button(window, text="decirle que traiga cawamas", command=combi)
botoncito.grid(row=3, column=0, columnspan=3)
 
window.mainloop()