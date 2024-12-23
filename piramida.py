import pandas as pd
import plotly.graph_objects as go
file_path = "pira.xlsx"
data = pd.read_excel(file_path, sheet_name=0)
ages = list(range(0, 86)) + ["85+"]
men = data.iloc[9:96, 33].values * -1
women = data.iloc[9:96, 50].values
fig = go.Figure()
fig.add_trace(go.Bar(
    y=ages,
    x=men,
    name='Мужчины',
    orientation='h',
    marker=dict(color='blue')
))
fig.add_trace(go.Bar(
    y=ages,
    x=women,
    name='Женщины',
    orientation='h',
    marker=dict(color='pink')
))
fig.update_layout(
    title="Пирамида населения Казахстана по возрасту и полу",
    barmode='relative',
    xaxis=dict(title="Численность населения", tickvals=[-1000, -500, 0, 500, 1000]),
    yaxis=dict(title="Возраст"),
    template="plotly_white"
)
fig.show()
