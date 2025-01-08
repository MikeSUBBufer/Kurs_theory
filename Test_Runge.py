import numpy as np
class RungeKutta:
    def __init__(self, x0, t_range):
        self.x0 = x0
        self.t_range = t_range

        # Коэффициенты таблицы Бутчера (для метода с 4 стадиями)
        self.a = np.array([
            [0, 0, 0, 0],
            [0.5, 0, 0, 0],
            [0, 0.5, 0, 0],
            [0, 0, 1, 0]
        ])
        self.b = np.array([1/6, 2/6, 2/6, 1/6])
        self.c = np.array([0, 0.5, 0.5, 1])

    def f(self, t, x):
        """
        Правая часть дифференциального уравнения dx/dt = -e^t * x.

        :param t: Текущее время.
        :param x: Текущее значение x.
        :return: Значение производной dx/dt.
        """
        return -np.exp(t) * x

    def solve(self, h):
        """
        Решение задачи методом Рунге-Кутты.

        :param h: Шаг интегрирования.
        :return: Кортеж (t_values, x_values), содержащий массивы времени и решений.
        """
        t_start, t_end = self.t_range
        t_values = np.arange(t_start, t_end + h, h)
        x_values = np.zeros_like(t_values)
        # Установка начальных условий
        x_values[0] = self.x0

        for i in range(1, len(t_values)):
            t = t_values[i - 1]
            x = x_values[i - 1]

            # Вычисление стадий
            k = np.zeros(len(self.c))
            for j in range(len(self.c)):
                t_stage = t + self.c[j] * h
                x_stage = x + h * np.dot(self.a[j, :j], k[:j])
                k[j] = self.f(t_stage, x_stage)

            # Вычисление следующего значения x
            x_values[i] = x + h * np.dot(self.b, k)

        return t_values, x_values
