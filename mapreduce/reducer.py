#!/usr/bin/env python3
import sys

actual = None
total = 0.0

for linea in sys.stdin:
    try:
        clave, ingreso = linea.strip().split("\t")
        hora, categoria = clave.split("|", 1)
        ingreso = float(ingreso)

        if actual is not None and clave != actual:
            print(f"{actual.split('|')[0]}\t{actual.split('|')[1]}\t{total:.2f}")
            total = 0.0

        actual = clave
        total += ingreso

    except ValueError:
        continue

if actual is not None:
    hora, categoria = actual.split("|", 1)
    print(f"{hora}\t{categoria}\t{total:.2f}")
