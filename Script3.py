
import matplotlib.pyplot as plt
import numpy as np

# Crear datos para la función logarítmica
x = np.linspace(0.1, 10, 400)  # Definir un rango de valores de x (evitando x=0 para evitar log(0))
y = np.log(x)  # Calcular los valores correspondientes de y

# Graficar la función
plt.plot(x, y, label='y = log(x)')

# Personalizar el gráfico
plt.title('Gráfico de la función logarítmica')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.legend()  # Mostrar la leyenda
plt.show()
