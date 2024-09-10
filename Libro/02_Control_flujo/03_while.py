
"""


print("--------------------BUCLE WHILE---------------------------")

#ej1
i = 1
while i <= 10: #Mientras i sea menor a 10 se repite el bucle y se incrementa
    print(i, end=" ")
    i += 1 #Incremento de 1 en 1 
"""


"""
#ej1
pedirnumero = True
while pedirnumero:
    valor = int(input("Introduce un numero inferior a 10: "))
    if valor < 10:
        pedirnumero = False
print(f"Has introducido el valor {valor} entero el cual es inferior a 10")


#ej2
introducenombre = True
while introducenombre:
    val = input("Introduce un nombre que sea mayor a 5 caracteres: ")
    if len(val) >= 5:
        introducenombre = False
        print("El nombre introducido es: ", val)


#ej3

suma = True
while suma:
    num1 = int(input("Introduce el primer entero mayor a 50: "))
    num2 = int(input("Introduce el segundo entero mayor a 50: "))
    if (num1 > 50 and num2 > 50):
        suma = False
        res = num1 + num2
        print(f"La suma es: {res}")     




#ej4
num_secreto = 7 #Numero secreto
adivinado = False # Por defecto el False

while not adivinado: #Declaramos la condicion negandolo con not 
    intento = int(input("Introduce el numero secreto: "))
    if intento == num_secreto:
        adivinado = True #Una vez adivinado recien cambia a True
        print(f"Haz adivinado el numero secreto es: {num_secreto}")


#ej5

letra_especifica = "a" #Letra especifica
letra_introducida = "" #Letra introducida

while letra_introducida != letra_especifica: #Mientras la letra introducida no sea la letra especifica
    letra_introducida = input("Introduce la letra (a): ")

print("Has introducido la letra (a) ")


#ej6

item1 = 0
while item1 < 5:
    item2 = 0
    while item2 < 3:
        print(f"Interacion 1: {item1} Interacion 2: {item2}")
        item2 = item2 +1 
    item1 = item1 + 1

#continuar 157
"""

print("--------------------BUCLE FOR CON WHILE---------------------------")

for item1 in range(5): #empieza en 0 y termina en 4, muestra cada elemento del 0 al 4
    item2 = 0
    while item2 < 3: #empieza en 0 y termina en 2, muestra cada elemento del 0 al 2 repetido 5 veces
        print(f"Interacion 1: {item1} Interacion 2: {item2}")
        item2 += 1








