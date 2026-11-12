# Examen Segundo Parcial
## Pipeline de datos contenerizado

**Materia:** Manejo Masivo de Datos  
**Matrícula:** 125053549

## 1. Descripción

Proyecto de procesamiento de datos masivos mediante Docker, Hadoop Streaming, Python, MySQL y Flask.

Se generó un dataset de 5,000,000 registros de ventas. El análisis calcula el ingreso total por hora del día (0 a 23) y categoría.

**Fórmula:** ingreso = cantidad * precio_unitario

## 2. Estructura del proyecto

- `generar_dataset.py`: genera los datos de ventas.
- `hadoop/`: configuración de Hadoop.
- `mapreduce/mapper.py`: extrae hora, categoría e ingreso.
- `mapreduce/reducer.py`: suma los ingresos por grupo.
- `mapreduce/secuencial.py`: realiza el análisis secuencial.
- `api/`: aplicación Flask.
- `scripts/cargar_resultados.py`: guarda los resultados en MySQL.
- `docker-compose.yml`: configura los servicios.
- `evidencias/`: contiene las pruebas.

## 3. Tecnologías utilizadas

- Docker y Docker Compose.
- Hadoop 3.4.3 con Hadoop Streaming.
- Python 3.
- MySQL 8.0.
- Flask.
- PyMySQL.

## 4. Generación del dataset

Se generaron 5,000,000 registros utilizando la matrícula de nueve dígitos como semilla aleatoria.

Archivo generado: `ventas_125053549.csv`.

## 5. Procesamiento MapReduce

Se utilizó Hadoop Streaming para procesar los cinco millones de registros. El Mapper calcula el ingreso de cada venta y genera la clave hora-categoría. El Reducer suma los ingresos correspondientes a cada grupo.

Se obtuvieron 240 agrupaciones.

## 6. Comparación de resultados

| Método | Tiempo |
|---|---:|
| Secuencial | 11.90 segundos |
| Hadoop Streaming | 20.09 segundos |

Ambos métodos generaron exactamente los mismos 240 resultados.

## 7. Base de datos MySQL

Los 240 resultados se almacenaron correctamente en la tabla `resultados`.

## 8. API REST

Se desarrolló una API con Flask que devuelve los resultados almacenados en MySQL en formato JSON.

- Ruta principal: `http://localhost:5000/`
- Consulta de resultados: `http://localhost:5000/resultados`

## 9. Docker Compose

El proyecto utiliza tres servicios: Hadoop, MySQL y API Flask. La configuración fue validada correctamente.

## 10. Autenticación SSH

Se configuró autenticación mediante clave ED25519 para el usuario `hadoop`. La prueba de conexión devolvió `SSH_OK`.

## 11. Evidencias

En la carpeta `evidencias/` se encuentra el archivo `verificacion_pipeline.txt`, que contiene el resumen de las pruebas realizadas.
