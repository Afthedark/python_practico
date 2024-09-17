
"""
# Area de un cuadrado 1
def area_cuadrado(lado):
    area = lado ** 2
    return area


lado_cuadrado = int(input("Ingrese el lado del cuadrado: "))
area = area_cuadrado(lado_cuadrado)
print(f"La longitud del lado de un cuadrado es: {area}")
"""



"""
# Cálculo del promedio de tres números 2
def Promedio(valor):
    suma = 0
    for i in valor: #Se recorre la lista de notas
        suma += i #Se suman los valores de las notas
    promedio = suma / len(valor) #Se suman los valores de las notas y se dividen por la cantidad de notas
    return promedio

nota1 = int(input("Ingresa la primera nota: "))
nota2 = int(input("Ingresa la segunda nota: "))
nota3 = int(input("Ingresa la tercera nota: "))
promedio=Promedio([nota1, nota2, nota3]) #Se suman los valores de las notas y se dividen por la cantidad de notas
print(f"El promedio es: {promedio}")

"""


"""
"""

# Cálculo del tiempo de viaje 3
def TiempoViaje(d, v):
    tiempo = (d / v)
    return tiempo

distancia = int(input("Ingrese la distancias en km/h: "))
velocidad = int(input("Ingresa la velocidad a la que viaja en km/h: "))
tiempo_res = TiempoViaje(distancia, velocidad)
print(f"El tiempo de viaje en horas es: {tiempo_res}")

