# Statistical-Thinking-in-Python-Part-1

##  Plotting a histogram of iris data
For the exercises in this section, you will use a classic data set collected by botanist Edward Anderson and made famous by Ronald Fisher, one of the most prolific statisticians in history. Anderson carefully measured the anatomical properties of samples of three different species of iris, Iris setosa, Iris versicolor, and Iris virginica. The full data set is available as part of scikit-learn. Here, you will work with his measurements of petal length.

Plot a histogram of the petal lengths of his 50 samples of Iris versicolor using matplotlib/seaborn's default settings. Recall that to specify the default seaborn style, you can use **sns.set()**, where sns is the alias that seaborn is imported as.

The subset of the data set containing the Iris versicolor petal lengths in units of centimeters (cm) is stored in the NumPy array **versicolor_petal_length**.

In the video, Justin plotted the histograms by using the pandas library and indexing the DataFrame to extract the desired column. Here, however, you only need to use the provided NumPy array. Also, Justin assigned his plotting statements (except for plt.show()) to the dummy variable _. This is to prevent unnecessary output from being displayed. It is not required for your solutions to these exercises, however it is good practice to use it. Alternatively, if you are working in an interactive environment such as a Jupyter notebook, you could use a ; after your plotting statements to achieve the same effect. Justin prefers using _. Therefore, you will see it used in the solution code.

**Instructions**
1. Import matplotlib.pyplot and seaborn as their usual aliases (plt and sns).
2. Use seaborn to set the plotting defaults.
3. Plot a histogram of the Iris versicolor petal lengths using plt.hist() and the provided NumPy array versicolor_petal_length.
4. Show the histogram using plt.show().

##  Axis labels!
In the last exercise, you made a nice histogram of petal lengths of Iris versicolor, but you didn't label the axes! That's ok; it's not your fault since we didn't ask you to. Now, add axis labels to the plot using **plt.xlabel()** and **plt.ylabel()**. Don't forget to add units and assign both statements to_. The packages **matplotlib.pyplot** and seaborn are already imported with their standard aliases. This will be the case in what follows, unless specified otherwise.

**Instructions**
1. Label the axes. Don't forget that you should always include units in your axis labels. Your y-axis label is just 'count'. Your x-axis label is 'petal length (cm)'. The units are essential!
2. Display the plot constructed in the above steps using plt.show().

## Adjusting the number of bins in a histogram
The histogram you just made had ten bins. This is the default of **matplotlib**. The "square root rule" is a commonly-used rule of thumb for choosing number of bins: choose the number of bins to be the square root of the number of samples. Plot the histogram of Iris versicolor petal lengths again, this time using the square root rule for the number of bins. You specify the number of bins using the bins keyword argument of **plt.hist()**.

The plotting utilities are already imported and the seaborn defaults already set. The variable you defined in the last exercise, **versicolor_petal_length**, is already in your namespace.

**Instructions**

1. Import numpy as np. This gives access to the square root function, np.sqrt().
2. Determine how many data points you have using len().
3. Compute the number of bins using the square root rule.
4. Convert the number of bins to an integer using the built in int() function.
5. Generate the histogram and make sure to use the bins keyword argument.
6. Hit 'Submit Answer' to plot the figure and see the fruit of your labors!

## Bee swarm plot
Make a bee swarm plot of the iris petal lengths. Your x-axis should contain each of the three species, and the y-axis the petal lengths. A data frame containing the data is in your namespace as df.

For your reference, the code Justin used to create the bee swarm plot in the video is provided below:
    *_ = sns.swarmplot(x='state', y='dem_share', data=df_swing)*
    *_ = plt.xlabel('state')*
    *_ = plt.ylabel('percent of vote for Obama')*
    *plt.show()*
 
In the IPython Shell, you can use sns.swarmplot? or help(sns.swarmplot) for more details on how to make bee swarm plots using seaborn.

**Instructions**

