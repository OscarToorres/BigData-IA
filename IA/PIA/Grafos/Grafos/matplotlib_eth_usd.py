import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import datetime

filename = "ETH-USD.csv"
df = pd.read_csv(filename, parse_dates=["Date"], usecols=["Date","Open","Volume"], index_col="Date")
fecha_min = datetime.datetime(year=2017,month=1,day=1)
df = df.loc[df.index > fecha_min]

df["Volume"] = df["Volume"] / 10000000

df = df.rolling(20).mean()
df = df.dropna()

fig, ax = plt.subplots()
ax.plot(df.index, df["Open"], label="Valor Open",color="skyblue")
ax.plot(df.index, -df["Volume"], label="Volume (en 10 Mill)",color="pink")
plt.fill_between(df.index, df["Open"],alpha=0.5,color = "skyblue")
plt.fill_between(df.index, -df["Volume"],alpha=0.5,color = "pink")

ax.set_yticks([-4000, -2000, 0, 2000, 4000])
ax.set_yticklabels([4000, 2000, 0, 2000, 4000])
ax.set_xticklabels(df.index, rotation=90)

plt.show()

# print(df)