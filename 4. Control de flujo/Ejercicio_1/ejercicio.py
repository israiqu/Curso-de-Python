print("Bienvenido, para comenzar dime cuántos años tienes:")

edad = 3

if edad >= 0 and edad < 18:
    print("Tu eres menor de edad")
elif edad >= 18 and edad <150:
    print ("Tu eres mayor de edad")
else:
    print("Elige una edad real")
