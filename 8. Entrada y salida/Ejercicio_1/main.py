f = open('mi_nota.txt', 'w')
f.write('Ejercicio #2\n\n')
f.close()

f = open('mi_nota.txt', 'r+')
f.readline()
f.write('En este ejercicio, tendréis que crear un archivo py donde creéis un archivo txt, lo abráis y escribáis dentro del archivo. Para ello, tendréis que acceder dos veces al archivo creado.\n')
f.close()

f.seek(0)
print(f.read())
f.close()
