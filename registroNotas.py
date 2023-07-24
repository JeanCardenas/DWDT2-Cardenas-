class Alumno:
    def __init__(self, nombre, apellido, edad, nacionalidad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.nacionalidad = nacionalidad
        self.notas = ''

if __name__ == "__main__":
    alumnos = []
    while True:
        print("Bienvenidos al registro de notas")
        comando = input("Ingrese comando (R, C, P, S o X): ")

        if comando == "R":
            nombre = input("Ingrese el nombre del alumno: ")
            apellido = input("Ingrese el apellido del alumno: ")
            edad = input("Ingrese la edad del alumno: ")
            nacionalidad = input("Ingrese la nacionalidad del alumno: ")
            alumnoNuevo = Alumno(nombre, apellido, edad, nacionalidad)
            alumnos.append(alumnoNuevo)

        elif comando == "C":
            for alumno in alumnos:
                while True:
                    try:
                        nota = int(input(f"Alumno {alumno.nombre} {alumno.apellido}, Ingrese nota: "))
                        if 0 <= nota <= 20:
                            alumno.notas.append(nota)
                            break
                        else:
                            print("La nota debe estar entre 0 y 20.")
                    except ValueError:
                        print("Ingrese un número válido.")

        elif comando == "P":
            if len(alumnos) > 0:
                total_notas = sum(sum(alumno.notas) for alumno in alumnos)
                promedio = total_notas / sum(len(alumno.notas) for alumno in alumnos)
                print(f"El promedio de notas para {len(alumnos)} alumno(s) es: {promedio:.2f}")
            else:
                print("No hay alumnos registrados.")

        elif comando == "S":
            if len(alumnos) > 0:
                suma_notas = sum(sum(alumno.notas) for alumno in alumnos)
                print(f"La suma de notas de {len(alumnos)} alumno(s) es: {suma_notas}")
            else:
                print("No hay alumnos registrados.")

        elif comando == "X":
            print("Finzalizacion del programa")
            break

        else:
            print("Comando inválido. Intentelo de nuevo.")




