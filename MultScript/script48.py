#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 16:07:26 2020

@author: llabori
"""
""" Ejemplos utilizando la instruccion print() """

# Primer Ejemplo
print("Python")
Luna = 385000

# Segundo Ejemplo
print('D.M Tierra - Luna', Luna, 'Km')

# Tercer Ejemplo
print('D.M Tierra - Luna '+str(Luna)+' Km')

# Cuarto Ejemplo 
print("\nHOLA\nUSUARIOS\nDE PYTHON\n")

# Quinto Ejemplo 
print('Continuara.....', end=' ')
print('\n')
print('otro dia.....')

# Sexto Ejemplo
lu = 'Quito (Ecuador)'
la = -0.216979
lo = -78.51627
cu = repr(lu)+': '+ repr(la) + ',' + repr(lo) # Concatena con formato de interprete
print(cu)

# Septimo Ejemplo
alt = 110
dis = 550
edi = 'La Giralda'
est = 'Antares'
print('{} mide {} metros '.format(edi, alt))

# Septimo Ejemplo
print('{1} metros : {0}'.format(edi,alt))
print('{c}:{p} '.format(c='Lima', p='Peru'))

# Muestra redondeo con 2 o 3 decimales
val1 = 8.56767
val2 = 9.45548
print('{0:.3} {1:.4} '.format(val1, val2))

# Rellena con guiones bajos
print('{0:_^30} '.format('Sevilla'))

# Rellenamos con ceros a la izquierda
val3 = 34
print(str(val3).zfill(4))

# Imprime un valor como flotante con cierta cantidad de digitos decimales
val4 = 2.34565676
print('Valor aprox. {0:.3f} '.format(val4))

# Insertar salto de linea antes de imprimir
print('\nCodigos Postales')

# Imprimimos los valores contenidos en un diccionario
correos = {'SJ' : 300, 'LR': 309, 'B': 310}
for cod, loc in correos.items():     # recorremos todos los registros del diccionario
    # muestra lista de pares con formatos
    print('{0:5}:{1:4d} '.format(cod, loc))
    
# Muestra la tabla de multiplicar
print("\nLa tabla de multiplicar")         # Muestra la tabla de multiplicar
for i in range(1, 11):                     # Recorrer los numeros del 1 al 10
    print(repr(i)+':')
    for y in range(1, 11):                 # Recorrer los numeros del 1 al 10
        print(repr(i).ljust(2),'* ',end='') # Muestra operadores
        print(repr(y).ljust(3), end='')    
        print(' =' + repr(i*y).center(5))  # Muestra el resultado de la linea
    
# Ejemplo de impresion utilizando comodines: 
# %s (cadena), %i (entero), %f (número con decimales)
#
# Los datos también se pueden tabular reservando un número
# determinado de caracteres:
# Ejemplo: %10s  reserva 10 posiciones y alinea a la izquierda
#          %-10s reserva 10 posiciones y alinea a la derecha
        
nombre = 'Claudio'
edad = 35
altura = 1.86

print('Tiene %i años de edad' %edad)
print('%s tiene %i años de edad y mide %f' %(nombre, edad, altura))
print('\n')

# Presentacion Tabulando los datos a mostrar
personas = [('Claudio', 35, 1.826),
            ('Elena', 24, 1.84),
            ('Manuel', 9, 1.449),
            ('Isabel', 34, 1.72)]

for persona in personas:
    nombre = persona[0]
    edad = persona[1]
    altura = persona[2]
    print('%-8s tiene %2i años y mide %1.2f' %(nombre, edad, altura))

    
    


