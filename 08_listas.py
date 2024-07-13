

"""


print("---------------------Listas----------------------------")


lista = ["Python", "RA-MA", 2019, "Libro", 3]
print(lista)
print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])
print(lista[4])



print("---------------------Concatenando Listas----------------------------")

lista1 = ["Python", "RA-MA", 2019, "Libro", 3]
lista2 = ["Javascript", "RA-MA", 2020, "Libro", 3]

listaconcat = lista1 + lista2

print("Numero elementos lista 1: ", len(lista1))
print("Solo Lista 1", lista1)

print("Numero elementos lista 2: ", len(lista2))
print("Solo Lista 2", lista2)

print("Lista 1 + lista 2 concatenada: ", listaconcat)
print(listaconcat)


#continuar 120

print("---------------------Añadir elementos a Listas----------------------------")
lista = ["camiseta", "Pantalon", "Zapatillas"]
print(lista)

lista = lista + ["Abrigo"]
print(lista)

lista = lista + ["Jersey", "Sudadera"]
print(lista)

lista = lista + ["Calcetines", "Bufanda"]
print(lista)




print("---------------------Editar y eliminar elementos a Listas----------------------------")

lista = ["camiseta", "Pantalon", "Zapatillas"]
print(lista)

lista[0] = "Cazadora"
print(lista)

del lista[0] 
print(lista)




print("---------------------Multipliciar Listas----------------------------")


lista = ["camiseta", "Pantalon", "Zapatillas"]
print(lista)

listaaumentada = lista * 0
print(listaaumentada)



print("---------------------Acceder a Listas y sublistas----------------------------")

lista = ["Camisetas", ["Calcetines", "Cazadora"], "Zapatillas"]

print(lista)
print(lista[0])
print(lista[2])
print(lista[1][0])
print(lista[1][1])

"""

print("---------------------Posiciones de las Listas y sublistas----------------------------")

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(lista)

lista1 = lista[3:7] #Imprime de la posicion 3 a la 7
print(lista1)

lista2 = lista[:5] #Imprime de la posicion 0 a la 5
print(lista2)

lista3 = lista[6:] #Imprime de la posicion 6 a la 9
print(lista3)


#continuar 125
