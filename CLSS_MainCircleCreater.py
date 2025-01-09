import numpy as np
from CLSS_MatCircle import MatCircle
class CirclePoints(MatCircle):
    def __init__(self, num_points, lifetime):
        super().__init__(lifetime)
        self.num_points = num_points
        #self.radius = 3  # Радиус окружности
        #self.lifetime = (0 , lifetime)
        self.x_points = None  # Массив координат x
        self.y_points = None  # Массив координат y

    def generate_points(self):
        # Углы точек для полной окружности
        angles = np.linspace(0, 2 * np.pi, self.num_points)
        # Вычисляем координаты x и y с центром в (4, -4)
        self.x_points = self.radius * np.cos(angles) + 4
        self.y_points = self.radius * np.sin(angles) - 4



