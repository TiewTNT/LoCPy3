import plotly.graph_objects as go
from numpy import *
from random import randint

fig = go.Figure()

x = linspace(-10, 10, 100)
y = eval(func := input())
temp = []

if not isinstance(x, ndarray):
    for i in range(2000):
        temp.append(y)

    y = temp


fig.add_trace(go.Scatter(x=x, y=y, marker={'color': f'rgba({randint(0, 255)}, {randint(0, 255)}, {randint(0, 255)}, 0.5)'}, name=func))
fig.add_trace(go.Scatter(x=[-11, 11], y=[0, 0], marker={'color': 'rgba(50, 50, 50, 0.5)'}, name='xline'))
fig.add_trace(go.Scatter(x=[0, 0], y=[-11, 11], marker={'color': 'rgba(50, 50, 50, 0.5)'}, name='yline'))
fig.update_layout(xaxis_range=[-10, 10], yaxis_range=[-10, 10], xaxis=dict(dtick=1), yaxis=dict(dtick=1), width=800, height=800)
lines_to_hide = ['xline', 'yline', 'func']
for line_name in lines_to_hide:
    fig.update_traces(selector=dict(name=line_name), showlegend=False)
fig.show()
