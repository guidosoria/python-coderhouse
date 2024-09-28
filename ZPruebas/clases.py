class Persona:
    
    
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        
    def saludar(self):
        return f'Hola mi nombre es {self.nombre}, mi apellido {self.apellido} y tengo {self.edad} años'
    
class Empleado(Persona):
    
    
    def __init__(self, nombre, apellido, edad, sueldo, horario):
        super().__init__(nombre, apellido, edad)
        self.sueldo = sueldo
        self.horario = horario
        
    def saludar(self):
        return (
            f'{super().saludar()}'
            f' y gano {self.sueldo} dolares'
        )
        
empleado1 = Empleado("Guido", "Soria", 30, 3000, 360)

print(empleado1.saludar())