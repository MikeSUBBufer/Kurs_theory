import math
import numpy as np
import matplotlib.pyplot as plt
from CLSS_streamline import StrLine
from CLSS_MainCircle import MainCircle
a=int(input('Hello please enter selected time: '))
Grafik = StrLine(a)
Grafik.graf()
circle = MainCircle(radius=3, num_points=100)  # Создаём окружность с радиусом 3
points = circle.get_coordinates()
print("Coordinates of points:")
print(points)
circle.plot_circle()  # Строим график окружности