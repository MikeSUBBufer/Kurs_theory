import math
import numpy as np
import matplotlib.pyplot as plt

# Создание сетки координат
x, y = np.meshgrid(np.linspace(-100, 100, 1000), np.linspace(-100, 100, 1000))

# Время для построения линий тока
t = 2

# Поле скоростей в момент времени t
v_x = -x * math.exp(t)
v_y = y * math.exp(t)
mag=np.sqrt(v_y**2+v_x**2)
# Построение линий тока
plt.figure(figsize=(8, 6))
plt.streamplot(x, y, v_x, v_y, color=mag, density=3, linewidth=0.5)
plt.title(f"Линии тока в момент времени t = {t:.2f}")
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.show()
