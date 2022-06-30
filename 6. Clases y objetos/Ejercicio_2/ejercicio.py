class Alumno:
    nombre = None
    calificacion = None
    resultado = None 

    def __init__(self, nombre, calificacion):
        self.nombre = nombre
        self.calificacion = calificacion
        if self.calificacion >= 70:
            self.resultado = "Aprobado"
        elif self.calificacion < 70:
            self.resultado = "Reprobado"


miNota = Alumno("Israel", 98)

print("Hola", miNota.nombre, "Tu calificación es de:", miNota.calificacion, "Por lo que estás:", miNota.resultado)