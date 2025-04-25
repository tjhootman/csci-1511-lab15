import matplotlib.pyplot as plt

# create a list of numbers for the x-axis
x_values = list(range(1, 5001))
# create empty list to store cubic values
y_values = []

# calculate the cube for each number in x_values and store it in y_values
for num in x_values:
    num **= 3
    y_values.append(num)

# apply plot style
plt.style.use('dark_background')

# plot the line
fig, ax = plt.subplots(figsize=(10, 8))
ax.scatter(x_values,y_values, c=y_values, cmap=plt.cm.plasma, s=10)

# add the title and axes labels
plt.title('First 5000 Cubic Numbers', fontsize=16)
plt.xlabel('Number', fontsize=12)
plt.ylabel('Cube', fontsize=12)
plt.tick_params(axis='both', labelsize=10)

# show the plot
plt.show()
