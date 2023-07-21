input1 = input("Ingrese un numero ")
input2 = input("Ingrese otro numero ")

if ((input1 == '') or (input2 == '')):
    print('Error: valor no valido')
else:
    num1 = int(input1)
    num2 = int(input2)
    if (num2 == 0):
        print('Error: no se puede dividir por 0')
    else:
        print(num1/num2)
