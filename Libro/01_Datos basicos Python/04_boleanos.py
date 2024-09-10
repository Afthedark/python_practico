"""
print("===================BOOLEANOS=======================")
verdad = True
falso = False

print(f"Es verdadero, {verdad}")
print(f"Es Falso, {falso}")




print("===================Compararion AND=======================")

#Ambas expresiones deben ser verdaderas para ser verdadero

print(True and True) #True
print(True and False) #False
print(False and True) #False
print(False and False) #False


print("===================Compararion OR=======================")

#Una expresion almenos debe ser verdadera para ser verdadero 

print(True or True) #True
print(True or False) #True  
print(False or True) #True
print(False or False) #False


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



