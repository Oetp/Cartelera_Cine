import tkinter as tk

ventana = tk.Tk()

ventana.title("Cartelera de Cine")
ventana.geometry("1920x1080")

texto = tk.Label(ventana,
                 text="🎬 CARTELERA DE CINE 🎬", #este texto va adentro de ventana
                 font=("Arial", 20)
                 )
texto.grid(row=0, column=0)

#Foto de la izq

imagen1 = tk.PhotoImage(file="C:/Users/matpe/Downloads/Foto png/Death note.png")

foto1 = tk.Label(ventana, image=imagen1)
foto1.place(x=100, y=100)




nombre1 = tk.Label(ventana, text="Death Note " , font=("Times New Roman", 15), fg="Black" )
nombre1.place(x=280, y=650)


nombre1_2 = tk.Label(ventana, text="130 min " , font=("Verdana", 15), fg="Black" )
nombre1_2.place(x=280, y=680)

nombre2_3 = tk.Label(ventana,
                     text="-Quedan 2 Boletas " ,
                     font=("Verdana", 8),
                     fg="Black")
nombre2_3.place(x=280, y=710)


#Foto de derecha

imagen2 = tk.PhotoImage(file="C:/Users/matpe/Downloads/Foto png/Angel.png")

foto2 = tk.Label(ventana, image=imagen2)
foto2.place(x=1200, y=300)



nombre2 = tk.Label(ventana, text="Santificado " , font=("Times New Roman", 15), fg="Black")
nombre2.place(x=1350, y=650)


nombre2_2 = tk.Label(ventana,
                     text="-140 min " ,
                     font=("Verdana", 15),
                     fg="Black")
nombre2_2.place(x=1350, y=680)

nombre2_3 = tk.Label(ventana,
                     text="-Quedan 5 Boletas " ,
                     font=("Verdana", 8),
                     fg="Black")
nombre2_3.place(x=1350, y=710)




texto1 = tk.Label(ventana, text = "Ingresa que pelicula quieres ver " , font=("Times New Roman", 30), fg="Black")
texto1.place(x=620, y=400)

entrada1 = tk.Entry(ventana, font=("Times New Roman", 15))
entrada1.place(x=730, y=460)





entrada2 = tk.Entry(ventana, font=("Times New Roman", 15) , fg = "Red")
entrada2.place(x=730, y=690)

texto2 = tk.Label(ventana, text = "Cuantas boletas quieres?  " , font=("Times New Roman", 20), fg="Black")
texto2.place(x=700, y=630)


#Disponibilidad

texto3 = tk.Label(ventana, text = "Disponible hasta el 10 Noviembre " , font=("Times New Roman", 10), fg="Black")
texto3.place(x=280, y=650)

texto4 = tk.Label(ventana, text = "Disponible hasta el 1 Noviembre " , font=("Times New Roman", 10), fg="Black")
texto4.place(x=1350, y=650)


ventana.mainloop()
