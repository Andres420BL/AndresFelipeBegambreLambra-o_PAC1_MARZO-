#Crea un programa que solicite al usuario ingresar valores y este debe verificar cuando se ingresa una vocal, el programa 
# debe contar y mostrar la cantidad de vocales (a, e, i, o, u) ingresadas cuantas, de cada una y la cantidad total, importante 
# tener en cuenta que la aplicación se detiene con una opción de menú llamada finalizar. 


import os
os.system('cls')

contador_A=0
contador_e=0
contador_I=0
contador_O=0
contador_u=0
var_controlbln =True
while var_controlbln ==True:
    opcionint =int(input('Menu \n1 Conteo de vocales\n2.Finalizar'))

    if opcionint == 1:
        palabraStr=(input('Ingresa una Palabra------------------>'))
        for letra in palabraStr:
            if letra =='A' or letra =='a':
                contador_A+=1
            elif letra =='E' or letra =='e':
                contador_e+=1
            elif letra =='I' or letra =='i':
                contador_I+=1
            elif letra =='O' or letra =='o':
                contador_O+=1
            elif letra =='U' or letra =='u':
                contador_u+=1
                      
    if opcionint == 2:
        print('Contador de A---------------->',contador_A)
        print('Contador de B---------------->',contador_e)
        print('Contador de C---------------->',contador_I)
        print('Contador de o---------------->',contador_O)
        print('Contador de U---------------->',contador_u)
        print('Total de vocales---------------->',contador_I+contador_e+contador_A+contador_O + contador_u )

var_controlbln = False