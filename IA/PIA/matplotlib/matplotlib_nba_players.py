import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


fichero = "all_seasons.csv"
df = pd.read_csv(fichero,usecols=["pts", "reb", "ast"])
#print(df)
df.head()
fig,ax = plt.subplots(figsize=(8,6))
x = df["pts"]
y = df["reb"]
dimension3 = df["ast"]
p = ax.scatter(x,y,c = dimension3,cmap="RdBu_r", s=10, alpha=0.5, vmin = dimension3.min(),vmax=dimension3.max())
cb = fig.colorbar(p, ax=ax, label="Asistencias")
ax.set_xlabel("Puntos")
ax.set_ylabel("Rebotes")
plt.show()