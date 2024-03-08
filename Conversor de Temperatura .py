#Escribe un programa que permita al usuario convertir una temperatura en grados centígrados a Fahrenheit o viceversa. El programa debe solicitar al usuario ingresar la temperatura y la unidad de medida (C para Celsius, F para Fahrenheit) y luego realizar la conversión correspondiente, el programa debe manejar un menú de opciones y solo detenerse cuando se presione la opción finalizar.

import os
os.system('cls')

var_controlBln = True
while var_controlBln == True:
    opcionint=int(input('Menu de opcines\n1.Convertir de fahrenheit a celcius\n2.Convertir de Celcius a fahrenheit\n3.Finalizar '))
    
    if opcionint == 1:
        var_temperaturaint =int(input('Ingrese la temperatura fahrenheit a convertir-------->'))
        conversionflt =float(var_temperaturaint-32)*5/9
        
        
    if opcionint == 2:
        var_temperaturaint =int(input('Ingrese la temperatura celcius a convertir-------->'))
        conversionflt=float(var_temperaturaint*9/5)+32
        
    if opcionint == 3:
        print('La conversion final es --------------->',conversionflt)
        
var_controlBln = False
