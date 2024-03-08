#!/usr/bin/python3

import sys
subproblema = None
gastoMedio = None
contador = None

for linea in sys.stdin:

    persona, tienda, gasto, cont = linea.split(";")
    gasto = int(gasto)
    cont = int(cont)
    if subproblema is None:
        subproblema = (persona, tienda)
        contador = 0
        gastoMedio = 0
    if subproblema == (persona, tienda):
        contador += cont
        gastoMedio += gasto
    else:
        print("%s;%s;%s" % (subproblema[0], subproblema[1], gastoMedio/contador))
        subproblema = (persona, tienda)
        contador = cont
        gastoMedio = gasto

print("%s;%s;%s" % (subproblema[0], subproblema[1], gastoMedio/contador))

