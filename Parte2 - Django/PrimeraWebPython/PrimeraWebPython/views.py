from django.http import HttpResponse

def saludo(request):
    contenido_html = '''
                      <h1 style="border: 1px solid Blue; color: Blue; border-raidus: 15px;">
                        Hola Django
                      </h1>
                  '''
    return HttpResponse(contenido_html)


def saludo2(request):
    contenido_html = '''
                      <table style="border: 1px solid black;">
                        <tr>
                          <td>
                            Apellidos
                          </td>
                          <td>
                            Nombres
                          </td>
                        </tr>
                        <tr>
                          <td>
                            Samuel
                          </td>
                          <td>
                            Allpacca
                          </td>
                        </tr>
                        <tr>
                          <td>
                            Xiomara
                          </td>
                          <td>
                            Tinta
                          </td>
                        </tr>
                      </table>
                  '''
    return HttpResponse(contenido_html)


def suma2numeros(response, num1, num2):
    suma = "la suma es: ", int(num1) + int(num2)
    return HttpResponse(suma)

def tablaN(response, num):
    contenido = ""
    for n in range(int(num)):
        prodActual = n * int(num)
        contenido = contenido + f'- {n} * {num} = {prodActual} <br>'
    return HttpResponse(contenido)
