
def bisiesto(year):
    if year > 0:
        leapYear = True
        i = year % 4
        if i == 0:
            i = year % 100
            if i== 0:
                i = year % 400
                if i == 0:
                    leapYear = True
                else:
                    leapYear = False
            else:
                leapYear = True
        else:
            leapYear = False

        if leapYear:
            print("El año", year, "Es bisiesto")
        else:
            print("El año", year, "No es bisiesto")
    else:
        print("introduce un número válido mayor que 0")

bisiesto(2022)