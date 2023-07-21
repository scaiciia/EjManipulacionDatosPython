num1 = int(input('Ingrese un numero '))
num2 = int(input('Ingrese otro numero '))

if (num1 > num2):
    print(str(num1) + ' es mayor que ' + str(num2))
elif (num2 > num1):
    print(str(num2) + ' es mayor que ' + str(num1))
else:
    print('Ambos numeros son iguales')
