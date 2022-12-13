def numero(dime_numero):
    if dime_numero in range (1,11):
        tabla = open("tabla-"+str(dime_numero)+".txt", "w")
        for i in range(1,11):
            tabla.write(str(dime_numero)+"x"+str(i)+"="+str(dime_numero*i)+"\n")
        tabla.close()
    return
num = int(input("introduzca un numero del 1 al 10"))
numero(num)