import pandas as pd 
import numpy as np
from datetime import datetime

# Specify the file path
file_path = "SatTeam/data/hackupc-travelperk-dataset.csv"  # This path does not have the activities, Change it if we got time

# Read the CSV file into a DataFrame
df = pd.read_csv(file_path, header= 0)   # Esto es mi excel I guess
#print('type=', type(df))   #test stuff

#df = df.values.tolist()       # CSV converted to list, each one corresponding to a row (a customer)

df_simple = [row[1:] for row in df.values]  # this has to strip away the first coloumn (customer number) while making it a list

#print(df_simple)                           #this is test stuff
#print(df_simple[1][0])

            # Test Invented profile
name = "Quandale"
Ddate = "04/07/2024"    # Dates format MUST be written as DD/MM/YYYY and user should be obligated to do so
Rdate = '07/07/2024'    
Dcity = 'Dublin'          # Cities should not be written by users, should be proposed by the page
Acity = 'Rome'
# Activites = [LIST]            # To be done

OverlapIntended = 3      # The customer may decide how many days he wants to coincide with someone



UserProfileTest = [name, Ddate, Rdate, Dcity, Acity]   # The imput profile caracteristics to be compared

#print(UserProfileTest)         #test stuff
#print(df_simple[10])

# --------------------------------------------------------------------------------------------------------------------
# Prototype 1 : Arrival and Departure dates are the same and no activities are registered. Coincidences are low but program runs

def UserComparer1(UserProfile, DataBase):  # This function is meant to compare Users caracteristics
    CompatibleUsers = []
    for user in DataBase:
        if np.array_equal(UserProfile[1:], user[1:]):  # Compare elements 1 to 4 (excluding element 0)
            CompatibleUsers.append(user[0])  # Append the identifier (element 0) of the compatible user
    
    if len(CompatibleUsers) != 0:
        return CompatibleUsers
    else:
        return 'No compatible results'



#TestList = UserComparer1(UserProfileTest, df_simple)      #test stuff
#print(TestList)


# ------------------------------------------------------------------------------------------------------------------------
# Prototype 2: Coincide at least 3 days in the same city


def parse_date(date_str):       # Date converter to treat the values
    # Parse date string into datetime object
    return datetime.strptime(date_str, '%d/%m/%Y')


def UserComparer2(UserProfile, DataBase , OverlapIntended):
    #OverlapIntended is an integer meant to be the days the customer wants to coincide with the stranger

    CompatibleUsers = []

    # Parse UserProfile dates
    user_date1 = parse_date(UserProfile[1])   # Get the dates from the Customer 
    user_date2 = parse_date(UserProfile[2])
    
    for user in DataBase:
        # Parse dates from CompatibleUsers
        comp_user_date1 = parse_date(user[1])    # Compare with the dates of the others on the database
        comp_user_date2 = parse_date(user[2])
        
        # Check if dates overlap by at least 3 days
        overlap_days = (min(user_date2, comp_user_date2) - max(user_date1, comp_user_date1)).days + 1

        if overlap_days >= OverlapIntended and np.array_equal(UserProfile[4],user[4]) :     # The Arrival city has to be the same
            CompatibleUsers.append(user[0])  # Append the identifier (element 0) of the compatible user
    

    if len(CompatibleUsers) != 0:
        return CompatibleUsers
    else:
        return 'No compatible results'



#TestList1 = UserComparer2(UserProfileTest, df_simple, OverlapIntended)      #test stuff
#print(TestList1)

# ------------------------------------------------------------------------------------------------------------------------
