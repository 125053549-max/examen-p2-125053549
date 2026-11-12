#!/usr/bin/env python3
import sys
import csv

for linea in sys.stdin:
    try:
        fila = next(csv.reader([linea]))

        if fila[0] == "id":
            continue

        fecha = fila[1]
        hora = fecha.split(" ")[1].split(":")[0]
        categoria = fila[3]

        cantidad = float(fila[5])
        precio = float(fila[6])

        ingreso = cantidad * precio

        clave = f"{hora}|{categoria}"
        print(f"{clave}\t{ingreso:.2f}")

    except (ValueError, IndexError):
        continue
