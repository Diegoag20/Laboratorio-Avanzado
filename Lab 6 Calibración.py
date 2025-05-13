import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Valores que tú identificas manualmente
canales = np.array([75, 148, 207, 460, 563, 637, 811])  # Ejemplo
energias = np.array([122, 245, 344, 779, 964, 1112, 1408])  # Ejemplo (en keV)

# Ajuste lineal
slope, intercept, r_value, p_value, std_err = linregress(canales, energias)

x_vals = range(min(canales)-10, max(canales)+10)
y_vals = [slope * x + intercept for x in x_vals]

# Crear la figura
plt.figure(figsize=(8,6))
plt.scatter(canales, energias, color='red', label='Datos de calibración')
plt.plot(x_vals, y_vals, color='blue', label=f'Regresión lineal')

# Texto en la gráfica
plt.text(0.05, 0.9, f'E = {slope:.2f}·Canal {intercept:.2f}\n$R^2$ = {r_value**2:.4f}',
         transform=plt.gca().transAxes, fontsize=12, bbox=dict(facecolor='white', alpha=0.7))

# Etiquetas
plt.xlabel('Canal')
plt.ylabel('Energía (keV)')
plt.title('Calibración del detector con Eu-152')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
