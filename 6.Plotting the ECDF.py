
# Use ecdf() to compute the ECDF of versicolor_petal_length. Unpack the output into x_vers and y_vers.
# Plot the ECDF as dots. Remember to include marker = '.' and linestyle = 'none' in addition to x_vers and y_vers as arguments inside plt.plot().
# Label the axes. You can label the y-axis 'ECDF'.
# Show your plot.

# Compute ECDF for versicolor data: x_vers, y_vers
x_vers,y_vers = ecdf(versicolor_petal_length)

# Generate plot
plt.plot(x_vers,y_vers,marker='.',linestyle='none')

# Label the axes
plt.ylabel('ECDF')
plt.xlabel('versicolor_petal_length')


# Display the plot
plt.show()
