import plotly.graph_objs as go
from CLSS_RungeKutta import RungeKutta
from CLSS_MatCircleDeformed import NewMatCircle
class DeformedCircle(RungeKutta):
    def __init__(self, num_points, lifetime, h):
        super().__init__(num_points, lifetime, h)
        self.result_x = self.result_x.T
        self.result_y = self.result_y.T
        self.new()
    def new(self):
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=self.result_x[0], y=self.result_y[0], mode='lines+markers', name='Искажение круга'))
        frames = []
        for i in range(len(self.result_x)):
            frames.append(go.Frame(data=[go.Scatter(x=self.result_x[i], y=self.result_y[i])]))
        fig.frames = frames
        fig.update_layout(
            updatemenus=[dict(type="buttons",
                              showactive=False,
                              buttons=[
                                  dict(label="Play",
                                       method="animate",
                                       args=[None, dict(frame=dict(duration=50, redraw=True), fromcurrent=True)]),
                                  dict(label="Pause",
                                       method="animate",
                                       args=[[None], dict(frame=dict(duration=0, redraw=False), mode="immediate")])
                              ])],
            title="Анимация искажения круга",
            xaxis=dict(range=[0, 19], title="X"),
            yaxis=dict(range=[-14, 0], title="Y"),
            showlegend=False
        )
        fig.show()
        C=NewMatCircle()
        C.__class__.x = self.result_x
        C.__class__.y = self.result_y
        C.__class__.color = self.color
if __name__ == '__main__':
    test=DeformedCircle(100, 0.5, 0.01)
    Port=NewMatCircle()
    print(Port.x)
