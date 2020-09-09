import matplotlib.pyplot as plt

x_values = range(1, 10)
y_values = [x ** 2 for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, s=200)

# ax.set_title('Función cuadrática', fontsize=24)
# ax.set_xlabel('$x$')
# ax.set_ylabel('$x^2$')

ax.tick_params(axis='both', which='major', labelsize=14)
# ax.grid()

plt.show()