from flask import Flask, jsonify
import pymysql
import os

app = Flask(__name__)

def conectar():
    return pymysql.connect(
        host=os.getenv("DB_HOST", "mysql"),
        database=os.getenv("DB_NAME", "examen"),
        user=os.getenv("DB_USER", "admin"),
        password=os.getenv("DB_PASSWORD", "admin123"),
        port=3306,
        cursorclass=pymysql.cursors.DictCursor
    )

@app.route("/")
def inicio():
    return jsonify({
        "mensaje": "API del Examen Big Data",
        "consulta": "/resultados"
    })

@app.route("/resultados")
def resultados():
    try:
        conexion = conectar()
        cursor = conexion.cursor()

        cursor.execute("""
            SELECT hora, categoria, ingreso_total
            FROM resultados
            ORDER BY hora, categoria
        """)

        datos = cursor.fetchall()
        cursor.close()
        conexion.close()

        return jsonify([
            {
                "hora": fila["hora"],
                "categoria": fila["categoria"],
                "ingreso_total": float(fila["ingreso_total"])
            }
            for fila in datos
        ])

    except Exception as error:
        return jsonify({"error": str(error)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
