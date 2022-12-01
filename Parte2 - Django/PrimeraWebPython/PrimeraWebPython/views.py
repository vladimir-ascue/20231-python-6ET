from django.http import HttpResponse

def saludo(request):
  contenidoHTML = '''
                      <h1 style="border: 1px solid Blue; color: Blue; border-raidus: 15px;">
                        Hola Django
                      </h1>
                  '''
  return HttpResponse(contenidoHTML)

def saludo2(request):
  contenidoHTTP = '''
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
  return HttpResponse(contenidoHTTP)

  def suma2numeros(num1, num2):
    suma = int(num1) + int(num2)
    return HttpResponse("La suma es: ", suma)