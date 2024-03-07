import sys
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dfl = pd.read_html("https://www.tiobe.com/tiobe-index/")
tabla = dfl[0]
#print(tabla["Language.1"])
#print(tabla.columns)
tabla["Lenguaje"] = tabla["Programming Language.1"]
tabla["Porcentaje"] = tabla["Ratings"]
tabla.drop("Programming Language.1",axis=1,inplace=True)
tabla.drop("Ratings",axis=1,inplace=True)

df2 = tabla[["Lenguaje", "Porcentaje"]]
#print(df2)

fig = plt.figure(figsize=(10,5))
ax = fig.add_subplot(1,1,1)
ax.bar(df2.index, df2["Porcentaje"])

#ax.set_xticks(df2["Lenguaje"])
#ax.set_xticklabels(df2.index, rotation=90)

plt.show()

#print(tabla)

