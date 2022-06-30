import time


def Horario():
    irAcasa = False
    horaActual = time.strftime("%H")
    horaObjetivo = 19
    if int(horaActual) >= horaObjetivo:
        irAcasa = True
    else:
        res = horaObjetivo - int(horaActual)
        print("faltan", res, "horas para ir a casa")

    if irAcasa:
        print("Ya son las", horaActual, "vete a casa")

Horario()
