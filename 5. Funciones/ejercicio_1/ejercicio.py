import math

def areaTriangulo(b,a):
    area = (b * a) / 2
    print("El área del triángulo es:", area)

def areaCirculo(r):
    area = math.pi * (r**2)
    print("El área del círculo es:", area)

areaTriangulo(4, 3)
areaCirculo(2)
