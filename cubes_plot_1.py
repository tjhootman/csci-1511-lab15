import matplotlib.pyplot as plt

x_values = list(range(1, 6))
y_values = []

for num in x_values:
    num **= 3
    y_values.append(num)

fig, ax = plt.subplots()
ax.plot(x_values,y_values,linewidth=2)

plt.show()
