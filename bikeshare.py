# Import libraries.
import pandas as pd
import numpy as np
from datetime import datetime

# Laod Data files.
chi=pd.read_csv('chicago.csv')
nyc=pd.read_csv('new_york_city.csv')
wa=pd.read_csv('washington.csv')

# Make dictionary of Cities data.
CITY_DATA = { 'chi': chi,
              'nyc': nyc,
              'wa': wa }
# Data Inputs.
cities=['chi','nyc', 'wa']
months=range(1,7)
days=['sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat']

# Dictionary of input short day form that suitable with the data.
days_dict={'sun':'Sunday', 'mon':'Monday', 'tue':'Tuesday', 'wed':'Wednesday', 'thu':'Thursday', 'fri':'Friday', 'sat':'Saturday'}
cities_dict={'chi':'chicago','nyc':'new york city', 'wa':'washington'}

# Input the city and correct user's inputs.
while True:
    city=input(print('\nWhich city you want? Choose one city of (chi, nyc, wa)."These are shorts of (chicago,new york city,washington)":\n')).lower()
    if city in cities:
        city_=False
        break

# Input the month and correct user's inputs.
while True:
    try:
        month=int(input(print('\nWhich month you want? Choose one month by its integer number (from 1 to 6):\n')))
        if month in months:
            month_=False
            break
    except:
        print('\n**Error!!!:The month number you have input is not integer.**')

# Input the day and correct user's inputs
while True:
    day=input(print('\nWhich day you want? Choose one day of(sun, mon, tue, wed, thu, fri, sat):\n')).lower()
    if day in days:
        day_=False
        break

# Tuple of inputted data.
filter_=(city,month,day)

# Create Function to filter the data.
def load_data(city_, month_, day_):
    """
    Loads data for the specified city and filters by month and day.

    Args:
        (str) city - name of the city to analyze (short form).
        (int) month - number of the month to filter.
        (str) day - name of the day of week to filter (short form)
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    # load data file into a dataframe
    df = CITY_DATA[city]

    # convert the Start&End Time columns to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

        # filter by month to create the new dataframe
    df = df[df['month'] == month]

        # filter by day of week to create the new dataframe
    df = df[df['day_of_week'] == days_dict[day].title()]

    # Cleaning: drop un needed column.
    df=df.drop(['Unnamed: 0'],axis=1)

    return df

# Filtered data.
data_f=load_data(filter_[0],filter_[1],day)

# Summary.
print('\n\nSummary:')
print('\n  Filters:')
print('The city you have inputted:',cities_dict[city])
print('The month you have inputted:',month)
print('The day you have inputted:',days_dict[day])
print('\n  Statistics:')
print('Total trips:',data_f.shape[0])
print('The average Trip Duration is:',data_f['Trip Duration'].mean())
print('The most frequant Start Station is:',data_f['Start Station'].mode()[0])
print('The most frequant End Station is:',data_f['End Station'].mode()[0])
print('The most rush start time hour is:',data_f['Start Time'].dt.hour.mode()[0])
print('The most rush end time hour is:',data_f['End Time'].dt.hour.mode()[0],'\n\n\n\n')

# Appeare the filtered data.
print(data_f)
print("\n\n\nThanks for using the data")
print("\nThat is your filter")
# References:
# AttributeError: 'DatetimeProperties' object has no attribute 'weekday_name': https://stackoverflow.com/questions/60214194/error-in-reading-stock-data-datetimeproperties-object-has-no-attribute-week
# Case insensitive user input strings: https://stackoverflow.com/questions/56708668/case-insensitive-user-input-strings#:~:text=Python%20doesn%27t%20do%20case%20insensitivity%2C%20but%20you%20can,the%20correct%20answer%20and%20userGuess%20to%20compare%20them
# how to change the month name column to month number column in dataframe in pandas: https://stackoverflow.com/questions/69538335/how-to-change-the-month-name-column-to-month-number-column-in-dataframe-in-panda
# pandas python how to count the number of records or rows in a dataframe: https://stackoverflow.com/questions/17468878/pandas-python-how-to-count-the-number-of-records-or-rows-in-a-dataframe
