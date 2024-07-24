
"""


print("==================FUNCIONES=======================")



#Ej1
def Hola():
    print("Hola te esta gustando python?")


print("Primera invocacion: ", end="")
Hola()

print("Segunda invocacion: ", end="")
Hola()


#Ejm2

def Hola():
    return "Hola te esta gustando python?"

print(f"Primera invocacion: ", Hola())
print(f"Segunda invocacion: ", Hola())

#Ejm2

def Es_par_impar(param):
    if param % 2 == 0:
        return ("El numero es par")
    else:
        return ("El numero es impar")


numero = int(input("Introduce un numero para saber si es par o impar: "))
resultado = Es_par_impar(numero)
print(resultado)



#Ejm2.2
def TablaMultiplicar(num):
    multi = 1
    for i in range(1, 11):
        multi = num * i
        print(f"{num} x {i} = {multi}")


numero = int(input("Introduce un numero para ver su tabla de multiplicar del 1 al 10: "))
TablaMultiplicar(numero)


#Ejm3
def Multiplicar(n1, n2):
    return n1 * n2


multiplicando = int(input("Ingrese un numero: "))
multiplicador = int(input("Ingrese otro numero: "))

res = Multiplicar(multiplicando, multiplicador)
print(f"La multiplicacion es: {res}")







print("-------------------Varios parametros en python con * ----------------------")

def SumarMultiplicar(*valores):
    resultadosuma = 0
    resultadomultiplicacion = 1

    for item in valores: #Para iterar los valores que recibe
        resultadosuma = resultadosuma + item #sumar los valores 
        resultadomultiplicacion = resultadomultiplicacion * item #multiplicar los valores
    return resultadosuma, resultadomultiplicacion



ressuma, resmulti = SumarMultiplicar(3, 5, 7, 9, 11, 13, 15, 17, 19, 21)

print(f"El resultado de la suma es: {ressuma}")
print(f"El resultado de la multiplicacion es: {resmulti}")    

"""


def SumarMultiplicar(param1, param2):
    return Sumar(param1, param2), Multiplicar(param1, param2)


def Sumar(n1, n2):
    return n1 + n2


def Multiplicar(n1, n2):
    return n1 * n2


num1 = int(input("Introduce un numero 1: "))
num2 = int(input("Introduce un numero 2: "))

res_suma, res_multi = SumarMultiplicar(num1, num2)

print(f"La suma es: {res_suma}")
print(f"La multi es: {res_multi}")





#continuar 167