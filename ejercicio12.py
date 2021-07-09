class Estructuras_Ciclicas:   

      #Elabore pseudocódigo para el caso en que se desean escribir los números del 1 al 100

    def __init__(self):
        pass

    #Estructuras WHILE
    def estructuraCic2(self):    #BUCLE CONTROLADO POR CONTADOR      #EJERCICIO 12
        i=1
        while i<=100:
            print("El numero es: {}" .format(i))
            i+=1
        return i

clase1= Estructuras_Ciclicas()
clase1.estructuraCic2()