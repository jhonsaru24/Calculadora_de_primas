# Importamos las librerías
import requests                  # Para el procedimiento de los municipios
from bs4 import BeautifulSoup    # Para el procedimiento de los municipios
 
print('\n')
print('*********************************************')
print('**BIENVENIDOS AL SISTEMA DE CALCULAR PRIMAS**')
print('*********************************************\n')
 
# ----------------------------------------------------------------------------------------
                                     # Municipios
# ----------------------------------------------------------------------------------------
# URL de la página que contiene la lista de municipios
url = 'https://es.wikipedia.org/wiki/Wikiproyecto:Colombia/Listado_de_municipios'
 
# Hacer una solicitud HTTP a la página donde se extraeran los datos
page = requests.get(url)
 
 
# COMPROBAR QUE LA SOLICITUD FUE EXITOSA .....................................
if page.status_code == 200:
 
    # html.parser analizara la página para bajar el contenido html
    soup = BeautifulSoup(page.text, 'html.parser')
 
    # Seleccionamos los datos que necesitamos ----------------------------
 
    # Buscar un div en específico que contiene los datos de los municipios
    div_contenedor = soup.find('div', id='mw-content-text')  
    # Si se encuentra el div
    if div_contenedor:
        # Buscar la lista ordenada (ol) dentro del div
        ol_element = div_contenedor.find('ol')
        
        # Si se encuentra la lista ordenada
        if ol_element:
            # Buscar los elementos 'a' dentro de la lista ordenada
            #   'a'         --->   Seleccionamos todos los elementos con esa etiqueta
            #   'href=True' --->   (palabra clave) Al usar href=True, estamos especificando que queremos encontrar solo los enlaces (<a>) que tienen el atributo href': Seleccionamos todos los elementos con esa etiqueta
            #   'title=True'--->   (palabra clave) Al usar title=True, estamos especificando que queremos encontrar solo los enlaces (<a>) que tienen el atributo title.
            link_municipios = ol_element.find_all('a', href=True, title=True)
 
    # Extraer el atributo title de cada enlace, es decír el nombre del municipio
    # Para esto se utiliza una lista por comprensión para extraer los valores del atributo. Estos se almacenan en un arreglo
    municipios = [link['title'] for link in link_municipios]
 
    # Convertir la lista en una cadena
    municipios_str = ', '.join(municipios)
 
    # Convertir la cadena en una lista utilizando como separador la coma y el espacio
    lista_municipios = municipios_str.split(", ")
 

else:
    print(f'Error al acceder a la página: {page.status_code}')

while True: 
    def recolectar_datos_municipio():
        while True:
            print('\nTener en cuenta que la primera letra de cada palabra del municipio debe ir en mayúscula (con tíldes)\ny si es necesario ingresar el nombre del departamento entre parentesís \nPor ejemplo: Bello (Antioquía)\n')
            nom_municipio2 = input('Ingrese el nombre del municipio: ')
            
            if not nom_municipio2:
                print("Error: El nombre del municipio no puede estar vacío.")
            elif nom_municipio2  not in str(municipios).lower():
                print("Error: El nombre del municipio no esta en la lista. Intentelo nuevamente")
            elif nom_municipio2  in municipios:
                break  # Sale del bucle si el municipio no está vacío y está en la lista
    
        while True:
            try:
                cant_hombres = int(input('Ingrese la cantidad de hombres adultos: '))
                if cant_hombres < 0:
                    raise ValueError("La cantidad de hombres adultos no puede ser negativa.")
                else:
                    break   # Se sale del bucle si la cantidad que ingresa el usuario es es >= 0 y si es un caracter numerico
            except ValueError:
                print("Error: Ingrese un número entero positivo para la cantidad de hombres adultos.")
    
        while True:
            try:
                cant_mujeres = int(input('Ingrese la cantidad de mujeres adultas: '))
                if cant_mujeres < 0:
                    raise ValueError("La cantidad de mujeres adultas no puede ser negativa.")
                else:
                    break
            except ValueError:
                print("Error: Ingrese un número entero positivo para la cantidad de mujeres adultas.")
    
        while True:
            try:
                cant_ninos = int(input('Ingrese la cantidad de niños: '))
                if cant_ninos > 500:
                    raise ValueError("La cantidad de niños no puede ser mayor a 500.")
                elif cant_ninos < 0:
                    raise ValueError("La cantidad de niños no puede ser negativa o no debe estar vacía.")
                else:
                    break
            except ValueError:
                print("Error: Ingrese un número entero positivo para la cantidad de niños menor o igual a 500.")
    
        while True:
            try:
                cant_ninas = int(input('Ingrese la cantidad de niñas: '))
                if cant_ninas > 500:
                    raise ValueError("La cantidad de niñas no puede ser mayor a 500.")
                if cant_ninas < 0:
                    raise ValueError("La cantidad de niñas no puede ser negativa o no debe estar vacía.")
                else:
                    break
            except ValueError:
                print("Error: Ingrese un número entero positivo para la cantidad de niñas menor o igual a 500.")
    
        # retorna los valores
    
        return nom_municipio2, cant_hombres, cant_mujeres, cant_ninos, cant_ninas
    
    if __name__ == "__main__":
        nom_municipio2, cant_hombres, cant_mujeres, cant_ninos, cant_ninas = recolectar_datos_municipio()
    
    
    print('\n')
    # sumamos la cantidad de los niños y niñas para hacer la comparación
    
    total_cant_ninos = cant_ninos + cant_ninas
    
    if total_cant_ninos > 0 and total_cant_ninos <= 100:
        primaPorNino = 30000
    elif total_cant_ninos >= 101 and total_cant_ninos <= 200:
        primaPorNino = 25000
    elif total_cant_ninos >=201 and total_cant_ninos <= 500:
        primaPorNino = 20000
    else:
        primaPorNino = 0
        print('Rango no admitido')

    
    #Se hace la realización de los calculos para el total de adultos y el valor total de las primas
    
    total_adultos = cant_hombres + cant_mujeres
    primaPorTodosLosNinos = (total_cant_ninos * primaPorNino)
    
    # Aquí muestramos el resultado de los datos obtenidos del programa
    print('La prima a pagar por cada uno de los niños es de: '+ str(primaPorNino))
    print('El nombre del Municipio es: ', nom_municipio2)
    print('La cantidad de adultos (Hombres) es: ', cant_hombres)
    print('La cantidad de adultos (Mujeres) es: ', cant_mujeres)
    print('La cantidad de niños es: ', cant_ninos)
    print('La cantidad de niñas es: ', cant_ninas)
    print('La cantidad de adultos en el municipio de', nom_municipio2,'es de: ', total_adultos, ', y la cantidad total de niños es de: ', total_cant_ninos)
    print('El monto de prima por mantenimiento de los niños es de: $'+ str(primaPorTodosLosNinos))
    salida = input('Desea continuar? s/n: ')
    if salida.lower() == 's':
        print('Gracias por utilizar el programa')
    elif salida.lower() == 'n':
        print('¡Programa terminado!')
        break
    else:
        print('Error: Ingrese una opción válida')
