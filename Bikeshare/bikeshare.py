import sys
import time
import numpy as np
import pandas as pd


# Filenames
chicago = 'chicago.csv'
new_york_city = 'new_york_city.csv'
washington = 'washington.csv'


def get_month_dic():
    """ Returns a dictionary of the months in their proper order and their index

    Args:
        none.
    Returns:
        (Dictionary) Dictionary with size of 12 consisting of the months of the year as the key
        and their index as the value
    """
    month_dic = {"january": 1, "february": 2, "march": 3, "april": 4, "may": 5, "june": 6,
                 "july": 7, "august": 8, "september": 9, "october": 10, "november": 11, "december": 12}
    return month_dic


def get_month_list():
    """ Returns a list of the months in their proper order

    Args:
        none.
    Returns:
        (List) List of strings with size of 12 consisting of the months of the year
    """
    month_list = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october",
                  "november", "december"]
    return month_list


def get_week_days():
    """ Returns a list of the weekdays in their proper order

    Args:
        none.
    Returns:
        (List) List of strings with size of 7 consisting of the days in a week
    """
    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    return weekdays


def get_city():
    """Asks the user for a city and returns the filename for that city's bike share data.

    Args:
        none.
    Returns:
        (str) Filename for a city's bikeshare data.
    """
    while True:
        city = input('\nHello! Let\'s explore some US bikeshare data!\n'
                     'Would you like to see data for Chicago, New York, or Washington?\n').lower().strip()
        if city == "chicago":
            return chicago
        if city == "new york" or city == "newyork":
            return new_york_city
        if city == "washington":
            return washington
        print("Wrong input, Please Try Again.")


def get_time_period():
    """Asks the user for a time period and returns the specified filter.

    Args:
        none.
    Returns:
        (str) The Time period filter
    """
    while True:
        time_period = input('\nWould you like to filter the data by month, day, or not at '
                            'all? Type "none" for no time filter.\n').lower().strip()
        if time_period in ['month', 'day', 'none']:
            return time_period
        print("Wrong input, Please Try Again.")


def get_month():
    """Asks the user for a month and returns the specified month.

    Args:
        none.
    Returns:
        (Integer) The month's index number
    """
    month_dic = get_month_dic()
    while True:
        month = input('\nWhich month? January, February, March, April, May, or June?\n').lower().strip()
        if month in month_dic:
            return month_dic[month]
        print("Wrong input, Please Try Again.")


def get_day(month):
    """Asks the user for a day and returns the specified day.

    Args:
        none.
    Returns:
        (Integer) Filter by the day in the month
    """
    while True:
        try:
            day = eval(input('\nWhich day? Please type your response as an integer.\n'))
        except Exception as e:
            print("ERROR! Error Message:", str(e))
            print("Wrong input, Please Try Again.")
            continue
        if 1 <= day <= 31:
            if month in [4, 6, 9, 11]:
                if day <= 30:
                    return day
                print("The Month {}".format(month), "has only 30 days. Please enter a valid day")
            if month == 2:
                if day <= 28:
                    return day
                print("The Month {}".format(month), "has only 28 days. Please enter a valid day")
            else:
                return day
        else:
            print("Please enter a valid day of the month, a value between 1 and 31")


def popular_month(city_dataframe):
    """ Answers the question: What is the most popular month for start time?

    Args:
       The city BikeShare dataFrame containing the Start Time column/Series.
    Returns:
       none
    """
    try:
        months = get_month_list()
        index = city_dataframe['Start Time'].dt.dayofweek.mode()
        if not index.empty:
            index = int(index)
        else:
            print("The Start Time is empty.\n Skipping...")
            return

        most_pop_month = months[index - 1].capitalize()
        print('The most popular month for start time is {}.'.format(most_pop_month))

    except Exception as e:
        print("Something went wrong while calculating the popular month statistics in the "
              "popular_month(city_dataframe) function")
        print("ERROR! Error Type:", sys.exc_info()[0])
        print("ERROR! Error Message:", str(e))
        print("Skipping...")


def popular_day(city_dataframe):
    """ Answers the question: What is the most popular day of week (Monday, Tuesday, etc.) for start time?

    Args:
        The city BikeShare dataFrame containing the Start Time column/Series.
    Returns:
        none
    """
    try:
        days_of_week = get_week_days()
        index = city_dataframe['Start Time'].dt.dayofweek.mode()
        if not index.empty:
            index = int(index)
        else:
            print("The Start Time is empty.\n Skipping...")
            return

        most_pop_day = days_of_week[index]
        print('The most popular day of week for start time is {}.'.format(most_pop_day))

    except Exception as e:
        print("Something went wrong while calculating the popular weekday statistics in the "
              "popular_day(city_dataframe) function")
        print("ERROR! Error Type:", sys.exc_info()[0])
        # logging.error(traceback.format_exc())
        print("ERROR! Error Message:", str(e))
        print("Skipping...")


