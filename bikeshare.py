import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    cities = ['chicago', 'new york city', 'washington']
    months = ['january', 'february', 'march', 'april', 'may', 'june','all']
    days_of_week = ['sunday', 'monday', 'tuesday', 'wednesday','thursday', 'friday', 'saturday', 'all']

    while True:
        city = input ('Please enter the city- Chicago, New york city, Washington: '). lower()
        if city in cities:
            break
        else:
            print('Please check your input')


    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input ('please enter the month:-all or January, February, March, April, May, June: ' ).lower()
        if month in months:
            break
        else:
            print('Please check your input,: ')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input ('please enter the day:select sunday, monday, tuesday, wednesday, thursday, friday, saturday, all:  ').lower()
        if day in days_of_week:
            break
        else:
            print('Please check your input, ')


    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
     # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] =df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    month = df['month'].mode()[0]
    months = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6:'June'}
    print('most common month: ', months[month])
    # TO DO: display the most common day of week
    day = df['day_of_week'].mode()[0]
    print('most common day: ', day)
    # TO DO: display the most common start hour
    common_start_hour = df['hour'].mode()[0]
    print('most common hour: ',common_start_hour)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station =df['Start Station'].mode()[0]
    print('most commonly used start station: ', start_station)

    # TO DO: display most commonly used end station
    end_station = df['End Station'].mode()[0]
    print('most commonly used end station: ', end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df['start_end_station'] = df['Start Station'] + ', ' + df ['End Station']
    start_end_station = df['start_end_station'].mode()[0]
    print('most frequent combination of start and end station: ', start_end_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    travel_time = df['Trip Duration'].sum()
    travel_time_hrs =travel_time/3600.0
    print('Total travel time (hours): ', travel_time_hrs)

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    mean_travel_time_hrs = mean_travel_time/3600.0
    print('Mean travel time (hours): ', mean_travel_time_hrs)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('Bike users:\n', user_types)
    print()
    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        gender = df['Gender'].value_counts()
        print('counts of Gender \n ', gender)
    else:
        print('no gender data availble')
    print()
    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest_year  = df['Birth Year'].min()
        print('Earliest year of birth: ', earliest_year)
        recent_year  = df['Birth Year'].max()
        print('Recent year of birth: ', recent_year)
        common_year  = df['Birth Year'].mode()[0]
        print('Common year of birth: ', common_year)
    else:
        print('no year of birth data availble')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
