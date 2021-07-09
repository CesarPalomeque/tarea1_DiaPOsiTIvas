  
class Expresiones_Logicas:    
     
     #Una escuela aplica dos exámenes a sus aspirantes, por lo que cada uno de ellos obtiene dos calificaciones denotadas como C1 y C2.
     #  El aspirante que obtenga calificaciones mayores que 80 en ambos exámenes es aceptado; en caso contrario es rechazado.
    def __init__(self):
        pass

    #Expresiones lógicas  #USO DE "AND" "OR"
    def estructuraSel7(self):                                
        C1= int(input("Ingrese la primera calificación: "))
        C2= int(input("Ingrese la segunda calificación: "))
        if C1 >=80 and C2>=80:
            print("La calificacion 1: {},la calificación 2:{} es ACEPTADO" .format(C1,C2))
        else:
            print("La calificacion 1: {},la calificación 2:{} es RECHAZADO" .format(C1,C2))
    

    def estructuraSel8(self):
        C1= int(input("Ingrese la primera calificación: "))
        C2= int(input("Ingrese la segunda calificación: "))
        if C1 >=90 or C2>=90:
            print("La calificacion 1: {},la calificación 2:{} es ACEPTADO" .format(C1,C2))
        else:
            print("La calificacion 1: {},la calificación 2:{} es RECHAZADO" .format(C1,C2))

clase1= Expresiones_Logicas()
clase1.estructuraSel7()
clase1.estructuraSel8()