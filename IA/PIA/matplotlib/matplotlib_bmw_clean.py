import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

fichero = "bmw-clean.csv"
df = pd.read_csv(fichero,usecols=["year","price","mpg"])
df.head()
fig,ax = plt.subplots(figsize=(8,6))
y = df["price"]
x = df["mpg"]
dimension3 = df["year"]
p = ax.scatter(x,y,c = dimension3,cmap="plasma_r",s=10, alpha=0.5, vmin = dimension3.min(),vmax=dimension3.max())
cb = fig.colorbar(p, ax=ax, label="Años")
ax.set_xlabel("Precio")
ax.set_ylabel("mpg")
plt.show()

#print(df)