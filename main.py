from CLSS_MatCircle import MatCircle
from CLSS_streamline import StrLine
from CLSS_RungeKutta import RungeKutta
lifetime=float(input('Hello please enter selected lifetime of the body: '))
num_points=int(input('Please enter number(int) of points for body: '))
h=float(input('Please enter the step for Runge-Kutta: '))
Grafik = StrLine(lifetime)
Grafik.graf()
Runge=RungeKutta(num_points,lifetime,h)
print(Runge.result_x)
