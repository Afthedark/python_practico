"""
print("===================BOOLEANOS=======================")
verdad = True
falso = False

print(f"Es verdadero, {verdad}")
print(f"Es Falso, {falso}")




print("===================Compararion AND=======================")

print(True and True)
print(True and False)
print(False and True)
print(False and False)


print("===================Compararion OR=======================")


print(True or True)
print(True or False)
print(False or True) 
print(False or False)


print("===================NOT=======================")

print(not True) #False
print(not False) #False
"""

print("===================BOOL=======================")

booleano1 = bool(input("Primer valor: "))
booleano2 = bool(input("Segundo valor: "))
booleano3 = bool(input("Tercer valor: "))
booleano4 = bool(input("Cuarto valor: "))
booleano5 = bool(input("Quinto valor: "))

print("Resultado: ", booleano5 or (booleano3 and not booleano2) and booleano1 or booleano5)



