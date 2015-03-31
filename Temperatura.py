#!/usr/bin/env python
# _*_ coding: latin1 _*_

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