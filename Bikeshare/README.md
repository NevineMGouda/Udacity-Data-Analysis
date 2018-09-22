# Explore US Bikeshare Data
The aim of this Python script is to explore data related to bike share systems and come with statistical analysis given a dataset. Where this is achieved by parsing the dataset into the code and depending on the users' raw input to chose the desired filters (from the interactive script provided) the required statistics are shown.

## Datasets
The datasets used for this script is obtained from Udacity. Where it consists of  bikeshare data for a specific time window.

The dataset consists of 3 files: chicago.csv, new_york_city.csv and washington.csv is provided by. All the three files contain the following columns: 
* Start Time
* End Time
* Trip Duration (in seconds)
* Start Station
* End Station
* User Type (Subscriber or Customer)
* Gender
* Birth Year
However the last two columns (Gender and Birth Year) are missing from the washington.csv file.

## Statistical Questions
The script answers the following questions about the bike share data:
* What is the most popular month for start time?
* What is the most popular day of weekday for start time?
* What is the most popular hour of day for start time?
* What is the total trip duration and average trip duration?
* What is the most popular start station and most popular end station?
* What is the most popular trip?
* What are the counts of each user type?
* What are the counts of gender?
* What are the earliest (i.e. oldest person), most recent (i.e. youngest person), and most popular birth years?

## Running the Script
The script can run using any interpreter. Such as Pycharm which can be downloaded from this [link](https://www.jetbrains.com/pycharm/download/). Or simply run it from the terminal using python bikeshare.py.

## References using to complete this project
* https://pandas.pydata.org/pandas-docs/stable/generated/pandas.read_csv.html
* https://pandas.pydata.org/pandas-docs/stable/generated/pandas.set_option.html
* https://pandas.pydata.org/pandas-docs/stable/generated/pandas.Series.dt.dayofweek.html
* https://pandas.pydata.org/pandas-docs/version/0.22/generated/pandas.core.groupby.GroupBy.count.html
* https://pandas.pydata.org/pandas-docs/stable/generated/pandas.Series.mode.html

