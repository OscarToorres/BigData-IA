import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

fichero = "pokemon.csv"
df = pd.read_csv(fichero,usecols=["Speed"])
#df.hist(column="Speed")

df2 = df.groupby(["Speed"]).size()
df2 = df2.reset_index()
df2 = df2.rename(columns={0:"Cantidad"})

plt.bar(df2["Speed"],df2["Cantidad"])
plt.show()
