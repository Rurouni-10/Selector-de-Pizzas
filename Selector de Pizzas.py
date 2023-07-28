import tkinter
window = tkinter.Tk()
window.title("Selector de Pizzas")
window.geometry("400x500")
window.minsize(200,400)
window.config(bg="wheat")
titulo = tkinter.Label(bg="lightgreen", fg="darkblue", padx=30, pady=10,
                       text="Variedades de Pizzas", font="Times 26 bold",
                       relief="solid", bd=3)
titulo.pack(pady=10)
##### Primer Cuadro ####
Seleccionador = tkinter.LabelFrame(window, bg="wheat", relief="solid", bd=5)
Seleccionador.pack()

valor_seleccionado= tkinter.StringVar()
valor_seleccionado.set(None)

def seleccion():
    pizza_seleccionada = valor_seleccionado.get()
    if pizza_seleccionada == "a":
        resultado = "Napolitana"
    elif pizza_seleccionada == "b":
        resultado = "Calabresa"
    elif pizza_seleccionada == "c":
        resultado = "Especial"
    elif pizza_seleccionada == "d":
        resultado = "4 Quesos"
    elif pizza_seleccionada == "e":
        resultado = "Fugazzetta"
    else:
        resultado = "No hay Seleccion"
    Mensaje_en_Pantalla.config(text=f"Su Pizza elegida es: \n{resultado}")
    Elegir["state"] = "disable"
    Reinicio["state"] = "normal"
def reiniciar():
    valor_seleccionado.set(None)
    Mensaje_en_Pantalla.config(text="Elija su Pizza")
    Reinicio["state"] = "disable"
    Elegir["state"] = "normal"
#### Opciones ####
opcion_1= tkinter.Radiobutton(Seleccionador, bg="wheat", text="Napolitana",
                              variable=valor_seleccionado, value="a",
                              font="Times 18 bold", justify="left", width=10,
                              anchor="w")
opcion_1.pack()

opcion_2= tkinter.Radiobutton(Seleccionador, bg="wheat", text="Calabresa",
                              variable=valor_seleccionado, value="b",
                              font="Times 18 bold", justify="left", anchor="w",
                              width=10)
opcion_2.pack()

opcion_3= tkinter.Radiobutton(Seleccionador, bg="wheat", text="Especial",
                              variable=valor_seleccionado, value="c",
                              font="Times 18 bold", justify="left", anchor="w",
                              width=10)
opcion_3.pack()

opcion_4= tkinter.Radiobutton(Seleccionador, bg="wheat", text="4 Quesos    ",
                              variable=valor_seleccionado, value="d",
                              font="Times 18 bold", justify="left", anchor="w",
                              width=10)
opcion_4.pack()

opcion_5= tkinter.Radiobutton(Seleccionador, bg="wheat", text="Fugazzetta",
                              variable=valor_seleccionado, value="e",
                              font="Times 18 bold", justify="left", anchor="w",
                              width=10)
opcion_5.pack()
##### Segundo Cuadro ####

Elegir= tkinter.Button(window, text="Elegir",bg="lightgreen",
                         relief="groove", bd=6, width=10, fg="darkblue",
                         font="Arial 18 bold", command=seleccion)
Elegir.pack(pady=10)

Reinicio= tkinter.Button(window, text="Reiniciar",bg="lightgreen",
                         relief="groove", bd=6, width=10, fg="darkblue",
                         font="Arial 18 bold", command=reiniciar)
Reinicio.pack(pady=10)
#### Pizza Seleccionada ####

Mensaje_en_Pantalla= tkinter.Label(window, text="Elija su Pizza",
                                   font="Arial 18 bold",justify="center",
                                   relief="solid", bg="wheat")
Mensaje_en_Pantalla.pack(pady=10)
window.mainloop()