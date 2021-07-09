class Estructuras_Ciclicas:   

    #Calcular el factorial de N números enteros leídos de teclado

    def __init__(self):
        pass

    #Bucles anidados
    def estructuraCic7(self):                         #EJERCICIO 17
        num= int(input("Ingrese un número: "))
        factorial=1
        for i in range(1, num+1):
            factorial*=i
        print("El factorial del número {} es: {}" .format(num, factorial))

clase1= Estructuras_Ciclicas()
clase1.estructuraCic7()