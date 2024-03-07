import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("euro-dollar-clean.csv")

#
df_r = df.groupby(["year", "month"])["dollar"].mean().unstack()

meses = ['ENE','FEB','MAR', 'ABR','MAY','JUN','JUL','AGO','SEP','OCT','NOV','DEC']

df_r.columns = meses

fig, ax = plt.subplots()

im = ax.imshow(df_r, cmap="Blues")
cbar = fig.colorbar(im, ax=ax, extend="max").outline.set_visible(False)

x = df_r.columns
y = df_r.index



for i in range(len(y)):
  for j in range(len(x)):
    valor = df_r.iloc[i,j].round(2)
    if (valor >= 1.25):
        ax.text(j, i, valor, ha="center", fontsize="xx-small", color="White")
    else:
        ax.text(j, i, valor, ha="center", fontsize="xx-small")


ax.set_xticks(range(len(x)))
ax.set_xticklabels(x, rotation=90)

ax.set_yticks(range(len(y)))
ax.set_yticklabels(y)

ax.invert_yaxis()
plt.show()
