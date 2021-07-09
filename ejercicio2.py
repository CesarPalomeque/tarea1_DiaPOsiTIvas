class  Estructuras_Secuenciales : 
#Obtener la cantidad de dinero que tendrá que pagar el cliente, si la tienda ofrece un 15% de descuento sobre el total de la compra.

    def  __init__ (self):
        pass

    def  estructuraSec1 ( self ):                   
        totalCompra =  float ( input ( "Ingrese valor final de su compra:" ))
        descuento =  totalCompra * 0.15
        cantidadPagar =  totalCompra - descuento
        print ( "El valor de la compra es {}, su saldo total a pagar es {}".format(totalCompra,cantidadPagar))

clase1 =  Estructuras_Secuenciales ()
clase1.estructuraSec1 ()