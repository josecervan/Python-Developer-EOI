import pygal

lines = list()

with open("density.csv") as densities:
    for line in densities:
        lines.append(line.split(','))
    lines.pop(0)

lines.append([46, ' Spain', '93\n'])
lines.append([98, ' Greece', '81\n'])

# --
lines.sort(key=lambda x: x[1])

line_chart = pygal.HorizontalBar()
line_chart.title = 'By country'

for country in lines:
    line_chart.add(country[1], int(country[2]))

line_chart.render_to_file('density_by_country.svg')

# --
lines.sort(key=lambda x: int(x[2]), reverse=True)

line_chart = pygal.HorizontalBar()
line_chart.title = 'Densidad de población'

for country in lines:
    line_chart.add(country[1], int(country[2]))

line_chart.render_to_file('density_by_density.svg')
