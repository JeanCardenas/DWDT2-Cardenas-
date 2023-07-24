class alumnos:
    def __init__(self,nombre,apellido,edad,nota,nacionalidad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.nota = ''
        self.nacionalidad = nacionalidad
    def mostrarNota(self):
        print(f"Su nota es: {self.nota}")
    def modificarNota(self,newNota):
        self.nota = newNota




    