
"""

print("==================IF ELSE=======================")

#ej1
numero = int(input("Ingresa un numero del 1 al 1000: "))
if numero <= 400:
    print("El numero es menor que 400")

print(f"Has escrito el numero {numero} ")


#ej2
cadena = input("Introduzca una cadena de texto: ")
if cadena.endswith("a") or cadena.endswith("e") or cadena.endswith("i") or cadena.endswith("o") or cadena.endswith("u"):
    print("La cadena de texto termina en una vocal")

print(f"Haz escrito {cadena}")



#ej3
numero = int(input("Introduce un numero del 1 al 1000: "))
if numero <= 400:
    print("El numero es menor que 400: ")
else:
    print("El numero es mayor o igual que 400: ")

print(f"Has escrito el numero {numero} ")
"""


#ej4

sum1 = int(input("Primer numero: "))
sum2 = int(input("Segundo numero: "))

resultado = sum1 + sum2

if (resultado % 2 == 0):
    if resultado >= 1000:
        print(f"El resultado de la suma es {resultado} par y es mayor o igual a 1000 !")
    else:
        print(f"El resultado de la suma es {resultado} par y es menor que 1000 !")

else:
    if resultado >= 1000:
        print(f"El resultado de la suma es {resultado} impar y es mayor o igual a 1000 !")
    else:
        print(f"El resultado de la suma es {resultado} impar y es menor que 1000 !")


#continuar 148











