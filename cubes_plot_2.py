import matplotlib.pyplot as plt

class CubeCalculator:
    """Calculates the cubes of a sequence of numbers."""
    def calculate_cubes(self, n):
        """Generates a list of cubes for the first n natural numbers.

        Args:
            n (int): Number of natural numbers to cube.

        Returns:
            List[int]: A list containing the cubes of the first n natural numbers.
        """
        return [i**3 for i in range(1, n + 1)]
    
class ScatterPlotter:
    """Generates and displays a scatter plot."""
    def __init__(self, title, xlabel, ylabel, style='dark_background', figsize=(10,8)):
        """Initializes the ScatterPlotter with title, labels, style and figure size.

        Args:
            title (str): The title of the plot.
            xlabel (str): The label for the x-axis.
            ylabel (str): The label for the y-axis.
            style (str, optional): The matplotlib style to use. Defaults to 'dark_background'.
            figsize (tuple, optional): The size of the figure (width, height) in inches. Defaults to (10,8).
        """
        plt.style.use(style)
        self.fig, self.ax = plt.subplots(figsize=figsize)
        self.title = title
        self.xlabel = xlabel
        self.ylabel = ylabel
    
    def plot(self, x_values, y_values, color_values, cmap='plasma', s=10):
        """Creates and displays the scatter plot.

        Args:
            x_values (List[int]): A list of values for the x-axis.
            y_values (List[int]): A list of values for the y-axis.
            color_values (List[int]): A list of values to determine the color of each point.
            cmap (str, optional): The matplotlib colormap to use. Defaults to 'plasma'.
            s (int, optional): The size of the points in the scatter plot. Defaults to 10.
        """
        self.ax.scatter(x_values, y_values, c=color_values, cmap=cmap, s=s)
        plt.title(self.title, fontsize=16)
        plt.xlabel(self.xlabel, fontsize=12)
        plt.ylabel(self.ylabel, fontsize=12)
        plt.tick_params(axis='both', labelsize=10)
        plt.show()

if __name__ == '__main__':
    num_points = 5000
    # Calculate the cubic values
    calculator = CubeCalculator()
    y_values = calculator.calculate_cubes(num_points)
    x_values = list(range(1, num_points +1))
    # Create and display the scatter plot
    plotter = ScatterPlotter('First 5000 Cubic Numbers', 'Number', 'Cube')
    plotter.plot(x_values, y_values, y_values)


# ----- Orginal Code -----

# create a list of numbers for the x-axis
# x_values = list(range(1, 5001))
# # create empty list to store cubic values
# y_values = []

# calculate the cube for each number in x_values and store it in y_values
# for num in x_values:
#     num **= 3
#     y_values.append(num)

# apply plot style
# plt.style.use('dark_background')

# plot the line
# fig, ax = plt.subplots(figsize=(10, 8))
# ax.scatter(x_values,y_values, c=y_values, cmap=plt.cm.plasma, s=10)

# add the title and axes labels
# plt.title('First 5000 Cubic Numbers', fontsize=16)
# plt.xlabel('Number', fontsize=12)
# plt.ylabel('Cube', fontsize=12)
# plt.tick_params(axis='both', labelsize=10)

# show the plot
# plt.show()
