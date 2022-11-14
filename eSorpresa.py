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
  print("1- Ingresar nombres de 2 alumnos ")
  print("2- Ingresar Notas ")
  print("3- Calcular pormedio ")
  print("4- Mostrar Resgistro ")
  print("5- Salir ")
  print(">>> Ingrese una opcion: ")
 
opcion = 1
flag = True

 nombreAlumno1, nombreAlumno2 = "", ""
nota1A1, nota2A1,nota3A1,nota1A2,nota2A2,nota3A2 = 0, 0, 0, 0, 0, 0
promedioA1, promedioA2 = 0, 0

def promedio(nota1, nota2, nota3):
  return (nota1 + nota2 + nota3) / 3

def resultado(promedio):
  resultado = "REPROBADO"

  if (promedio > 12):
    resultado = "APROBADO"
  else:
    if (promedio < 10):
      resultado = "REPROBADO"
    else:
      resultado = "DESAPROBADO"

#  if (promedio >= 0 and promedio < 10):
#    resultado = "REPROBADO"
#  elif (promedio >= 10 and promedio < 13):
#    resultado = "DESAPROBADO"
#  elif (promedio >= 13 and promedio <=20):
#    resultado = "APROBADO"
  return resultado

while ( flag ):
  menu()
  opcion = leerEntero("Ingrese opcion: ")
  match opcion:
    case 1: # INGRESE ONMBRES DE ALUMNOS
      nombreAlumno1 = input("Ingrese nombre del primer alumno: ")
      nombreAlumno2 = input("Ingrese nombre del segundo alumno: ")
    case 2: # INGRESAR NOTAS DE ALUMNOS
      flag2 = True
      while (flag2):
        print ("    1- Ingrese notas de ", nombreAlumno1)
        print ("    2- Ingrese notas de ", nombreAlumno2)
        print ("    3- Voler al menu anterior")
        opcion2 = leerEntero("Seleccione opcion: ")
        match opcion2:
          case 1:
            nota1A1 = leerEntero("Ingresar Nota 1 de "+ nombreAlumno1)
            nota2A1 = leerEntero("Ingresar Nota 2 de "+ nombreAlumno1)
            nota3A1 = leerEntero("Ingresar Nota 3 de "+ nombreAlumno1)
          case 2:
            nota1A2 = leerEntero("Ingresar Nota 1 de "+ nombreAlumno2)
            nota2A2 = leerEntero("Ingresar Nota 2 de "+ nombreAlumno2)
            nota3A2 = leerEntero("Ingresar Nota 3 de "+ nombreAlumno2)
          case 3:
            flag2 = False
    case 3: # Calcular promedios
      promedioA1 = promedio(nota1A1, nota2A1, nota3A1)
      promedioA2 = promedio(nota1A2, nota2A2, nota3A2)
      print("Promedios calculados con éxito")
    case 4: # Mostrar Resgistro
      print ("*************************************")
      print ("***            REGISTRO            **")
      print ("*************************************")
      print ("ALUMNO "+'\t\t'+"Nota1"+'\t'+"nota2"+'\t'+"nota3"+'\t'+"Promedio"+"\t"+"Resultado")
      print (nombreAlumno1,"\t\t",nota1A1,"\t",nota2A1,'\t',nota3A1,'\t',promedioA1,"\t\t",resultado(promedioA1))
      print (nombreAlumno2,'\t\t',nota1A2,'\t',nota2A2,'\t',nota3A2,'\t',promedioA2,"\t\t",resultado(promedioA2))
    case 5:
      print ("Adios...")
      flag = False