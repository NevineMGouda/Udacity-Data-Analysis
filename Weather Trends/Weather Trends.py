# Importing the libraries needed for the project
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

# Loading the previously created csv file using Pandas' method read_csv and load the data into Panda's DataFrames
data_frame = pd.read_csv("results.csv")
# Pand's rolling method provides rolling window calculations which is how we calculate the moving average
# Where the window is equal to the number of years we want to smooth out and calculate their average
# The window here is set to 7
rolled_df = data_frame.rolling(window=7,on="year").mean()
# Plotting the Global and Local line charts
plt.plot(data_frame['year'],rolled_df["global_temp"],label="Global")
plt.plot(data_frame['year'],rolled_df["cairo_temp"],label="Local: Cairo")
# Showing the legends for the 2 lines to be able to identify them
plt.legend()
plt.xticks(np.arange(min(data_frame['year']), max(data_frame['year'])+1, 7),rotation=90)
# Setting the plots' labels and titles
plt.xlabel("Years")
plt.ylabel("Average Temperature (Degree Celsius)")
plt.title("Python: 7-Years Moving Average Temperature")
# Printing out the plots
plt.show()
# Printing some statistics
print "Min. Global Temp", min(data_frame['global_temp'])
print "Max. Global Temp", max(data_frame['global_temp'])
print "Min. Cairo Temp", min(data_frame['cairo_temp'])
print "Max. Cairo Temp", max(data_frame['cairo_temp'])

