class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def imprimir(self):
        print(f"El alumno se llama {self.nombre} y su nota es {self.nota}")
