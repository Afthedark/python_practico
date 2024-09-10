
"""
print("===================NUM ENTEROS=======================")

n1 = int(input("Ingrese un numero entero: "))
n2 = int(input("Ingrese otro numero entero: "))

print(f"Resultado: {n1 + n2}")


print("===================DIV ENTEROS=======================")

n1 = int(input("Dividendo: "))
n2 = int(input("Divisor: "))

print(f"Resultado: {n1 // n2}")



print("===================BASE EXPONTE ENTEROS=====================")


base = int(input("Base: "))
exponente = int(input("Exponente: "))

print(f"Resultado {base ** exponente}")



print("===================RESTA DECIMALES=====================")

minuendo = float(input("Minuendo: "))
sustraendo = float(input("Sustraendo: "))

print(f"resultado {minuendo - sustraendo}")



print("===================DIVISION REALES=====================")

diviendo = float(input("Dividiendo: "))
divisor = float(input("Divisor: "))

print(f"Resultado {diviendo / divisor}")



print("===================Multiplicacion REALES=====================")

multiplicando = float(input("Multiplicando: "))
multiplicador = float(input("Multiplicador: "))

print(f"Resultado {multiplicando * multiplicador}")



print("===================Multiplicacion REALES REDONDEANDO=====================")

multiplicando = float(input("Multiplicando: "))
multiplicador = float(input("Multiplicador: "))
res = round(multiplicando * multiplicador, 1)

print(f"Resultado {res}")
"""


print("===================Uso de Parentesis=====================")


numero1 = float(input("Primer numero: "))
numero2 = float(input("Segundo numero: "))
numero3 = float(input("Tercer numero: "))
numero4 = float(input("Cuarto numero: "))
numero5 = float(input("Quinto numero: "))
numero6 = float(input("Sexto numero: "))


resultado = (numero5+(numero3*(numero1**numero6)))-(numero4//numero2)
print(f"Resultado: {resultado}")