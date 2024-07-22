"""

print("--------------------BUCLE FOR---------------------------")

lista = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

for item in lista:
    print(item, end=" ")


#end= " " es para que no salga el salto de linea





print("--------------------BUCLE FOR ANIDADOS---------------------------")

listaabc = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

listainteracciones = [1,2,3,4,5]

for item in listainteracciones:
    print(f"Interacción numero: {item}")
    for letra in listaabc:
        print(letra, end=" ")
    print("\n")



#
lista_meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"] 

for mes in lista_meses:
    print(f"Mes: {mes}")
    for dia in range(1,32):
        print(dia, end=" ")
    print("\n")

    
#
categorias = {
    "frutas": ["manzana", "pera", "banana"],
    "verduras": ["lechuga", "coliflor", "papa"],
    "lacteos": ["leche", "queso", "yogurt"]
}

for categoria, productos in categorias.items(): #.items() es para mostrar el diccionario   
    print(f"Categoria: {categoria}")
    for producto in productos:
        print(productos, end=" ")
    print("\n")


#
alumnos = {
    "mario": [80, 85, 90],
        "carlos": [90, 80, 85],
    "lucy": [80, 85, 90],
}

for alumno, notas in alumnos.items(): #.items() es para mostrar el diccionario   
    print(f"Nombre alumno: {alumno}")
    for nota in notas:
        print(nota, end=" ")
    print("\n")




#

lista = [99, "Casa", ["hola", "adios"], "perro", "gato", 34]

for iterar in lista:
    print(iterar)
"""


for item in range(5): #empieza en 0 y termina en 4
    for item2 in range(3): # empieza en 0 y termina en 2
        print(f"Iteracion: {item} {item2}") #itera 0 0, 0 1, 0 2, 1 0, 1 1, 1 2


#continuar 155


