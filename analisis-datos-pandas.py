import pandas as pd

archivo_excel = "movies.xls"

data_1900s = pd.read_excel(archivo_excel, sheet_name="1900s")
data_2000s = pd.read_excel(archivo_excel, sheet_name="2000s")
data_2010s = pd.read_excel(archivo_excel, sheet_name="2010s")

print("Primeras 5 filas de la hoja 2000s:\n")
print(data_2000s.head())

print("\nLa hoja 2010s contiene", data_2010s.shape[0], "filas.")

df_movies = pd.concat([data_1900s, data_2000s, data_2010s], ignore_index=True)

muestra_10 = df_movies.head(10)
print("\nPrimeras 10 filas del DataFrame unificado:\n")
print(muestra_10)

peliculas_por_pais = df_movies["Country"].value_counts()
print("\nCantidad de películas por país:\n", peliculas_por_pais)

mejores_directores_2010s = data_2010s["Director"].value_counts().nlargest(5)
print("\nTop 5 directores (2010s):\n", mejores_directores_2010s)

top_peliculas = df_movies.sort_values("IMDB Score", ascending=False).head(5)
print("\nTop 5 películas por IMDB Score:\n")
print(top_peliculas[["Title", "IMDB Score"]])

promedio_imdb_pais = df_movies.groupby("Country")["IMDB Score"].mean()
print("\nPromedio de IMDB Score por país:\n", promedio_imdb_pais)

df_movies["Decade"] = (df_movies["Year"] // 10) * 10
peliculas_por_decada = df_movies["Decade"].value_counts().sort_index()
print("\nCantidad de películas por década:\n", peliculas_por_decada)

print("\nInformación general del DataFrame:")
df_movies.info()

df_limpio = df_movies.dropna(subset=["IMDB Score"])

salida = "movies_limpio.xlsx"
df_limpio.to_excel(salida, index=False)
print(f"\nArchivo '{salida}' exportado exitosamente.")