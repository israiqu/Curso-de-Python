
saludo = input('¿Como te llamas? ')
print(f'Hola {saludo}, vamos a comenzar')

datos = input("Escribe el nombre de 3 paises:\n")
paises = [pais for pais in datos.split(",")]
print(",".join(sorted(list(set(paises)))))
