import time
import pandas as pd
import numpy as np

city_data = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filterss():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city_data = { 'chicago': 'chicago.csv',
                          'new york': 'new_york_city.csv',
                          'washington': 'washington.csv' } 
    months = ['Jan','Feb', 'Mar', 'Apr', 'May', 'Jun']
    days = ['Mon','Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    
    while True:     
            city = input("Would you like to see data for, Chicago, New York or Washington?  ").lower()
            if city not in city_data:
                print('Invalid input: Select from: --> Chicago, New York or Washington ')
                continue
            elif city in city_data:
                city = city_data[city]
                break
   
    while True:
        choice= input('Would you like to filter the data by month, day, both, or not at all? type none if u dont want to add filter  ').lower()
        if choice == 'none':
             month='all'
             day='all'
             break
        elif choice == 'both':
             while True:
                   month = input('Select month from Jan to Jun ').title()[0:3]
                   if month not in months:
                        print('Invalid input')
                        continue
                   else:
                        break          
             while True:
                   day = input('Select day from Mon to Sun '+ ' ').title()[0:3]
                   if day not in days:
                        print('Invalid input: Select from: --> Mon, Tue, Wed, Thu, Fri, Sat, or Sun  ')
                   else:   
                        break
             break
        elif choice == 'month':
             day='all'
             while True:
                   month = input('Select month from Jan to Jun ').title()[0:3]
                   if month not in months:
                        print('Invalid input')
                        continue
                   else:
                        break 
             break
        elif choice == 'day':
             month='all'   
             while True:
                   day = input('Select day from Mon to Sun '+ ' ').title()[0:3]
                   if day not in days:
                        print('Invalid input: Select from: --> Mon, Tue, Wed, Thu, Fri, Sat, or Sun  ')
                   else:   
                        break
             break
        else:
             print('Invalid input: Select from: --> month, day, both, or none  ')        

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
    df =  pd.read_csv(city)
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.strftime('%a')
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['Jan','Feb', 'Mar', 'Apr', 'May', 'Jun']
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
    popular_month = df['month'].mode()[0]
    print('Most commom month is: ')
    print (popular_month)
     
    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print ('Most commom day is: ' + popular_day)
    
    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most commom hour is: ')
    print (popular_hour)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    #Uses mode method to find the most common start station
    common_start_station = df['Start Station'].mode()[0]

    print(f"The most commonly used start station: {common_start_station}")

    # TO DO: display most commonly used end station
    #Uses mode method to find the most common end station
    common_end_station = df['End Station'].mode()[0]

    print(f"\nThe most commonly used end station: {common_end_station}")


    # TO DO: display most frequent combination of start station and end    station trip

    #Uses str.cat to combine two columsn in the df
    #Assigns the result to a new column 'Start To End'
    #Uses mode on this new column to find out the most common combination
    #of start and end stations
    df['Start To End'] = df['Start Station'].str.cat(df['End Station'], sep=' to ')
    combo = df['Start To End'].mode()[0]

    print(f"\nThe most frequent combination of trips are from {combo}.")    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time

    #Uses sum method to calculate the total trip duration
    total_duration = df['Trip Duration'].sum()
    #Finds out the duration in minutes and seconds format
    minute, second = divmod(total_duration, 60)
    #Finds out the duration in hour and minutes format
    hour, minute = divmod(minute, 60)
    print(f"The total trip duration is {hour} hours, {minute} minutes and {second} seconds.")
    

    # TO DO: display mean travel time
    average_duration = round(df['Trip Duration'].mean())
    #Finds the average duration in minutes and seconds format
    mins, sec = divmod(average_duration, 60)
    #This filter prints the time in hours, mins, sec format if the mins exceed 60
    if mins > 60:
        hrs, mins = divmod(mins, 60)
        print(f"\nThe average trip duration is {hrs} hours, {mins} minutes and {sec} seconds.")
    else:
        print(f"\nThe average trip duration is {mins} minutes and {sec} seconds.")    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('Counts of user types is ' )
    print(user_types)

    # TO DO: Display counts of gender
    try :
        user_genders = df['Gender'].value_counts()
        print('Counts of user genders is ' )
        print(user_genders)
    except Exception as err:
        print("\nThere is no 'Gender' column in this file.")
    
    # TO DO: Display earliest, most recent, and most common year of birth

    try:
        earliest = int(df['Birth Year'].min())
        recent = int(df['Birth Year'].max())
        common_year = int(df['Birth Year'].mode()[0])
        print(f"\nThe earliest year of birth: {earliest}\n\nThe most recent year of birth: {recent}\n\nThe most common year of birth: {common_year}")
    except:
        print("There are no birth year details in this file.")

    print(f"\nThis took {(time.time() - start_time)} seconds.")
    print('-'*80)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    
def display_data(df):
        """Displays 5 rows of data from the csv file for the selected city.

        Args:
            param1 (df): The data frame you wish to work with.

        Returns:
            None.
        """
        BIN_RESPONSE_LIST = ['yes', 'no']
        rdata = ''
        #counter variable is initialized as a tag to ensure only details from
        #a particular point is displayed
        counter = 0
        while rdata not in BIN_RESPONSE_LIST:
            print("\nDo you wish to view the raw data?")
            rdata = input().lower()
            #the raw data from the df is displayed if user opts for it
            if rdata == "yes":
                print(df.head())
            elif rdata not in BIN_RESPONSE_LIST:
                print("\nPlease check your input.")
                print("Input does not seem to match any of the accepted responses.")
                print("\nRestarting...\n")

        #Extra while loop here to ask user if they want to continue viewing data
        while rdata == 'yes':
            print("Do you wish to view more raw data?")
            counter += 5
            rdata = input().lower()
            #If user opts for it, this displays next 5 rows of data
            if rdata == "yes":
                 print(df[counter:counter+5])
            elif rdata != "yes":
                 break

        print('-'*80)
    
    
        
    
def main():
    while True:
        city, month, day = get_filterss()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	print("Welcome")
	main()