def popular_hour(city_dataframe):
    """ Answers the question: What is the most popular hour of day for start time?

    Args:
        The city BikeShare dataFrame containing the Start Time column/Series.
    Returns:
        none
    """
    try:
        popular_military_hour = city_dataframe['Start Time'].dt.hour.mode()

        if not popular_military_hour.empty:
            popular_military_hour = int(popular_military_hour)
        else:
            print("The Start Time is empty.\n Skipping...")
            return

        if popular_military_hour == 0:
            am_pm = 'AM'
            popular_12_hour = 12
        elif 1 <= popular_military_hour < 12:
            am_pm = 'AM'
            popular_12_hour = popular_military_hour
        elif popular_military_hour == 12:
            am_pm = 'PM'
            popular_12_hour = popular_military_hour
        else:
            am_pm = 'PM'
            popular_12_hour = popular_military_hour - 12

        print('The most popular hour of day for start time is {}{}.'.format(popular_12_hour, am_pm))
    except Exception as e:
        print("Something went wrong while calculating the popular hour statistics in the "
              "popular_hour(city_dataframe) function")
        print("ERROR! Error Type:", sys.exc_info()[0])
        print("ERROR! Error Message:", str(e))
        print("Skipping...")


def trip_duration(city_dataframe):
    """ Answers the question: What is the total trip duration and average trip duration?

    Args:
        The city BikeShare dataFrame containing the Start Time column/Series.
    Returns:
        none
    """
    try:
        total_duration = city_dataframe['Trip Duration'].sum()

        if np.isnan(total_duration):
            total_duration = 0.0

        average_duration = city_dataframe['Trip Duration'].mean()
        if np.isnan(average_duration):
            average_duration = 0.0

        print('The total trip duration is {} seconds. And the average trip duration is {} seconds.'.
              format(total_duration, average_duration))

        # print(a more readable total trip duration
        total_minute, total_second = divmod(total_duration, 60)
        total_hour, total_minute = divmod(total_minute, 60)
        if total_hour > 24:
            total_days, total_hour = divmod(total_hour, 24)
        else:
            total_days = 0.0

        print("Where the total trip duration can be approximated to {} days, {} hours, {} minutes and {}"
              " seconds.".format(total_days, total_hour, total_minute, total_second))

        # print(a more readable average trip duration
        average_minute, averagel_second = divmod(average_duration, 60)
        average_hour, average_minute = divmod(average_minute, 60)
        if average_hour > 24:
            average_days, average_hour = divmod(average_hour, 24)
        else:
            average_days = 0.0
        print("And the total trip duration can be approximated to {} days, {} hours, {} minutes and {}"
              " seconds.".format(average_days, average_hour, average_minute, averagel_second))

    except Exception as e:
        print("Something went wrong while calculating the trip duration statistics in the "
              "trip_duration(city_dataframe) function")
        print("ERROR! Error Type:", sys.exc_info()[0])
        print("ERROR! Error Message:", str(e))
        print("Skipping...")


def popular_stations(city_dataframe):
    """ Answers the question: What is the most popular start station and most popular end station?

    Args:
        The city BikeShare dataFrame containing the Start Station and End Station columns/Series.
    Returns:
        none
    """
    try:
        popular_start_station = city_dataframe['Start Station'].mode()
        popular_end_station = city_dataframe['End Station'].mode()
        if popular_start_station.empty:
            print("There isn't any Start Station found.\nSkipping...")
            return
        if popular_end_station.empty:
            print("There isn't any End Station found.\nSkipping...")
            return
        print('The most popular start station is {}.'.format(popular_start_station.to_string(index=False)))
        print('While the most popular end station is {}.'.format(popular_end_station.to_string(index=False)))

    except Exception as e:
        print("Something went wrong while calculating the popular stations statistics in the "
              "popular_stations(city_dataframe) function")
        print("ERROR! Error Type:", sys.exc_info()[0])
        print("ERROR! Error Message:", str(e))
        print("Skipping...")


