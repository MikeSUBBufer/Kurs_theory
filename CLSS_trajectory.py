import numpy as np
import matplotlib.pyplot as plt
from CLSS_RungeKutta import RungeKutta
class Trajectory:
    def __init__(self, x_coords, y_coords):
        super().__init__(num_points, lifetime)
        self.x_coords = x_coords
        self.y_coords = y_coords

    def get_trajectory(self):
        trajectory = []
        for x, y in zip(self.x_coords, self.y_coords):
            trajectory.append((x, y))
        return trajectory

    def print_trajectory(self):
        for point in self.get_trajectory():
            print(f"Координата: {point}")

    def plot_trajectory(self):
        plt.plot(self.x_coords, self.y_coords, marker='o')
        plt.title("Траектория пути")
        plt.xlabel("X координаты")
        plt.ylabel("Y координаты")
        plt.grid()
        plt.show()

if __name__ == "__main__":
    num_points = 100
    lifetime = 2
    h = 0.1
    rk = RungeKutta(num_points, lifetime, h)
    x_coords = rk.result_x
    y_coords = rk.result_y
    tr = Trajectory(x_coords,y_coords)
    tr.plot_trajectory()