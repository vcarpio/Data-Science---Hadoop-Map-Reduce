#!/usr/bin/env python
import sys

for line in sys.stdin:
    if "," not in line:
        continue

    # para que ignore la primera linea
    if line == "CITING" or line == "CITED":
        continue

    citing, cited = line.strip().split(",", 1)
    print('%s %s' % (cited, citing))