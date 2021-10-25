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
    
   #while loop here handles the exceptions
    while True:
        cities = ["chicago", "washington", "new york city"]
        city= input("\nPlease enter your specified city from (chicago, new york city, washington): ").lower()
        if city in cities:
            break
        else:
            print("\nPlease enter a valid value like (chicago, new york city, washington)")
            
            
    while True:
        months = ["all", "january", "february", "march", "april", "may", "june"]
        month= input("\nPlease enter your filtering month from january to june or type 'all' if you want no filtering: ").lower()
        if month in months:
            break
        else:
            print("\nPlease enter a valid value like (all, january, may...)")
        
    while True:
        days = ["all", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
        day= input("\nPlease enter your filtering day from monday to sunday or type 'all' if you want no filtering: ").lower()
        if day in days:
            break
        else:
            print("\nPlease enter a valid value like (all, monday, thursday...)")       
    


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
    
    df= pd.read_csv(CITY_DATA[city]) #loading the dictionary of the required city into a dataframe
    df['Start Time']= pd.to_datetime(df['Start Time'])
    df['Month']= df['Start Time'].dt.month
    df['Day']= df['Start Time'].dt.weekday_name
    
    if month != "all": #in case of a filtering month
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['Month'] == month]
        #creating a new dataframe to filter data by a month
        
    if day != "all": #in case of a filtering day
        df = df[df['Day'] == day.title()]
        #creating a new dataframe to filter data by a day


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    
    most_common_month= df['Month'].mode()[0]
    print("\nMost common month is :" , most_common_month)
    
    most_common_day= df['Day'].mode()[0]
    print("\nMost common day is :" , most_common_day)
    
    df['Hour'] = df['Start Time'].dt.hour #as hour dataframe wasn't initially defined like month and day
    most_common_hour= df['Hour'].mode()[0]
    print("\nMost common hour is :" , most_common_hour)
    




    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    
    most_common_start_station= df['Start Station'].mode()[0]
    print("\nMost common start station is : {} station".format(most_common_start_station))
    
    most_common_end_station= df['End Station'].mode()[0]
    print("\nMost common end station is : {} station".format(most_common_end_station))
    
    df['Trip']= df['Start Station'] +" --TO-- "+ df['End Station'] #combining both of the start station and the end station together to get the whole trip
    most_common_trip= df['Trip'].mode()[0]
    print("\nMost common trip is :" , most_common_trip)
    
    



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    
    Total_travel_time= df['Trip Duration'].sum()
    Average_travel_time= df['Trip Duration'].mean()

    
    print("\nThe total travel time of trips is : {} hours".format(Total_travel_time))
    print("\nThe average travel time of trips is : {} hours".format(Average_travel_time))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city): #adding the city attribute to use it down below
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    #calculating the user types count for the 3 cities
    user_types = df['User Type'].value_counts()
    print("\nUser type counts are :\n {} ".format(user_types))
    
    #calculating gender count, earliest birth year, most recent birth year and common birth year for Chicago and NYC only
    if city == 'new york city' or city == 'chicago':
        gender_counts = df['Gender'].value_counts()
        print("\nGender counts for {} are :\n {} ".format(city, gender_counts))
        
        earliest_birth_year = int(df['Birth Year'].min()) 
        print("\nEarliest birth year for {} is : {} ".format(city, earliest_birth_year))
        
        most_recent_birth_year = int(df['Birth Year'].max())
        print("\nMost recent birth year for {} is : {} ".format(city, most_recent_birth_year))
        
        most_common_birth_year = int(df['Birth Year'].mode()[0])
        print("\nMost common birth year for {} is : {} ".format(city, most_common_birth_year))
        
        #adding 'int' in order to not represent the years as float
        

   


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

 

def raw_data_display(df):
    
    
    data_display = input("\nDo you like to be shown the first 5 rows of raw data? (yes/no) : ").lower()
    initial_row = 0
    
    while data_display == 'yes':
        print(df.iloc[initial_row: initial_row + 5])
        more_data_display = input("\nDo you like to be shown the next 5 rows? (yes/no) : ").lower()
        
        while more_data_display == 'yes':
            initial_row += 5
            print(df.iloc[initial_row: initial_row + 5])
            more_data_display = input("\nDo you like to be shown the next 5 rows? (yes/no) : ").lower()
        else:
            print("\nTHAT'S IT!\n---------------------------------------------------------")
            break      
        
    else:
        print("\nTHAT'S IT!\n---------------------------------------------------------")
                



def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city) #adding the 'city' attribute to use it in user_stats function
        raw_data_display(df) 

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
