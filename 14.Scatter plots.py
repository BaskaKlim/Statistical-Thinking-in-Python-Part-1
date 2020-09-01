# Use plt.plot() with the appropriate keyword arguments to make a scatter plot of versicolor petal length (x-axis) versus petal width (y-axis). The variables versicolor_petal_length and versicolor_petal_width are already in your namespace. Do not forget to use the marker='.' and linestyle='none' keyword arguments.
# Label the axes.
# Display the plot.

# Make a scatter plot

plt.plot(versicolor_petal_length, versicolor_petal_width, marker='.', linestyle='none')

# Label the axes
_ = plt.xlabel("total votes (thousands)")
_ = plt.ylabel("percent of vote for Obama")

# Show the result
plt.show()
