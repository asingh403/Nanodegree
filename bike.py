import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york': 'new_york_city.csv',
             'washington': 'washington.csv', }

Time = {0: '12:00 A.M',
        1: '1:00 A.M',
        2: '2:00 A.M',
#        return_string = "filter on month is: " + month + "\n" + \
        3: '3:00 A.M',
        4: '4:00 A.M',
        5: '5:00 A.M',
        6: '6:00 A.M',
        7: '7:00 A.M',
        8: '8:00 A.M',
        9: '9:00 A.M',
        10: '10:00 A.M',
        11: '11:00 A.M',
        12: '12:00 P.M',
        13: '1:00 P.M',
        14: '2:00 P.M',
        15: '3:00 P.M',
        16: '4:00 P.M',
        17: '5:00 P.M',
        18: '6:00 P.M',
        19: '7:00 P.M',
        20: '8:00 P.M',
        21: '9:00 P.M',
        22: '10:00 P.M',
        23: '11:00 P.M', }


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use
    # a while loop to handle invalid inputs
    while True:
        try:
            city = input(
                "Would you like to see the data for Chicago, New York, or Washington?\n")
            if city.lower() in CITY_DATA:
                break
            else:
                print("Sorry we don't have the data for this city!\n")
        except KeyboardInterrupt:
            print("Have a good day!")
            quit()
            break
        except Exception:
            print("Please Give a valid Input\n")

    # get user input for month (all, january, february, ... , june)
    while True:
        Months = ['january', 'february', 'march', 'april', 'may', 'june']
        try:
            month = input(
                "Please enter a Month for which you need the deatils(all, january, february, ... , june).\n")
            if month != "all":
                if month.lower() in Months:
                    break
                else:
                    print("Sorry we don't have the data for this month!\n")
            else:
                break
        except KeyboardInterrupt:
            print("Have a good day!")
            quit()
            break
        except Exception:
            print("Please Give a valid Input.\n")

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        days = [
            'monday',
            'tuesday',
            'wednesday',
            'thursday',
            'friday',
            'saturday',
            'sunday']
        try:
            day = input(
                "Please enter the day of the week for which you need the deatils(all, monday, tuesday, ... sunday).\n")
            if day != "all":
                if day.lower() in days:
                    break
                else:
                    print("Sorry we don't have the data for this day!\n")
            else:
                break
        except KeyboardInterrupt:
            print("Have a good day!")
            quit()
            break
        except Exception:
            print("Please Give a valid Input.\n")

    print('-' * 40)
    return city.lower(),month.lower(),day.lower()


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
    Months = ['january', 'february', 'march', 'april', 'may', 'june']

    df = pd.read_csv(CITY_DATA[city])

    if month != 'all':
        df['Start Time'] = pd.to_datetime(df['Start Time'])
        df['month'] = df['Start Time'].dt.month
        month = Months.index(month) + 1
        df = df[df['month'] == month]

    if day != "all":
        df['Start Time'] = pd.to_datetime(df['Start Time'])
        df['weekday'] = df['Start Time'].dt.weekday_name

        df = df[df['weekday'] == day.capitalize()]

    return df


