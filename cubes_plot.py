import matplotlib.pyplot as plt

x1 = list(range(1, 6))
y1 = []

for num in x1:
    num **= 3
    y1.append(num)

fig, ax = plt.subplots()
ax.plot(x1,y1,linewidth=2)

plt.show()