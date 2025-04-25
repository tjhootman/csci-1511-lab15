import matplotlib.pyplot as plt

x_values = list(range(1, 5001))
y_values = []

for num in x_values:
    num **= 3
    y_values.append(num)

fig, ax = plt.subplots()
ax.scatter(x_values,y_values, c=y_values, cmap=plt.cm.cool, s=10)

plt.show()
