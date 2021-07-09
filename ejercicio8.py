  
class Estructuras_Selectivas:    
     #Leer tres números enteros diferentes entre sí y determinar el número mayor de los tres.
    def __init__(self):
        pass

    def estructuraSel5(self):                             
        num1= int(input("Ingrese el primer número: "))
        num2= int(input("Ingrese el segundo número: "))
        num3= int(input("Ingrese el tercer número: "))
        if num1> num2 and num1> num3:
            print("El número mayor es {}" .format(num1))
        elif num2> num1 and num2> num3:
            print("El número mayor es {}" .format(num2))
        else:
            print("El número mayor es {}" .format(num3))

clase1= Estructuras_Selectivas()
clase1.estructuraSel5()