def popular_trip(city_dataframe):
    """ Answers the question: What is the most popular trip?

    Args:
        The city BikeShare dataFrame containing the Start Station and End Station columns/Series.
    Returns:
        none
    """
    try:
        trip = city_dataframe['Start Station'].str.cat(city_dataframe['End Station'], sep=' TO ')
        most_popular_trip = trip.mode()
        if most_popular_trip.empty:
            print("There isn't any trips found.\nSkipping...")
            return
        print('The most popular trip is FROM {}.'.format(most_popular_trip.to_string(index=False)))

    except Exception as e:
        print("Something went wrong while calculating the popular trip statistics in the "
              "popular_trip(city_dataframe) function")
        print("ERROR! Error Type:", sys.exc_info()[0])
        print("ERROR! Error Message:", str(e))
        print("Skipping...")


def users(city_dataframe):
    """ Answers the question: What are the counts of each user type?

    Args:
        The city BikeShare dataFrame containing the User Type column/Series.
    Returns:
        none
    """

    try:
        users_types = city_dataframe.groupby("User Type")["User Type"].count()
        if len(users_types) == 0:
            print("The User Type column doesn't contain any types.\nSkipping...")
            return
        for index, row in users_types.iteritems():
            print('The user type: {}, has a total count of: {}.'.format(index, row))

    except Exception as e:
        print("Something went wrong while calculating the users type statistics in the "
              "users(city_dataframe) function")
        print("ERROR! Error Type:", sys.exc_info()[0])
        print("ERROR! Error Message:", str(e))
        print("Skipping...")


def gender(city_dataframe):
    """ Answers the question: What are the counts of gender?

    Args:
        The city BikeShare dataFrame containing the Gender column/Series.
    Returns:
        none
    """
    try:
        gender_types = city_dataframe.groupby("Gender")["Gender"].count()
        if len(gender_types) == 0:
            print("The Gender column doesn't contain any genders.\nSkipping...")
            return
        for index, row in gender_types.iteritems():
            print('The Gender: {}, has a total count of: {}.'.format(index, row))
    except Exception as e:
        print("Something went wrong while calculating the Gender statistics in the "
              "gender(city_dataframe) function")
        print("ERROR! Error Type:", sys.exc_info()[0])
        print("ERROR! Error Message:", str(e))
        print("Skipping...")


def birth_years(city_dataframe):
    """ Answers the question: What are the earliest (i.e. oldest user), most recent (i.e. youngest user),
    and most popular birth years?

    Args:
        The city BikeShare dataFrame containing the Birth Year column/Series.
    Returns:
        none
    """
    try:
        oldest = city_dataframe["Birth Year"].min()
        if not np.isnan(oldest):
            oldest = int(oldest)
            print('The oldest/earliest birth year: {}.'.format(oldest))
        else:
            print("The oldest/earliest birth year doesn't exist.\nSkipping...")

        youngest = city_dataframe["Birth Year"].max()
        if not np.isnan(youngest):
            youngest = int(youngest)
            print('The youngest/most recent birth year: {}.'.format(youngest))
        else:
            print("The youngest/most recent birth year doesn't exist.\nSkipping...")

        popular = city_dataframe["Birth Year"].mode()
        if not popular.empty:
            popular = int(popular)
            print('The most popular birth year: {}.'.format(popular))
        else:
            print("The most popular birth year doesn't exist.\nSkipping...")

    except Exception as e:
        print("Something went wrong while calculating the birth year statistics in the "
              "birth_years(city_dataframe) function")
        print("ERROR! Error Type:", sys.exc_info()[0])
        print("ERROR! Error Message:", str(e))
        print("Skipping...")


def display_data(city_dataframe):
    """Displays five lines of data if the user specifies that they would like to.
    After displaying five lines, ask the user if they would like to see five more,
    continuing asking until they say stop.

    Args:
        The city BikeShare dataFrame containing the Birth Year column/Series.
    Returns:
        none
    """
    start_row = 0
    end_row = 5
    while True:
        display = input('\nWould you like to view individual trip data? '
                        'Type \'yes\' or \'no\'.\n').lower().strip()
        if display == "no":
            return
        if display == "yes":
            print((city_dataframe[city_dataframe.columns].iloc[start_row:end_row]))
            start_row += 5
            end_row += 5
        else:
            print("Wrong input, Please Try Again.")


