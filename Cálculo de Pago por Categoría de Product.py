import os
os.system('cls')

#Escribe un programa en Python que permita calcular el pago de un producto en una tienda, tomando en cuenta que los productos se encuentran clasificados en cinco categorías: Ferretería, Aseo, Seguridad, Alimentos y Electrodomésticos. Cada categoría tiene un descuento diferente aplicado al precio del producto, el cual debe presentar un menú de opciones donde solo se termina el sistema con la opción “TERMINAR”. Descuentos por Categoría: Ferretería: 10% Aseo: 5% Seguridad: 15% Alimentos: 8% Electrodomésticos: 12% 
# El programa debe solicitar al usuario ingresar la categoría y el precio de cada producto comprado, y luego calcular el precio final con el descuento 
# aplicado. Al finalizar, debe mostrar la cantidad de productos comprados por cada categoría y el total recaudado

descuento_ferreteria=0.10
descuento_Aseo=0.05
descuento_seguridad=0.15
descuento_Alimentos= 0.08
descuento_electrodomesticos = 0.12
acumulador_ferreteria = 0
acumulador_aseo=0
acumulador_seguridad=0
acumulador_alimentos=0
acumulador_electrodomesticos =0
var_totalGFLT =0
var_controlBln = True
nombreStr=input('Ingrese su nombre------------------------->')
identificacionint=int(input('Ingrese su idetificacion------>'))
while var_controlBln== True:
    opcionint=int(input('Menu de Tienda\nCategoria de productos\n1.Ferreteria\n2.Aseo\n3.Seguridad\n4.Alimentos\n5.Electrodomesticos\n6.Terminar------>'))
    
    if opcionint ==1:
        precioflt=float(input('Ingrese el precio del producto'))
        cantidadint=int(input('Ingrese la cantidad del producto'))
        precio_productoint=(precioflt*cantidadint)
        descuento_finalflt=(precio_productoint*descuento_ferreteria)
        var_totalGFLT +=(precio_productoint-descuento_finalflt)
        acumulador_ferreteria +=cantidadint 
        
    if opcionint ==2:
        precioflt=float(input('Ingrese el precio del producto'))
        cantidadint=int(input('Ingrese la cantidad del producto'))
        precio_productoint=(precioflt*cantidadint)
        descuento_finalflt=(precio_productoint*descuento_Aseo)
        var_totalGFLT+=(precio_productoint-descuento_finalflt) 
        acumulador_aseo+=cantidadint
        
    if opcionint ==3:
        precioflt=float(input('Ingrese el precio del producto'))
        cantidadint=int(input('Ingrese la cantidad del producto'))
        precio_productoint=(precioflt*cantidadint)
        descuento_finalflt=(precio_productoint*descuento_seguridad)
        var_totalGFLT+=(precio_productoint-descuento_finalflt)
        acumulador_seguridad+=cantidadint
         
    if opcionint ==4:
        precioflt=float(input('Ingrese el precio del producto'))
        cantidadint=int(input('Ingrese la cantidad del producto'))
        precio_productoint=(precioflt*cantidadint)
        descuento_finalflt=(precio_productoint*descuento_Alimentos)
        var_totalGFLT += (precio_productoint-descuento_finalflt) 
        acumulador_alimentos+=cantidadint
        
    if opcionint ==5:
        precioflt=float(input('Ingrese el precio del producto'))
        cantidadint=int(input('Ingrese la cantidad del producto'))
        precio_productoint=(precioflt*cantidadint)
        descuento_finalflt=(precio_productoint*descuento_electrodomesticos)
        var_totalGFLT +=(precio_productoint-descuento_finalflt) 
        acumulador_electrodomesticos +=cantidadint
        
    if opcionint==6:
        print('\tFactura')
        print('Nombre----------------------------------------------------->',nombreStr)
        print('Identificacion--------------------------------------------->',identificacionint) 
        print('Cantidad de productos comprados de ferreteria-------------->',acumulador_ferreteria)
        print('Cantidad de productos comprados de aseo-------------------->',acumulador_aseo)
        print('Cantidad de productos comprados de seguridad--------------->',acumulador_seguridad)
        print('Cantidad de productos comprados de alimentos--------------->',acumulador_alimentos)
        print('Cantidad de productos comprados de electrodomesticos------->',acumulador_electrodomesticos)
        print('Total de la compra----------------------------------------->',var_totalGFLT,'$')
    
var_controlBlnl =False 