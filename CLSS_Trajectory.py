from CLSS_RungeKutta import RungeKutta
from matplotlib import pyplot as plt
class Trajectory(RungeKutta):
    def __init__(self, num_points,lifetime,h):
        super().__init__(num_points,lifetime,h)
        self.trajectory()
    def trajectory(self):
        plt.figure(figsize=(10,10))
        for i in range(len(self.result_x)):
            plt.plot(self.result_x[i],self.result_y[i],linewidth=0.7)
        plt.scatter(self.result_x.T[0],self.result_y.T[0], marker='o', c='b')
        plt.scatter(self.result_x.T[-1], self.result_y.T[-1], marker='o', c='b')
        plt.axis('equal')  # Устанавливает одинаковый масштаб для осей
        plt.title('Trajectory')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.show()
if __name__ == "__main__":
    c=Trajectory(100,0.5, 0.01)
