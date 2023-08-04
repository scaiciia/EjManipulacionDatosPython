"""
Resolver el siguiente ejercicio de programación:
El empleado llamado Juan cobró 300 dólares por mes desde enero a junio, 
500 dólares de julio a octubre, y 700 dólares por mes en noviembre y 
en diciembre. 

En base al escenario propuesto, se le solicita a los estudiantes 
que creen un pequeño programa que calcule el sueldo promedio del 
empleado Juan. Además, se debe indicar sí Juan se encuentra cobrando 
un sueldo bajo, normal o mejor de lo normal, considerando las 
siguientes pautas:

a. Sueldo bajo: por debajo de 300 dólares.
b. Sueldo normal:  entre 300 a 900.
c. Sueldo mejor de lo normal: más de 900 dólares.


Tip: se debe utilizar estructuras condicionales.
"""

def clasifSueldo(valor):
    if (valor < 300):
        rta = 'bajo'
    elif (valor > 900):
        rta = 'mejor de lo normal'
    else:
        rta = 'normal'
    return rta

sueldo = {'Enero': 300, 'Febrero': 300, 'Marzo': 300, 'Abril': 300, 'Mayo': 300, 'Junio': 300, 'Julio': 500, 'Agosto': 500, 'Septiembre': 500, 'Octubre': 500, 'Noviembre': 700, 'Diciembre': 700}
suma = 0

for mes, monto in sueldo.items():
    suma = suma + monto
    print("El sueldo del mes de {} es un sueldo {}".format(mes, clasifSueldo(monto)))

promedio = suma / len(sueldo.keys())

print("El sueldo promedio es ${:.2f} y es un sueldo {}".format(promedio, clasifSueldo(promedio)))