1. In the IPython Shell, inspect the DataFrame df using df.head(). This will let you identify which column names you need to pass as the x and y keyword arguments in your call to sns.swarmplot().
2. Use sns.swarmplot() to make a bee swarm plot from the DataFrame containing the Fisher iris data set, df. The x-axis should contain each of the three species, and the y-axis should contain the petal lengths.
3. Label the axes.
4. Show your plot.

## Computing the ECDF
In this exercise, you will write a function that takes as input a 1D array of data and then returns the x and y values of the ECDF. You will use this function over and over again throughout this course and its sequel. ECDFs are among the most important plots in statistical analysis. You can write your own function, foo(x,y) according to the following skeleton:
def foo(a,b):
   *"""State what function does here"""
    # Computation performed here
    return x, y*
 
The function foo() above takes two arguments a and b and returns two values x and y. The function header **def foo(a,b):** contains the function signature foo(a,b), which consists of the function name, along with its parameters.

**Instructions**

1. Define a function with the signature ecdf(data). Within the function definition,
Compute the number of data points, n, using the len() function.
2. The x-values are the sorted data. Use the np.sort() function to perform the sorting.
3. The y data of the ECDF go from 1/n to 1 in equally spaced increments. You can construct this using np.arange(). Remember, however, that the end value in np.arange() is not inclusive. Therefore, np.arange() will need to go from 1 to n+1. Be sure to divide this by n.
4. The function returns the values x and y.

## Plotting the ECDF
You will now use your **ecdf()** function to compute the ECDF for the petal lengths of Anderson's Iris versicolor flowers. You will then plot the ECDF. Recall that your ecdf() function returns two arrays so you will need to unpack them. An example of such unpacking is **x, y = foo(data)**, for some function foo().

**IInstructions**

1. Use ecdf() to compute the ECDF of versicolor_petal_length. Unpack the output into x_vers and y_vers.
2. Plot the ECDF as dots. Remember to include marker = '.' and linestyle = 'none' in addition to x_vers and y_vers as arguments inside plt.plot().
3. Label the axes. You can label the y-axis 'ECDF'.
4. Show your plot.

## Comparison of ECDFs
ECDFs also allow you to compare two or more distributions (though plots get cluttered if you have too many). Here, you will plot ECDFs for the petal lengths of all three iris species. You already wrote a function to generate ECDFs so you can put it to good use!

To overlay all three ECDFs on the same plot, you can use plt.plot() three times, once for each ECDF. Remember to include **marker='.'** and **linestyle='none'** as arguments inside **plt.plot()**.

**Instructions**

1. Compute ECDFs for each of the three species using your ecdf() function. The variables setosa_petal_length, versicolor_petal_length, and virginica_petal_length are all in your namespace. Unpack the ECDFs into x_set, y_set, x_vers, y_vers and x_virg, y_virg, respectively.
2. Plot all three ECDFs on the same plot as dots. To do this, you will need three plt.plot() commands. Assign the result of each to _.
3. A legend and axis labels have been added for you, so hit 'Submit Answer' to see all the ECDFs!

## Computing means
The mean of all measurements gives an indication of the typical magnitude of a measurement. It is computed using **np.mean().**

**Instructions**

1. Compute the mean petal length of Iris versicolor from Anderson's classic data set. The variable versicolor_petal_length is provided in your namespace. Assign the mean to mean_length_vers.
2. Hit submit to print the result.


##  Computing percentiles
In this exercise, you will compute the percentiles of petal length of Iris versicolor.

**Instructions**

1. Create percentiles, a NumPy array of percentiles you want to compute. These are the 2.5th, 25th, 50th, 75th, and 97.5th. You can do so by creating a list containing these ints/floats and convert the list to a NumPy array using np.array(). For example, np.array([30, 50]) would create an array consisting of the 30th and 50th percentiles.
2. Use np.percentile() to compute the percentiles of the petal lengths from the Iris versicolor samples. The variable versicolor_petal_length is in your namespace.
3. Print the percentiles.
