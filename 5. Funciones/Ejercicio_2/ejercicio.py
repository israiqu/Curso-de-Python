
from shutil import which


def numeroPrimo(num):
    if num >= 2:
        primo = True
        for i in range(2, num):
            if num%i == 0:
                primo = False
                break
        if primo:
            print(num, "Es un número primo")
        else:
            print(num, "No es un número primo")
    elif num == 1:
        print("El numero", num, "no se considera primo ni compuesto")
    else:
        print("Escribe un numero natural mayor que 1")
    
numeroPrimo(3)
