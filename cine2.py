dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]
no_disponibles = [0, 2]
No_disponibles = [0, 3]


sillas = [#matriz disponibilidad
    [0, 0, 1, 0, 0],
    [0, 1, 1, 0, 0],
    [0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0]
]


print("\033[92m===============================\033[0m")
print("\033[94m       Bienvenido al Cine                 \033[0m")
print("\033[92m===============================\033[0m")

acom = 0
print("Que mes desea ver su pelicula? ")

meses = [
    "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
    "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]


print(" MESES ")
o = 1
for i in meses:
    print(o, [i])
    o += 1
print()
num = int(input())
mes_elegido = meses[num - 1]


if num >= 10: #mayor octubre
    m = 0
    print("\n DIAS DE LA SEMANA ")
    for i in dias:
        print(m, [i])
        m += 1

    valido = False
    while valido == False:
        print("Que dia desea ver su pelicula?")
        elecciond = int(input())

        if elecciond < 0 or elecciond >= len(dias):
            print("\033[91mNumero de dia invalido\033[0m")

        elif elecciond in no_disponibles:
            print("\033[91mEse dia no esta disponible. Elija otro.\033[0m")

        else:
            print("Dia disponible.")
            dia_elegido = dias[elecciond]
            valido = True
            acom += 1

else: #Menores a octubre
    m = 0
    print("\n DIAS DE LA SEMANA ")
    for i in dias:
        print(m, [i])
        m += 1

    valido = False
    while valido == False:
        print("Que dia desea ver su pelicula?")
        elecciond = int(input())

        if elecciond < 0 or elecciond >= len(dias):
            print("\033[91mNumero de dia invalido\033[0m")

        elif elecciond in no_disponibles:
            print("\033[91mEse dia no esta disponible. Elija otro.\033[0m")

        else:
            print("Dia disponible.")
            dia_elegido = dias[elecciond]
            valido = True
            acom += 1


if num >= 10:
    peliculas = ("Hereditary ", "Scream ", "Obsesion")
    i = 0
    print("\033[92mEstas son las peliculas disponibles...\033[0m")

    while i < len(peliculas):
        print([i], peliculas[i])
        i += 1

else:
    peliculas = ["As above so below", "El conjuro ", "Michael Jackson"]
    i = 0
    print("\033[92mEstas son las peliculas disponibles...\033[0m")

    while i < len(peliculas):
        print([i], peliculas[i])
        i += 1


valido = False

while valido == False:
    eleccion = int(input("Que pelicula desea ver? "))

    if eleccion < 0 or eleccion >= len(peliculas):
        print("\033[91mNumero de pelicula invalido. Intente de nuevo.\033[0m")
    else:
        pelicula_elegida = peliculas[eleccion]
        valido = True


# Sillas
print("\033[92mDonde quiere ver la pelicula?\033[0m")

valido = False

while valido == False:
    fila = int(input("Que fila desea? (1-4): "))
    columna = int(input("Que silla desea? (1-5): "))

    fila = fila - 1
    columna = columna - 1

    if fila < 0 or fila >= len(sillas) or columna < 0 or columna >= len(sillas[fila]):
        print("\033[91mNumero de fila o silla invalido.\033[0m")

    elif sillas[fila][columna] == 1:
        print("\033[91mEsa silla esta ocupada. Elija otra.\033[0m")

    else:
        print("Silla disponible.")
        sillas[fila][columna] = 1
        fila_elegida = fila + 1
        silla_elegida = columna + 1
        valido = True


# Boletas
if acom == 1:
    print("Cada boleta tiene un valor de 20.000")
    print("Cuantas desea comprar?")
    boletas = int(input())

    debe = boletas * 20000
    pagar = 0

    while pagar < debe:
        pagar = int(input("Cuanto dinero tienes para pagar? "))

        if pagar < debe:
            print("\033[91mDinero insuficiente. Intentalo de nuevo.\033[0m")

    print("\033[94mGracias por comprar.\033[0m")
    print("Tu cambio es:", pagar - debe)

    print("\n\033[92m====================================\033[0m")
    print("\033[94m       RESUMEN DE TU RESERVA        \033[0m")
    print("\033[92m====================================\033[0m")

    print("Pelicula:", pelicula_elegida)
    print("Mes:", mes_elegido)
    print("Dia:", dia_elegido)
    print("Fila:", fila_elegida)
    print("Silla:", silla_elegida)
    print("Cantidad de boletas:", boletas)
    print("Precio por boleta: $20.000")
    print("Total a pagar: $", debe)
    print("Dinero entregado: $", pagar)
    print("Cambio: $", pagar - debe)

    print("\033[92m====================================\033[0m")
    print("Gracias por reservar con nosotros!")
    print("\033[92m====================================\033[0m")
