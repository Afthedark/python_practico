
"""

print("-------------------------DICCIONARIOS---------------------------")


daysemanas_ingles = {"Lunes": "Monday",
              "Martes": "Tuesday",
              "Miercoles": "Wednesday",
              "Jueves": "Thursday",
              "Viernes": "Friday",}


print(daysemanas_ingles["Lunes"])
print(daysemanas_ingles["Miercoles"])
print(daysemanas_ingles["Viernes"])



print("-------------------------Agregar y eliminar en DICCIONARIOS---------------------------")



daysemanas_ingles = {"Lunes": "Monday",
              "Martes": "Tuesday",
              "Miercoles": "Wednesday",
              "Jueves": "Thursday",
              "Viernes": "Friday",}

print(daysemanas_ingles)

#Agregando elementos
daysemanas_ingles["Sabado"] = "Saturday"
daysemanas_ingles["Domingo"] = "Sunday"
print(daysemanas_ingles)

#Eliminando elementos
del daysemanas_ingles["Lunes"]
print(daysemanas_ingles)


"""

print("-------------------------Metodos DICCIONARIOS---------------------------")

diasemana_ingles = {"Lunes": "Monday",
              "Martes": "Tuesday",
              "Miercoles": "Wednesday",
              "Jueves": "Thursday",
              "Viernes": "Friday",}


print(f"Diccionario original: {diasemana_ingles}")

copia_diccionario = diasemana_ingles.copy()
print(f"Copia del diccionario: {copia_diccionario}")

#pop es para borrar un elemento
print(f"valor pop del dia lunes (pop): {diasemana_ingles.pop('Lunes')}")

print(f"Despues de los cambios con el pop: {diasemana_ingles} ")

#popitem es para borrar un elemento al azar
print(f"Elementos al azar con pop item {diasemana_ingles.popitem()}")
print(f"Elementos al azar con cambios hechos {diasemana_ingles}")


#clear es para borrar todo el diccionario
diasemana_ingles.clear()
print(f"Diccionario vacio: {diasemana_ingles}")


#del es para borrar todo el diccionario
del diasemana_ingles
print(f"Diccionario eliminado: {diasemana_ingles}")


print(f"Diccionario original: {diasemana_ingles}")


#Investigar mas metodos de los diccionarios


