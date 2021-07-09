class Estructuras_Selectivas:    

    #Dado el sueldo de un empleado, encontrar el nuevo sueldo si obtiene un aumento del 10% si su sueldo es inferior a $600, en caso contrario no tendrá aumento.
    def __init__(self):
        pass

    def estructuraSel3(self):                          
        sueldoInicial= float(input("Ingrese el sueldo que poseía: "))
        if sueldoInicial <= 600:
            nuevoSueldo= sueldoInicial+(sueldoInicial*0.1)
            print("Su nuevo sueldo es {}" .format(nuevoSueldo))
        else:
            nuevoSueldo= sueldoInicial
            print("Su sueldo sigue siendo {}" .format(nuevoSueldo))

clase1= Estructuras_Selectivas()
clase1.estructuraSel3()