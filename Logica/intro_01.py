
"""
# Area de un cuadrado
def area_cuadrado(lado):
    area = lado ** 2
    return area


lado_cuadrado = int(input("Ingrese el lado del cuadrado: "))
area = area_cuadrado(lado_cuadrado)
print(f"La longitud del lado de un cuadrado es: {area}")
"""


def Promedio(num_promedio):
    suma = 0
    for i in num_promedio:
        suma += i
    promedio = suma / len(num_promedio)
    return promedio

nota1 = int(input("Ingresa la primera nota: "))
nota2 = int(input("Ingresa la segunda nota: "))
nota3 = int(input("Ingresa la tercera nota: "))
promedio=Promedio([nota1, nota2, nota3])
print(f"El promedio es: {promedio}")


