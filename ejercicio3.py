class Estructuras_Secuenciales : 
    
 #  Obtener la cantidad de dinero que recibirá un vendedor por concepto de comisiones por tres ventas realizadas en el mes, y el total que recibirá en el mes por sueldo y comisión. 
 # Se sabe que el vendedor recibe un sueldo base y un 10% extra por comisiones de todas sus ventas      
    def  __init__ (self):
        pass

    def  estructuraSec2 (self):                    
        sueldoBase =  float ( input ( "Ingrese su sueldo base:" ))
        venta1 =  float ( input ("Ingrese el valor de la primera venta realizada: "))
        venta2 =  float ( input ("Ingrese el valor de la segunda venta realizada: "))
        venta3 =  float ( input ("Ingrese el valor de la tercera venta realizada: "))
        totalVenta =  venta1 + venta2 + venta3
        Comisión = totalVenta * 0.1
        totalResivir =  sueldoBase + Comisión
        print ( "Su sueldo base es {}, mas las ventas realizadas {}, usted tuvo un total {}" .format(sueldoBase,totalVenta,totalResivir))

clase1 =  Estructuras_Secuenciales ()
clase1 . estructuraSec2 () 