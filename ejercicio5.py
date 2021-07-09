class Estructuras_Selectivas:   
    #Dado como dato la calificación de un alumno en un examen, escriba “aprobado” si su calificación es mayor o igual que 7 y “Reprobado” en caso contrario.
    def __init__(self):
        pass

   #Estructuras selectivas dobles        
    def estructuraSel2(self):                            
        calificacion= float(input("Ingrese la calificación del examen que obtuvo el estudiante: "))
        if calificacion >=7:
            print("La nota es {}, APROBADO" .format(calificacion))
        else:
            print("La nota es {}, REPROBADO" .format(calificacion))

clase1= Estructuras_Selectivas()
clase1.estructuraSel2()