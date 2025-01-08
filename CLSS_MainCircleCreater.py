import numpy as np
import matplotlib.pyplot as plt

class MainCircleCreater:
    def __init__(self, radius=3, num_points=100):
        self.radius = radius
        self.num_points = num_points
        self.coordinates = self.generate_circle()

    def generate_circle(self):
        #Генерирует массив координат точек окружности с отрицательными x и y.
        angles = np.linspace(0, 2 * np.pi, self.num_points, endpoint=False)  # Углы равномерно распределены
        x = self.radius * np.cos(angles)  # Координаты x
        y = self.radius * np.sin(angles)  # Координаты y
        return np.array([(-xi, -yi) for xi, yi in zip(x, y)])

    def get_coordinates(self):
        #Возвращает массив с координатами точек.
        return self.coordinates

    def plot_circle(self):
        #Строит график окружности на основе сгенерированных точек.
        x_coords, y_coords = zip(*self.coordinates)  # Разделяем координаты x и y
        plt.figure(figsize=(6, 6))
        plt.plot(x_coords, y_coords, marker='o', linestyle=' ', label='Circle')
        plt.axhline(0, color='gray', linewidth=0.5)
        plt.axvline(0, color='gray', linewidth=0.5)
        plt.title("Circle with Radius 3")
        plt.xlabel("X-axis")
        plt.ylabel("Y-axis")
        plt.legend()
        plt.grid(True)
        plt.axis('equal')
        plt.show()



