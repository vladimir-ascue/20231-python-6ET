from importList import *
datos = leerListas()
lista1 = datos[0] 
lista2 = datos[1]
while True:
    menu()
    opcion = int(input("  Ingrese a Opcion >> "))
    if opcion == 0:
        print("bye:  ")
        break
    if opcion == 1:
        print(f" Lista Uno: {lista1} \n Lista Dos: {lista2}")
    if opcion == 2:
        print("Union de las dos listas : ",set(lista1) | set(lista2))
    if opcion ==3:
        print("la diferencia es: ",set(lista1) - set(lista2))
    if opcion ==4: 
        print("La diferencia simetrica es:",set(lista1) ^ set(lista2))
    if opcion ==5:
        print("La interceccion es: ",set(lista1) & set(lista2))
    if opcion ==6:
        listainvertida=lista1
        listainvertida.reverse()
        print(f"Datos de la lista uno {lista1} Lista uno invertida: {listainvertida}")