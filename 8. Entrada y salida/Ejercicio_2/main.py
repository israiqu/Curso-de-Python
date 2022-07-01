import pickle

class Vehiculo:
    color = "Rojo"
    ruedas = 4
    puertas = 2

miCoche = Vehiculo()


print("Mi vehículo es color", miCoche.color, ", tiene",
      miCoche.puertas, "puertas y", miCoche.ruedas, "ruedas.")


f = open('clase_vehiculo.bin', 'wb')
pickle.dump(miCoche, f)
f.close()

f = open('clase_vehiculo.bin', 'rb')
recuperar = pickle.load(f)
f.close()


print(type(recuperar))
