  
class Estructuras_Selectivas:     
    # el ejercicio pide que se haga un programa donde el alumno ingrese su nota final de su examen para asi decirle si aprobo.
    def __init__(self):
        pass

    #Estructuras selectivas simples      
    def estructuraSel1(self): 
        calificacion= float(input("Ingrese la calificación del examen que obtuvo el estudiante: "))
        if calificacion >=7:
            print("La nota es {}, APROBADO" .format(calificacion))

clase1= Estructuras_Selectivas()
clase1.estructuraSel1()