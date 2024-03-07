import sys
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

try:
  import google.colab
  IN_COLAB = True
except:
  IN_COLAB = False

if IN_COLAB:
    # montar el drive, que es donde tenemos el dataset
    from google.colab import drive
    drive.mount("/content/drive")
    data_dir = "/content/drive/MyDrive/2023/Publica/Alumnos/"
    sys.path.append(data_dir)
else:
    import os
    data_dir = os.path.dirname(__file__) + "/"


filename = data_dir + "Medals.xlsx"
df = pd.read_excel(filename)
#print(df)
#print(df.describe())
#print(df.info())
df["Pais"] = df["Team/NOC"]
df.drop(["Team/NOC"], axis=1, inplace=True)

df = df.set_index("Pais")

df.sort_values("Rank")
df = df[:10]
df

fig = plt.figure(figsize=(8,5))
ax = fig.add_subplot(1,1,1)

ancho = 0.3
ax.bar(df["Rank"]-ancho, df["Gold"], ancho, color="gold", label="Oro")
ax.bar(df["Rank"], df["Silver"], ancho, color="silver", label="Plata")
ax.bar(df["Rank"]+ancho, df["Bronze"], ancho, color="orange", label="Bronce")

ax.set_xticks(df["Rank"])
ax.set_xticklabels(df.index, rotation=90)
plt.show()