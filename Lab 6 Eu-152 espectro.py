import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import LogFormatter
from matplotlib.ticker import MultipleLocator

# Coeficientes de calibración (supongamos que ya los obtuviste)
a = 1.75    # pendiente (keV/canal)
b = -15      # intercepto (keV)

# Leer archivo del Europio-152
df = pd.read_csv("C:\\Users\\Diego\\Downloads\\Eu-152_15min_NaI-Tl_bicron900V.csv", delimiter=';')  # Ajusta separador si es necesario
df = df.dropna()

# Convertir canal a energía
df["Energía (keV)"] = df["Canal"] * a + b

# Graficar conteos vs energía
plt.figure(figsize=(10,6))
plt.plot(df["Energía (keV)"], df["Conteos"], color='green')
plt.yscale('log')
plt.gca().yaxis.set_major_formatter(LogFormatter())
plt.gca().xaxis.set_major_locator(MultipleLocator(100))
plt.xlabel("Energía (keV)")
plt.ylabel("Conteos")
plt.title("Espectro calibrado de Eu-152")
plt.grid(True)
plt.tight_layout()
plt.show()
