


"""
print("===================CADENAS DE TEXTO=======================")
cadena1 = "Hola python definido con comillas dobles"
cadena2 = 'Hola python definido con comillas simple'

print(cadena1)
print(cadena2)



print("==================ACCEDER A CARACTERES DE CADENA==================")

cadena = "python"
print("Posicion de caracter de cadena [0]:", cadena[0])
print("Posicion de caracter de cadena [1]:", cadena[1])
print("Posicion de caracter de cadena [2]:", cadena[2])
print("Posicion de caracter de cadena [3]:", cadena[3])
print("Posicion de caracter de cadena [4]:", cadena[4])
print("Posicion de caracter de cadena [4]:", cadena[5])



print("==================OPERADORES CON CADENAS==================")

cadena1 = input("Introduzca la primera cadena: ")
cadena2 = input("Introduzca la segunda cadena: ")
cadena3 = input("Introduzca la tercera cadena: ")

cadenasuma = cadena1 + '.' + cadena2 + ' ' + cadena3 #Concatenar cadenas clasico
cadenamultiplicar = (cadena2, ' ') * 3 #Multiplicar cadenas

print(cadenasuma)
print(cadenamultiplicar)



print("==================OPERADORES CON CADENAS==================")

cadena1 = input("Introduzca la primera cadena: ")
cadena2 = input("Introduzca la segunda cadena: ")
cadena3 = input("Introduzca la tercera cadena: ")

cadenasuma = cadena1
cadenasuma +=  ' '
cadenasuma += cadena2
cadenasuma +=  ' '
cadenasuma += cadena3

print(cadenasuma)



cadena1 = input("Introduzca la primera cadena: ")
cadena2 = input('Introduzca la primera cadena: ')

print("Esta la segunda cadena contenida en la primera cadena ?", cadena2 in cadena1)





cadena1  = input("Introduzca la primera cadena: ")
cadena2 = input("Introduzca la segunda cadena: ")
cadena3 = input("Introduzca la tercera cadena: ")

print("Longitud cadena 2 es (len): ", (len(cadena2)))

print("Cadena 3 a mayuscula (upper): ", cadena3.upper())
print("Cadena 3 a minuscula (lower): ", cadena3.lower())

print("Cadena 2 cambia de mayuscula a minuscula y viceversa: ", cadena2.swapcase())

print("Cadena 1 la priemra letra en Mayuscuka (tittle)", cadena1.title())

print("Cadena 1 cada primera letra a mayuscula (capitalize):", cadena1.capitalize())


print("Cadena 3 a mayuscula (isupper): ", cadena3.isupper())
print("Cadena 3 a minuscula (islower): ", cadena3.islower())
#continuar pagina 110



print("==================Eliminar caracteres en INICIO Y FIN DE la CADENA==================")

cadena = input("Introduzca una cadena con espacios en blanco al principio y al final: ")

print(len(cadena))

cadenastrip = cadena.lstrip()  #Quita los espacios al principio de la cadena 
print("Cadena (lstrip): ", cadenastrip,end='.')
print("\nLontigitud de la cadena (lstrip): ", len(cadenastrip)) #Longitud de la cadena

cadenarstrip = cadena.rstrip() #Quita los espacios al final de la cadena
print("Cadena (rstrip): ", cadenarstrip,end='.')
print("\nLontigitud de la cadena (rstrip): ", len(cadenarstrip)) #Longitud de la cadena

cadenastrip = cadena.strip() #Quita los espacios al principio y al final de la cadena
print("Cadena (strip): ", cadenastrip, end='.')
print("\nLongitud de la cadena (strip): ", len(cadenastrip))



print("==================Verificar si una cadena empieza y termina por otra y cuantas veces se repite==================")

cadena = input("Introduzca una cadena: ")
buscar = input("Introduzca la cadena a buscar: ")

print("Comienza la cadena por la cadena a buscar: ", cadena.startswith(buscar))
print("Termina la cadena por la cadena a buscar: ", cadena.endswith(buscar))

print("Cuantas veces aparece la cadena a buscar: ", cadena.count(buscar))



print("==================Metodo Find==================")


cadena = input("Introduzca una cadena: ")
buscar = input("Introduzca la cadena a buscar: ")

print("Comienza la cadena por la cadena a buscar: ", cadena.find(buscar)) #Find es para devolver el indice
print("Termina la cadena por la cadena a buscar: ", cadena.rfind(buscar)) #rfind es para devolver el indice



print("==================Metodo replace==================")


cadena = input("Introduzca una cadena: ")
reemplazar = input("Introduzca la cadena a reemplazar: ")
remplazo = input("Introduzca la cadena de reemplazo: ")

print("Cadena original: ", cadena) 
print("Cadena reemplazada: ", cadena.replace(reemplazar, remplazo)) 


"""

print("==================Metodo split==================")


cadena = input("Introduzca una cadena con varias palabras: ")
print("Cadena dividida por espacios splic", cadena.split())



#continuar 114