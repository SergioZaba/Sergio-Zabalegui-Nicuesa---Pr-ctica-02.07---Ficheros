def numero(dime_numero):
    """Esta funcion te crea un fichero con la tabla de multiplicar del numero que introduzca el usuario
PARAMETROS:
           dime_numero: El numero que introduzca el usuario """
    if dime_numero in range (1,11):
        tabla = open("tabla-"+str(dime_numero)+".txt", "w")
        for i in range(1,11):
            tabla.write(str(dime_numero)+"x"+str(i)+"="+str(dime_numero*i)+"\n")
        tabla.close()
    return
num = int(input("introduzca un numero del 1 al 10"))
numero(num)