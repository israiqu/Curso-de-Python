import time


def Horario():
    irAcasa = False
    horaActual = time.time()
    horaObjetivo = time.time()
    if horaActual == 19:
        irAcasa = True
    else:
        res = horaActual - horaObjetivo
        print("faltan", res, "para ir a casa")

    if irAcasa:
        print("Ya son las", horaActual, "vete a casa")

Horario()
