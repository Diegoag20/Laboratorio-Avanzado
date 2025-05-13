import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Cargar datos
df = pd.read_csv("C:\\Users\\Diego\\Downloads\\Cs-137_15min_NaI-Tl_bicron_900V.csv", delimiter=';')  
df.dropna(inplace=True)

# Calibración: usa tus valores reales
a = 1.75    # pendiente (keV/canal)
b = -15     # intercepto (keV)
df["Energía (keV)"] = df["Canal"] * a + b

# Filtrar los datos en el rango de energía de interés
energia_min = 550
energia_max = 750
df_filtrado = df[(df["Energía (keV)"] >= energia_min) & (df["Energía (keV)"] <= energia_max)]

# Encontrar el máximo en este rango
max_conteos = df_filtrado["Conteos"].max()
max_index = df_filtrado["Conteos"].idxmax()

# Calcular la mitad del máximo
mitad_max = max_conteos / 2

# Buscar los puntos donde los conteos alcanzan la mitad del máximo
# Encuentra el primer punto donde los conteos son mayores o iguales a la mitad del máximo
i1 = df_filtrado[df_filtrado["Conteos"] >= mitad_max].iloc[0]["Energía (keV)"]
i2 = df_filtrado[df_filtrado["Conteos"] >= mitad_max].iloc[-1]["Energía (keV)"]

# Calcular el FWHM
fwhm = i2 - i1
print(f"FWHM: {fwhm:.2f} keV")

# Graficar
plt.figure(figsize=(10, 6))
plt.plot(df["Energía (keV)"], df["Conteos"], label="Espectro Cs-137")
plt.axvline(x=i1, color='red', linestyle='--', label=f"Mitad máxima (i1): {i1:.1f} keV")
plt.axvline(x=i2, color='red', linestyle='--', label=f"Mitad máxima (i2): {i2:.1f} keV")
plt.hlines(mitad_max, i1, i2, color='green', label=f'FWHM: {fwhm:.1f} keV')
plt.xlabel("Energía (keV)")
plt.ylabel("Conteos")
plt.title("FWHM del pico principal (entre 550 y 750 keV)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
