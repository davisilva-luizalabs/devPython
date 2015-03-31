#!/usr/bin/env python
# _*_ coding: latin1 _*_

#Para i uma lista  234, 654, 378, 789:
for i in [234,654,378,798]:

    #se o resto dividindo por 3 for igual a zero:
    if i % 3 == 0:

        #imprime
        print i, '/ 3 = ', i / 3


temp = int(raw_input('Entre com a Temperatura: '))

if temp < 0:
    print 'Congelando'
elif 0 <= temp <= 20:
    print 'Frio'
elif 21 <= temp <= 25:
    print 'Normal'
elif 26 <= temp <= 35:
    print 'Quente'
else:
    print 'Muito Quente !!!'