import csv
import sys
import time
from collections import defaultdict

archivo = sys.argv[1] if len(sys.argv) > 1 else "data/ventas_125053549.csv"

inicio = time.time()
resultados = defaultdict(float)

with open(archivo, "r", encoding="utf-8") as f:
    lector = csv.DictReader(f)

    for fila in lector:
        try:
            hora = fila["fecha_hora"].split(" ")[1].split(":")[0]
            categoria = fila["categoria"]
            cantidad = float(fila["cantidad"])
            precio = float(fila["precio_unitario"])

            resultados[(hora, categoria)] += cantidad * precio

        except (KeyError, ValueError, IndexError):
            continue

for (hora, categoria), ingreso in sorted(resultados.items()):
    print(f"{hora}\t{categoria}\t{ingreso:.2f}")

fin = time.time()

print(f"\nTiempo secuencial: {fin - inicio:.4f} segundos", file=sys.stderr)
