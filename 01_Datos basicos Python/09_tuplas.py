
"""
print("----------------------Tuplas---------------------------")

tupla = ('Casa', '2', 345, 'Perro', '99')
print(f"Elementos de la tupla: {tupla}")
print(f"Posicicion de la tupla 0: {tupla[0]}")
print(f"Posicicion de la tupla 1: {tupla[1]}")
print(f"Posicicion de la tupla 2: {tupla[2]}")
print(f"Posicicion de la tupla 3: {tupla[3]}")
print(f"Posicicion de la tupla 4: {tupla[4]}")


print("----------------------Metodos Tuplas---------------------------")

tupla = ('Casa', '2', 345, 'Perro', '99')
print(f"Elementos de la tupla: {tupla}")

print(f"Numero de elementos en '99' de la tupla: {tupla.count('99')}")
print(f"Que posicion ocupa 'Perro en la tupla {tupla.index('Perro')}")


print("----------------------Posiciones de las Tuplas---------------------------")

tupla = (1,2,3,4,5,6,7,8,9)
print(tupla)
print(tupla[4:9])
print(tupla[:3])
print(tupla[2:])


#Continuar 129



print("----------------------Concatenacion de las Tuplas y contar las tuplas---------------------------")

tupla1 = (29, "Television", 8763)
tupla2 = (1,2,3, "Videojuego")

print(f"Numero de elementos de la tupla1: {len(tupla1)}")
print(F"Tupla 1: ", tupla1)

tuplaconcatenada = tupla1 + tupla2
print(f"Tupla concatenada: ", tuplaconcatenada)
print(f"Cantidad de la tupla concatenada: {len(tuplaconcatenada)}")


"""


print("----------------------Operadores en las Tuplas y contar las tuplas---------------------------")

tupla = (1,2,3,4,5,6,7,8,9,0)
print(f"Tupla normal: {tupla}")

tuplamultiplicada = tupla * 2
print(f"Tupla multiplicada: {tuplamultiplicada}") 