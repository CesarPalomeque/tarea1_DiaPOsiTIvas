class Estructuras_Ciclicas:  
    #Determinar si un número entero proporcionado por el usuario es primo. 
    # Un número primo es un entero que no tiene más divisores que él mismo y la unidad. Elaborar código

    def __init__(self):
        pass

    def estructuraCic5(self):    #BUCLE CONTROLADO POR BANDERAS O INTERRUPTORES         
        primo= True
        divisor=2
        num= int(input("Ingrese un número: "))
        while divisor<num and primo==True:
            res= num%divisor
            if res==0:
                primo= False
            divisor+=1
        if primo== True:
            print("El número {} es primo" .format(num))
        else:
            print("El número {} no es primo" .format(num))

clase1= Estructuras_Ciclicas()
clase1.estructuraCic5()