def time_stats(df, city, month, day):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    Months = ['january', 'february', 'march', 'april', 'may', 'june']
    # display the most common month
    if month == "all":
        df['Start Time'] = pd.to_datetime(df['Start Time'])
        df['month'] = df['Start Time'].dt.month
        most_common_month = df['month'].mode()[0]
        print("The most common month of travel is :",
              Months[most_common_month - 1].capitalize())

    # display the most common day of week
    if day == "all":
        df['Start Time'] = pd.to_datetime(df['Start Time'])
        df['weekday'] = df['Start Time'].dt.weekday_name
        most_common_day = df['weekday'].mode()[0]
        print(
            "The most common day of travel is :",
            most_common_day.capitalize())

    # display the most common start hour
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['hour'] = df['Start Time'].dt.hour
    most_common_hour = df['hour'].mode()[0]
    count_of_most_popular_hour = len(df['hour'] == most_common_hour)
    if month == "all" and day == "all":
        return_string = "The most common hour of travel is " + \
            Time[most_common_hour] + " with count: " + str(count_of_most_popular_hour) + " when filter is none."
    if month != "all" and day == "all":
        return_string = "The most common hour of travel is " + Time[most_common_hour] + " with count: " + str(
            count_of_most_popular_hour) + " when month is " + month + " and there is no filter on day."
    if month == "all" and day != "all":
        return_string = "The most common hour of travel is " + Time[most_common_hour] + " with count: " + str(
            count_of_most_popular_hour) + " when there is no filter on month and day is " + day + "."
    if month != "all" and day != "all":
        return_string = "The most common hour of travel is " + Time[most_common_hour] + " with count: " + str(
            count_of_most_popular_hour) + " when month is " + month + " and day is " + day + "."
    print(return_string)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df, city, month, day):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    if month == "all" and day == "all":
        most_common_start_station = df['Start Station'].mode()[0]
        return_string = "filter is None\n" + \
            "The most common start station is " + most_common_start_station + "."
    if month != "all" and day == "all":
        most_common_start_station = df['Start Station'].mode()[0]
            "The most common start station is " + most_common_start_station + "."
    if month == "all" and day != "all":
        most_common_start_station = df['Start Station'].mode()[0]
        return_string = "filter on day is: " + day + "\n" + \
            "The most common start station is " + most_common_start_station + "."
    if month != "all" and day != "all":
        most_common_start_station = df['Start Station'].mode()[0]
        return_string = "filter on month is: " + month + " and filter on day is: " + \
            day + "\n" + "The most common start station is " + most_common_start_station + "."

    print(return_string)

    # display most commonly used end station
    if month == "all" and day == "all":
        most_common_end_station = df['End Station'].mode()[0]
        return_end_string = "filter is None\n" + \
            "The most common end station is " + most_common_end_station + "."
    if month != "all" and day == "all":
        most_common_end_station = df['End Station'].mode()[0]
        return_end_string = "filter on month is: " + month + "\n" + \
            "The most common end station is " + most_common_end_station + "."
    if month == "all" and day != "all":
        most_common_end_station = df['End Station'].mode()[0]
        return_end_string = "filter on day is: " + day + "\n" + \
            "The most common end station is " + most_common_end_station + "."
    if month != "all" and day != "all":
        most_common_end_station = df['End Station'].mode()[0]
        return_end_string = "filter on month is: " + month + " and filter on day is: " + \
            day + "\n" + "The most common end station is " + most_common_end_station + "."

    print(return_end_string)

    # display most frequent combination of start station and end station trip
    df['new'] = "Start Station is" + " " + df['Start Station'] + \
        "\nEnd Station is" + df['End Station']
    most_frequent = df['new'].mode()[0]
    print("The most frequent combination of stations:\n" + most_frequent)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df, city, month, day):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    if month != "all" and day != "all":
        total_trip_duration = df['Trip Duration'].sum()
        return_string = "filter: " + month + " and " + day + "\n" + \
            "Total trip duration is " + str(total_trip_duration) + '.'

    if month != "all" and day == "all":
        total_trip_duration = df['Trip Duration'].sum()
        return_string = "filter: " + month + "\n" + \
            "Total trip duration is " + str(total_trip_duration) + '.'

    if month == "all" and day != "all":
        total_trip_duration = df['Trip Duration'].sum()
        return_string = "filter: " + day + "\n" + \
            "Total trip duration is " + str(total_trip_duration) + '.'

    if month == "all" and day == "all":
        total_trip_duration = df['Trip Duration'].sum()
        return_string = "filter: None\nTotal trip duration is " + \
            str(total_trip_duration) + '.'

    print(return_string)

    # display mean travel time
    if month != "all" and day != "all":
        rows = df.shape[0]
        average_trip_duration = total_trip_duration / rows
        average_string = "filter: " + month + " and " + day + "\n" + \
            "Average trip duration is " + str(average_trip_duration) + '.'

    if month != "all" and day == "all":
        rows = df.shape[0]
        average_trip_duration = total_trip_duration / rows
        average_string = "filter: " + month + "\n" + \
            "Average trip duration is " + str(average_trip_duration) + '.'

    if month == "all" and day != "all":
        rows = df.shape[0]
        average_trip_duration = total_trip_duration / rows
        average_string = "filter: " + day + "\n" + \
            "Average trip duration is " + str(average_trip_duration) + '.'

    if month == "all" and day == "all":
        rows = df.shape[0]
        average_trip_duration = total_trip_duration / rows
        average_string = "filter: None\nAverage trip duration is " + \
            str(average_trip_duration) + '.'

    print(average_string)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df, city, month, day):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    counts = dict(df['User Type'].value_counts())
    for user in counts:
        print(user, ":", counts[user])

    # Display counts of gender
    if city.lower() == "washington":
        print("Data for Gender is not available for Washington.")
    else:
        genders = dict(df['Gender'].value_counts())
        for gender in genders:
            print(gender, ":", genders[gender])

    # Display earliest, most recent, and most common year of birth
    if city.lower() == "washington":
        print("Data for Birth Year in not available for Washington.")
    else:
        earliest = df['Birth Year'].min()
        print("Earlist year of Birth:", earliest)
        most_recent = df['Birth Year'].max()
        print("Most recent year of Birth:", (most_recent))
        most_common_birth_year = df['Birth Year'].mode()[0]
        print("Most common birth year is:", (most_common_birth_year))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df, city, month, day)
        station_stats(df, city, month, day)
        trip_duration_stats(df, city, month, day)
        user_stats(df, city, month, day)
        try:
            restart = input('\nWould you like to restart? Enter yes or no.\n')
        except KeyboardInterrupt:
            print("Have a good day!")
            quit()
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
