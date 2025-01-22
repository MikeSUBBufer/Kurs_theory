import numpy as np
import matplotlib.pyplot as plt
class StrLine:
    def __init__(self, time):
        self.time = time
        self.x, self.y = np.meshgrid(np.linspace(0, 5, 20), np.linspace(-5, 0, 20))
        self.v_x = self.x * (-np.exp(self.time))  # уравнения задающие поле скоростей в момент времени t
        self.v_y = self.y * np.exp(self.time)
    def graf(self):
        # Построение линий тока
        colormass = np.sqrt(self.v_y**2+self.v_x**2)
        plt.figure(figsize=(8, 6))
        plt.streamplot(self.x, self.y, self.v_x, self.v_y, color=colormass, density=3, linewidth=0.5)
        plt.xlabel("x")
        plt.ylabel("y")
        plt.grid()
        plt.show()
        plt.figure(figsize=(8, 6))
        plt.quiver(self.x, self.y, self.v_x, self.v_y, colormass, cmap="jet")
        plt.xlabel("x")
        plt.ylabel("y")
        plt.grid()
        plt.show()
if __name__ == "__main__":
    cl=StrLine(5)
    cl.graf()
