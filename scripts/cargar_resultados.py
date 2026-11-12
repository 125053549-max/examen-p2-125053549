import sys
import pymysql
import os

conexion = pymysql.connect(
    host=os.getenv("DB_HOST", "mysql"),
    database=os.getenv("DB_NAME", "examen"),
    user=os.getenv("DB_USER", "admin"),
    password=os.getenv("DB_PASSWORD", "admin123"),
    port=3306
)

cursor = conexion.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS resultados (
        hora INT NOT NULL,
        categoria VARCHAR(100) NOT NULL,
        ingreso_total DECIMAL(15,2) NOT NULL,
        PRIMARY KEY (hora, categoria)
    )
""")

cursor.execute("DELETE FROM resultados")

for linea in sys.stdin:
    partes = linea.strip().split("\t")

    if len(partes) != 3:
        continue

    hora, categoria, ingreso = partes

    cursor.execute(
        """
        INSERT INTO resultados (hora, categoria, ingreso_total)
        VALUES (%s, %s, %s)
        """,
        (int(hora), categoria, ingreso)
    )

conexion.commit()
cursor.close()
conexion.close()

print("Resultados guardados correctamente en MySQL.")
