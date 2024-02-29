import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

fichero = "avengers.csv"
df = pd.read_csv(fichero,encoding="ISO-8859-1",usecols=["Year"])
#df.info()
#df.describe()
#df.hist()
df["Year"] = df[df["Year"] >= 1960]
max = int(df["Year"].max())
min = int(df["Year"].min())
bins = range(min,max,5)
print(bins)
fig,ax=plt.subplots()
ax.hist(df["Year"],bins=bins,rwidth=0.95,zorder=2,alpha=0.9)
ax.set_xticks(bins)
ax.yaxis.grid()

plt.show()