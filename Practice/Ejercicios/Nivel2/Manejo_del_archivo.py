import pandas as pd

# Leer el archivo
df = pd.read_csv("Practice/Nivel2/Datos.csv")
# print(df)

print("------------------------------------")
#ordenar los nombres del dataframe de forma ascendente
df_ordenado_ascendente=df.sort_values("nombre")

#ordernando de forma descendente
df_ordenado_descendentemente=df.sort_values("edad", ascending=False)


#obteneniendo estadisticas
df_estadisticas=df.describe()
# print(df_estadisticas)

#los dos puntos en el primer parametro significa que se quiere acceder a todas las filas
df_apellidos = df.iloc[:,1]
# print(df_apellidos)