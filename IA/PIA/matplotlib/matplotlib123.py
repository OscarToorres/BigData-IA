import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,7,50) # Valores entre 0 y 7 y haz 50 divisiones
y = np.sin(x)
fig, ax = plt.subplots() 
ax.plot(x,y,label="Esta es sin",linewidth=3,color="red")
y2 = np.cos(x)
ax.plot(x,y2,label="Esta es cos",marker="o")
ax.set_title("Una prueba")
ax.legend() #Mostrar la leyenda
ax.set_xlim(0,2)
ax.set_ylim(0.5,1)
ax.annotate("Aqui se cruzan",xy=(0.76,0.71),xytext=(1.25,0.8),
								arrowprops=dict(facecolor="black",shrink=0.01))
ax.plot([0,0.78],[0.71,0.71],color="gray",linestyle="--")
