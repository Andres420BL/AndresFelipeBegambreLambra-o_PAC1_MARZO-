#Crea un programa que solicite al usuario ingresar un número entero positivo (N). El programa debe mostrar la tabla de multiplicar del número, teniendo en cuenta que se debe generar la tabla con los primeros 10 valores de dicha tabla. 

numeroint = int(input('Ingrese un numero ENTERO Positivo'))

while numeroint < 1:
    print("El numero debe ser mayor")
    numeroint = int(input("Por favor ingrese otro numero"))
    

if numeroint >= 1:
    print('1 *',numeroint,'=',numeroint*1)
    print('2 *',numeroint,'=',numeroint*2)
    print('3 *',numeroint,'=',numeroint*3)
    print('4 *',numeroint,'=',numeroint*4)
    print('5 *',numeroint,'=',numeroint*5)
    print('6 *',numeroint,'=',numeroint*6)
    print('7 *',numeroint,'=',numeroint*7)
    print('8 *',numeroint,'=',numeroint*8)
    print('9 *',numeroint,'=',numeroint*9)
    print('10 *',numeroint,'=',numeroint*10)

  
 

     
