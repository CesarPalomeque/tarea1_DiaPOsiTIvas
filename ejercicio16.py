class Estructuras_Ciclicas:  

    #
       
    def __init__(self):
        pass

    """Estructuras REPEAT"""
    def estructuraCic6(self):                          #EJERCICIO 16
        I=1
        serie=0
        num= int(input("Ingrese un número: "))
        band=True
        while band:
            if band ==True:
                serie= serie+(1/I)
                band= False
            else:
                serie= serie-(1/I)
                band= True
            I+=1
            if I>num:
                break
            print("El resultado de la serie es: {}" .format(serie))

clase1= Estructuras_Ciclicas()
clase1.estructuraCic6()