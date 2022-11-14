# LISTAS
lista1 = ["Vladimir", "Ascue", "Lovón"]
lista2 = [1, 2, 3]
lista3 = ["Vladimir", 2, lista2];

print(lista1)
print()
print(lista2)
print()
print(lista3)

print()
lista1.append("Saturnino")
print(lista1)

print()
lista1.insert(2,"Pandorfino")
print(lista1)

print()
lista1.remove("Pandorfino")
print(lista1)

lista1.insert(0,"Anastasia")
print(lista1)

lista1[0] = "Ruperto"
print(lista1)

# Tupla
tuplita = ("Vladi", "Ascue", 40, "Profe de Python")
print("****************** TUPLAS ********************")
print(tuplita);
print()
print("Vladi esta en la posicion: ", tuplita.index("Vladi"))
# print("Donde esta carlos: ",tuplita.index("Carlos"))
print("Donde esta 40: ",tuplita.index(40))

#tuplita["Vladi"] = "Carlos"
print()

#tuplita[0] = "Sebastian"
print()

print("****************** DICCIONARIOS ********************")

diccionario = {"Nombre":"Vladimir", "Apellido":"Ascue", "Edad":40}

print (diccionario)

print( diccionario["Nombre"] )



