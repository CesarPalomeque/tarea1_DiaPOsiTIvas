class Estructuras_Ciclicas:

    #Diseñe un pseudocódigo para calcular la suma y producto de N números enteros, utilizando un bucle controlado por condicion.
         
    def __init__(self):
        pass

    def estructuraCic4(self):    
        sum=0
        prod=1
        num= int(input("Ingrese un número: "))
        while num!=-1:
            sum= sum+num
            prod= prod*num
            print("El total de la suma es: {}" .format(sum))
            print("El total del producto es: {}" .format(prod))
            num= int(input("Ingrese un número: "))

clase1= Estructuras_Ciclicas()
clase1.estructuraCic4()