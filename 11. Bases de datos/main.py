from cgitb import reset
import sqlite3

conn = sqlite3.connect('alumnos.db')
cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS alumnos (id INT, nombre TEXT, apellido TEXT)")

cursor.execute("INSERT INTO alumnos VALUES(1,'Gines', 'Contreras')")
cursor.execute("INSERT INTO alumnos VALUES(2,'Rufina', 'Marino')")
cursor.execute("INSERT INTO alumnos VALUES(3,'Hipolito', 'Solis')")
cursor.execute("INSERT INTO alumnos VALUES(4,'Manuela', 'Carpio')")
cursor.execute("INSERT INTO alumnos VALUES(5,'Gloria', 'Sosa')")
cursor.execute("INSERT INTO alumnos VALUES(6,'Leandro', 'Gomez')")
cursor.execute("INSERT INTO alumnos VALUES(7,'Oscar', 'Rosales')")
cursor.execute("INSERT INTO alumnos VALUES(8,'Luca', 'Montoya')")
cursor.execute("INSERT INTO alumnos VALUES(4,'Maravillas', 'Postigo')")
cursor.execute("INSERT INTO alumnos VALUES(5,'Laila', 'Canales')")
cursor.execute("INSERT INTO alumnos VALUES(6,'Mohamed', 'Navarrete')")
cursor.execute("INSERT INTO alumnos VALUES(7,'Roman', 'Granado')")
cursor.execute("INSERT INTO alumnos VALUES(8,'Melania', 'Moreira')")

conn.commit()

cursor.execute("SELECT * FROM alumnos WHERE Nombre = 'Gloria'")

res = cursor.fetchall()

print(res)

conn.close()