# Define a function with signature pearson_r(x, y).
# Use np.corrcoef() to compute the correlation matrix of x and y (pass them to np.corrcoef() in that order).
# The function returns entry [0,1] of the correlation matrix.
# Compute the Pearson correlation between the data in the arrays versicolor_petal_length and versicolor_petal_width. Assign the result to r.
# Print the result.

def pearson_r(x, y):
    """Compute Pearson correlation coefficient between two arrays."""
# Compute correlation matrix: corr_mat
corr_mat=np.corrcoef(x,y)
# Return entry [0,1]
return corr_mat[0,1]
# Compute Pearson correlation coefficient for I. versicolor: r
r=pearson_r(versicolor_petal_length,versicolor_petal_width)
# Print the result
print(r)
