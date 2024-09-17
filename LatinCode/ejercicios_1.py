


#Ejercicio 1: Cálculo del área de un círculo

def CalculoAreaCirculo(dato):
    PI = 3.1416
    area = PI * (dato ** 2)
    redondeado = round(area, 2)
    return redondeado


radio = float(input("Ingrese el radio del circulo: "))
calculo = CalculoAreaCirculo(radio)
print(f"El area del circulo es: {calculo}")





