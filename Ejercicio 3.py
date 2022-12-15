import os.path


def busca_tabla(dime_numero, por_cuanto):
    """Esta funcion busca el fichero con la tabla de multiplicar que usted introduzca
    PARAMETROS:
                dime_numero: tabla que se quiere buscar"""
    if dime_numero in range(1, 11):
        busqueda = "tabla-"+str(dime_numero)+".txt"
        if os.path.isfile(busqueda) == True:
            fichero = open(busqueda,"r")
            multiplicacion = fichero.readlines()

            return print(multiplicacion[por_cuanto-1])
        else:
            print("Este fichero no existe")
num = int(input("Introduzca el numero de la tabla que quiera buscar \n"))
por = int(input("Introduzca el numero \n"))
busca_tabla(num, por)