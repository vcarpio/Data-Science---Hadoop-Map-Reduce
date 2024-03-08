#!/usr/bin/env python

import sys

current_citada = None
current_citantes = []

for line in sys.stdin:
    cited, citing = line.split(";")  # Se supone que los datos están en formato key-value

    if cited != current_citada:
        if current_citada:
            citantes_str = ', '.join(sorted(current_citantes))
            print('%s {%s}' % (current_citada, citantes_str))
        current_citada = cited
        current_citantes = []

    current_citantes.append(citing)

if current_citada:
    citantes_str = ', '.join(sorted(current_citantes))
    print('%s {%s}' % (current_citada, citantes_str))





