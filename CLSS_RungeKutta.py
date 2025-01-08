import numpy as np
from CLSS_MainCircleCreater import CirclePoints

class RungeKutta(CirclePoints):
    def __init__(self, num_points, lifetime):
        """
        Инициализация класса RungeKutta, наследующего CirclePoints.

        :param num_points: Количество точек на окружности.
        """
        super().__init__(num_points,lifetime)  # Временной отрезок для подстановки в метод Рунге-Кутты
        self.result_points = None  # Массив результатов для каждой точки

        # Коэффициенты таблицы Бутчера (для метода с 4 стадиями)
        self.a = np.array([
            [0, 0, 0, 0],
            [0.5, 0, 0, 0],
            [0, 0.5, 0, 0],
            [0, 0, 1, 0]
        ])
        self.b = np.array([1/6, 2/6, 2/6, 1/6])
        self.c = np.array([0, 0.5, 0.5, 1])

    def f(self, t, x, y):
        """
        Правая часть дифференциального уравнения dx/dt и dy/dt.

        :param t: Текущее время.
        :param x: Текущее значение x.
        :param y: Текущее значение y.
        :return: Значения производных dx/dt и dy/dt (набор).
        """
        dx_dt = -np.exp(t) * x
        dy_dt = -np.exp(t) * y
        return dx_dt, dy_dt

    def solve(self, h):
        """
        Решение задачи методом Рунге-Кутты для всех начальных координат (x, y).

        :param h: Шаг интегрирования.
        :return: Массив результатов (каждая строка содержит массивы x и y для одной начальной точки).
        """
        t_start, t_end = self.lifetime
        t_values = np.arange(t_start, t_end + h, h)

        results = []  # Для хранения решений для всех начальных точек

        for x0, y0 in zip(self.x_points, self.y_points):
            x_values = np.zeros_like(t_values)
            y_values = np.zeros_like(t_values)

            # Установка начальных условий для текущей точки
            x_values[0] = x0
            y_values[0] = y0

            for i in range(1, len(t_values)):
                t = t_values[i - 1]
                x = x_values[i - 1]
                y = y_values[i - 1]

                # Вычисление стадий
                kx = np.zeros(len(self.c))
                ky = np.zeros(len(self.c))
                for j in range(len(self.c)):
                    t_stage = t + self.c[j] * h
                    x_stage = x + h * np.dot(self.a[j, :j], kx[:j])
                    y_stage = y + h * np.dot(self.a[j, :j], ky[:j])
                    kx[j], ky[j] = self.f(t_stage, x_stage, y_stage)

                # Вычисление следующего значения x и y
                x_values[i] = x + h * np.dot(self.b, kx)
                y_values[i] = y + h * np.dot(self.b, ky)

            results.append((x_values, y_values))

        self.result_points = results
        return results

# Пример использования
if __name__ == "__main__":
    num_points = 100  # Количество точек (пользователь задаёт)
    lifetime = (0 , 2)
    rk = RungeKutta(num_points, lifetime)
    rk.generate_points()  # Генерация начальных точек окружности  # Установка временного интервала
    h = 0.1  # Шаг интегрирования

    results = rk.solve(h)  # Решение методом Рунге-Кутты

    # Вывод результатов
    for idx, (x_values, y_values) in enumerate(results):
        print(f"Начальная точка {idx + 1}:")
        for t, x, y in zip(np.arange(rk.lifetime[0], rk.lifetime[1] + h, h), x_values, y_values):
            print(f"t = {t:.2f}, x = {x:.4f}, y = {y:.4f}")
