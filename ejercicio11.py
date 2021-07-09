  
class Estructuras_Ciclicas:  
    #Calcular la suma de los cuadrados de los primeros 100 enteros y escribir el resultado.

    def __init__(self):
        pass
    
    #Estructuras FOR
    def estructuraCic1(self):                        
        i=1
        suma=0
        for i in range(100):
            suma= suma+i*i
            i+=1
        print("La suma de los 100 números es: {}" .format(suma))

clase1= Estructuras_Ciclicas()
clase1.estructuraCic1()