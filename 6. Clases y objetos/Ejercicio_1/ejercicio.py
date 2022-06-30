
class Vehiculo:
    color = "Rojo"
    ruedas = 4
    puertas = 2

class Coche(Vehiculo):
    velocidad = "250 km/h"
    cilindrada = 4

miCoche = Coche()

print("Mi coche es color", miCoche.color, "y tiene", miCoche.puertas, "puertas, además corre a", miCoche.velocidad, "con sus", miCoche.cilindrada, "cilindros y sus", miCoche.ruedas, "ruedas.")
