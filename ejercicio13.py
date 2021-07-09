class Estructuras_Ciclicas:     

    #Diseñe un código para calcular la suma y producto de N números enteros, utilizando un bucle controlado por el usuario.

    def __init__(self):
        pass

      #BUCLE CONTROLADO POR CONDICIÓN
    def estructuraCic3(self):         
        suma=0
        producto=1
        print("Desea continuar [S/N]:  ")
        resp= input().capitalize()
        while resp == "S":
            num= int(input("Ingrese un número: "))
            suma= suma+num
            producto= producto*num
            print("El total de la suma es: {}" .format(suma))
            print("El total del producto es: {}" .format(producto))
            print("Desea continuar [S/N]:  ")
            resp=input().capitalize()

clase1= Estructuras_Ciclicas()
clase1.estructuraCic3()