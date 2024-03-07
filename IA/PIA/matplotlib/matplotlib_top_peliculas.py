import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv("imdb_top_1000.csv", usecols=["Certificate", "Genre", "IMDB_Rating"])
df = df.dropna()
df.describe()
df.info()
df["Genero"] = df["Genre"].str.split(",", expand=True)[0]
df_r = df.groupby(["Certificate", "Genero"])["IMDB_Rating"].mean()
df_r = df_r.unstack()
df_r.index
calificaciones = ["U", "UA", "PG-13", "R", "A"]
generos = [ "Animation" , "Action" , "Adventure" , "Biography" , "Comedy" , "Crime" , "Drama" ]
df_r = df_r.loc[calificaciones, generos]
calificaciones_legibles = {"U" : "ALL" , "UA" : ">12" , "PG-13" : ">13" , "R" : ">17" , "A" : ">18" }
df3 = df_r.reset_index()
df3 = df3["Certificate"].replace(calificaciones_legibles)
df_r.index = df3

fig, ax = plt.subplots()

im = ax.imshow(df_r, cmap="Reds")
cbar = fig.colorbar(im, ax=ax, label="Ratings")

x = df_r.columns
y = df_r.index

for i in range(len(y)):
  for j in range(len(x)):
    valor = df_r.iloc[i,j]
    ax.text(j, i, f"{valor:.2f}", ha="center")

ax.set_xticks(range(len(x)))
ax.set_xticklabels(x, rotation=90)

ax.set_yticks(range(len(y)))
ax.set_yticklabels(y)

ax.invert_yaxis()

plt.show()