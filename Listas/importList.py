def menu():
    print (""" OPERACIONES CON LISTAS
            0- Salir"
            1- Leer las 2 listas"
            2- Union"
            3- Diferencia"
            4- Diferencia Simétrica"
            5- Interseccion"
            6- Invertir orden de elementos """)
def leerListas():
    lista1 = []
    lista2 = []
    response = [[],[]]
    for x in range(5):
        lista1.append(int(input("Ingrese datos para la lista Uno: ")))
    print("*"*50)
    for y in range(4):
        lista2.append(int(input("Ingrese datos para la lista Dos: ")))
        response[0] = lista1
        response[1] = lista2
    return response