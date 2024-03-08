#!/usr/bin/python3

import sys

subproblema = None
Gasto_total = None
contador = None
for linea in sys.stdin:
    persona, tienda, gasto = linea.strip().split(";")
    gasto = int(gasto)

    if subproblema is None:
        subproblema = (persona, tienda)
        Gasto_total = 0
        contador = 0

    if subproblema == (persona, tienda):
        Gasto_total += gasto
        contador += 1
    else:
        print("%s;%s;%s;%s" % (subproblema[0], subproblema[1], Gasto_total, contador))
        subproblema = (persona, tienda)
        Gasto_total = gasto
        contador = 1

print("%s;%s;%s;%s" % (subproblema[0], subproblema[1], Gasto_total, contador))
