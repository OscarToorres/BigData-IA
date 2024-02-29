import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.dates import date2num

filename = "global-temperatures.csv"

df = pd.read_csv(filename,
                 parse_dates=["dt"],
                 usecols = ["dt", "LandAverageTemperature"])
df.head()
df.info()

df = df.dropna()
df.info()

df.head()

fig,ax = plt.subplots(figsize=(15,4))
x = df.dt
y = df.LandAverageTemperature

ax.plot(x,y,linestyle="None",marker = ".")

x = date2num(x)
z = np.polyfit(x,y,2)
p = np.poly1d(z)
ax.plot(x,p(x),linewidth=5)

plt.show()