def statistics():
    """Calculates and prints out the descriptive statistics about a city and time period
    specified by the user via raw input.

    Args:
        none.
    Returns:
        none.
    """
    # Filter by city (Chicago, New York, Washington)

    city = get_city()
    # Tries to read the city data and parse the columns "Start Time" and "End Time" as date columns
    try:
        df = pd.read_csv(city, parse_dates=['Start Time', 'End Time'])
        pd.set_option("display.max_colwidth", -1)
    except Exception as e:
        print("ERROR! Error Type:", sys.exc_info()[0])
        print("ERROR! Error Message:", str(e))
        print("Something went wrong while reading the data file. Exiting...")
        return

    # Filter by time period (month, day, none)
    time_period = get_time_period()
    if time_period != "none":

        month = get_month()
        if time_period == "day":
            day = get_day(month)
            df_filtered = df[(df['Start Time'].dt.month == int(month)) & (df['Start Time'].dt.day == int(day))]
        else:
            df_filtered = df[df['Start Time'].dt.month == int(month)]
    else:
        df_filtered = df

    print('\nCalculating the first statistic...')
    # What is the most popular month for start time?
    if time_period == 'none':
        start_time = time.time()
        if "Start Time" in df_filtered:
            popular_month(df_filtered)
        else:
            print(" Start Time Column doesn't exist in the dataset. Skipping Popular Month statistics...")

        print("That took %s seconds." % (time.time() - start_time))
        print("\nCalculating the next statistic...")

    # What is the most popular day of week (Monday, Tuesday, etc.) for start time?
    if time_period == 'none' or time_period == 'month':
        start_time = time.time()
        if "Start Time" in df_filtered:
            popular_day(df_filtered)
        else:
            print(" Start Time Column doesn't exist in the dataset. Skipping Popular Day statistics...")

        print("That took %s seconds." % (time.time() - start_time))
        print("\nCalculating the next statistic...")

    start_time = time.time()

    # What is the most popular hour of day for start time?
    if "Start Time" in df_filtered:
        popular_hour(df_filtered)
    else:
        print(" Start Time Column doesn't exist in the dataset. Skipping Popular Hour statistics...")

    print("That took %s seconds." % (time.time() - start_time))
    print("\nCalculating the next statistic...")
    start_time = time.time()

    # What is the total trip duration and average trip duration?
    if "Trip Duration" in df_filtered:
        trip_duration(df_filtered)
    else:
        print("Trip Duration Column doesn't exist in the dataset. Skipping Trip Duration statistics...")

    print("That took %s seconds." % (time.time() - start_time))
    print("\nCalculating the next statistic...")
    start_time = time.time()

    # What is the most popular start station and most popular end station?
    if "Start Station" in df_filtered and "End Station" in df_filtered:
        popular_stations(df_filtered)
    else:
        print("Start Station and/or End Station Column(s) don't exist in the dataset. "
              "Skipping Popular Stations statistics...")

    print("That took %s seconds." % (time.time() - start_time))
    print("\nCalculating the next statistic...")
    start_time = time.time()

    # What is the most popular trip?
    if "Start Station" in df_filtered and "End Station" in df_filtered:
        popular_trip(df_filtered)
    else:
        print("Start Station and/or End Station Column(s) don't exist in the dataset. "
              "Skipping Popular Trips statistics...")

    print("That took %s seconds." % (time.time() - start_time))
    print("\nCalculating the next statistic...")
    start_time = time.time()

    # What are the counts of each user type?
    if "User Type" in df_filtered:
        users(df_filtered)
    else:
        print("User Type Column doesn't exist in the dataset. Skipping Users Type statistics...")

    print("That took %s seconds." % (time.time() - start_time))
    print("\nCalculating the next statistic...")
    start_time = time.time()

    # What are the counts of gender?
    if "Gender" in df_filtered:
        gender(df_filtered)
    else:
        print("Gender Column doesn't exist in the dataset. Skipping Gender statistics...")

    print("That took %s seconds." % (time.time() - start_time))
    print("\nCalculating the next statistic...")
    start_time = time.time()

    # What are the earliest (i.e. oldest user), most recent (i.e. youngest user), and
    # most popular birth years?
    if "Birth Year" in df_filtered:
        birth_years(df_filtered)
    else:
        print("Birth Year Column doesn't exist in the dataset. Skipping Birth Year statistics...")
    print("That took %s seconds." % (time.time() - start_time))

    # Display five lines of data at a time if user specifies that they would like to
    display_data(df_filtered)

    # Restart?
    restart = input('\nWould you like to restart? Type \'yes\' or \'no\'.\n').lower().strip()
    if restart.lower() == 'yes':
        statistics()


if __name__ == "__main__":
    statistics()
