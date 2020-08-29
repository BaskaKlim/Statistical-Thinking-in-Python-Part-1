# Import matplotlib.pyplot and seaborn as their usual aliases (plt and sns).
# Use seaborn to set the plotting defaults.
# Plot a histogram of the Iris versicolor petal lengths using plt.hist() and the provided NumPy array versicolor_petal_length.
# Show the histogram using plt.show().



# Import plotting modules
import matplotlib.pyplot as plt
import seaborn as sns

# Set default Seaborn style
sns.set()

# Plot histogram of versicolor petal lengths
_ = plt.hist(versicolor_petal_length)

# Show histogram
plt.show() 
