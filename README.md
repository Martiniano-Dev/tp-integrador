# 🎬 Análisis de Películas con Pandas

Este proyecto realiza un análisis exploratorio de datos de películas utilizando **Python** y **pandas**, a partir de un archivo Excel con distintas hojas que representan décadas cinematográficas.  

El script combina, limpia y analiza la información para obtener estadísticas sobre países, directores, décadas y calificaciones de IMDb.

---

## 📁 Contenido del proyecto

- `movies.xls`: Archivo de entrada con los datos de películas organizados por décadas (`1900s`, `2000s`, `2010s`).
- `analisis_peliculas.py`: Script principal (el código de este repositorio).
- `movies_limpio.xlsx`: Archivo de salida generado automáticamente con los datos limpios.

---

## 🧠 Funcionalidades principales

El código realiza las siguientes tareas paso a paso:

1. **Lectura de datos** desde las tres hojas del Excel (`1900s`, `2000s`, `2010s`).
2. **Exploración inicial** de las primeras filas de cada conjunto.
3. **Unificación** de todas las décadas en un único DataFrame.
4. **Estadísticas generales**, incluyendo:
   - Cantidad de películas por país
   - Top 5 directores de los años 2010
   - Top 5 películas con mejor puntaje IMDb
   - Promedio de puntaje IMDb por país  
   - Cantidad de películas por década
5. **Limpieza de datos** (eliminación de filas sin puntaje IMDb).
6. **Exportación** del DataFrame limpio a un nuevo archivo Excel: `movies_limpio.xlsx`.

---

## 🧩 Requisitos

Antes de ejecutar el script, asegúrate de tener instalado:

```bash
pip install pandas
```
---
