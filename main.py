from CLSS_streamline import StrLine
from CLSS_DeformedCircle import DeformedCircle
from CLSS_Trajectory import Trajectory
lifetime=float(input('Hello please enter selected lifetime of the body: '))
num_points=int(input('Please enter number(int) of points for body: '))
h=float(input('Please enter the step for Runge-Kutta: '))
Grafik = StrLine(lifetime)
Grafik.graf()
DefCir=DeformedCircle(num_points,lifetime,h)
Trajectory=Trajectory(num_points,lifetime,h)

