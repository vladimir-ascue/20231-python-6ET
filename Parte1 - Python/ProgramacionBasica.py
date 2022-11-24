# promedi de 3 notas
# Tener siempre en cuenta la indentacion o el indentado.
def sumar(num1, num2):
  resultado = num1 + num2
  return resultado

def restar(num1, num2):
  resultado = num1 - num2
  return resultado

def multiplicar(num1, num2):
  resultado = num1 * num2
  return resultado

def dividir(num1, num2):
  resultado = num1 / num2
  return resultado

def leerEntero(mensaje):
  flag = True
  while flag:
    try:
      num = int(input(mensaje))
      flag = False
    except ValueError:
      print("Error: Debe ingresar un entero válido.")
  return num

def menu():
  print("******  MENU  ******")
  print("0- Salir ")
  print("1- Sumar ")
  print("2- Restar ")
  print("3- Multiplicar ")
  print("4- Dividir ")
  print(">>> Ingrese una opcion: ")
 
opcion = 1
flag = True

while ( flag ):
  menu()
  opcion = leerEntero("Ingrese opcion: ")
  match opcion:
    case 0:
      print("Adios ...")
      flag = False
    case 1:
      num1 = leerEntero("Ingrese primer sumando: ")
      num2 = leerEntero("Ingrese segundo sumando: ")
      print ("la suma es: ", sumar(num1, num2))
    case 2:
      num1 = leerEntero("Ingrese minuendo: ")
      num2 = leerEntero("Ingrese sustraendo: ")
      print ("la diferencia es: ", restar(num1, num2))
    case 3:
      num1 = leerEntero("Ingrese primer operando: ")
      num2 = leerEntero("Ingrese segundo operando")
      print ("El producto es: ", multiplicar(num1, num2))
    case 4:
      num1 = leerEntero("Ingrese dividendo: ")
      num2 = leerEntero("Ingrese divisor")
      flag2 = True
      while (flag2):
        print (" - El divisor no puede ser 0")
        print ("    1- Ingresar nuevo divisor. ")
        print ("    Otro- Regresar al menú principal. ")
        op = leerEntero("    >> Leer opcion: ")
        if (op == 1):
          num2 = leerEntero("    >> Ingrese divisor: ")
          if (num2 != 0):
            print ("El cosiente es: ", dividir(num1, num2))
            flag2 = False
        else:
          flag2 = False



      