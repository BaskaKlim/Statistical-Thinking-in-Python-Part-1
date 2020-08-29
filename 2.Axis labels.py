# Instructions

# Label the axes. Don't forget that you should always include units in your axis labels. Your y-axis label is just 'count'. 
# Your x-axis label is 'petal length (cm)'. The units are essential!
# Display the plot constructed in the above steps using plt.show().

# Plot histogram of versicolor petal lengths
_ = plt.hist(versicolor_petal_length)

# Label axes
_ = plt.xlabel('petal length (cm)')
_ = plt.ylabel('count') 


# Show histogram
plt.show()
