class Estructuras_Selectivas: 
    #1. Determinar la cantidad de dinero que recibirá un trabajador por concepto de las horas extras trabajadas en una empresa, 
    # sabiendo que cuando las horas de trabajo exceden de 40, 
    # el resto  se consideran horas extras y que éstas se pagan al doble de una hora normal cuando no exceden de 8;
    # si las horas extras exceden de 8 se pagan las primeras 8 al  doble de lo que se paga por una hora normal y el resto al triple.

    def __init__(self):
        pass

    #Estructuras selectivas compuestas       
    def estructuraSel4(self):                            
        horasTrabajadas= int(input("Ingrese las horas que trabajó: "))
        pagoHoras= float(input("Ingrese el pago de la hora normal: "))
        if horasTrabajadas > 40:
            horasExtras= horasTrabajadas-40
            if horasExtras > 8:
                horaextrasTrabajadas= horasExtras-8
                paghe= (pagoHoras*2*8) + (pagoHoras*3*horaextrasTrabajadas)
            else:
                paghe= pagoHoras*2*horasExtras
            pagt= pagoHoras*40+paghe
        else:
            pagt= pagoHoras*horasTrabajadas
        print("El pago total por las horas trabajadas es {}" .format(pagt))

clase1= Estructuras_Selectivas()
clase1.estructuraSel4()