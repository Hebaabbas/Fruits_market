import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('Fruits_market')

store_name = input("Hello! This is a Fruit market store data collector. Please choose a name for the market you'd like to run: ")
user_age = int(input("And now please input your age: "))
if user_age < 18:
    raise SystemExit('The user must be at least 18')

def store_ready():
    """
    This function is to ask the user if the business day is over and incase it is yes then it would either direct to start inserting the values, 
    if not the system will inform the user to come back later
    """       
    while True:
        store_condition = input("Is the business day over now and you are ready to register what was sold for today? please insert yes or no: ")
        if store_condition.lower() == "yes":
            print("Great! Now you can input the amount you have sold.")
            return True
        elif store_condition.lower() == "no":
            print("Please come back when the business day is over.")
            return False
        else:
            print("You did not insert a valid option, please give it another try")
            continue

def get_sold_data():
    """
    This function is to show what name the user has picked for the market and the business day date as well as to input the value sold by the end of the day.
    """
    today = datetime.now().date()

    print("Welcome to " + market_name.capitalize() + "'s sales data collector.")
    print("Please enter how many products were sold on the date of " + str(today))
    print("Data provided are to be 8 values for different fruits kind, separated by commas.")
    print("Data provided represents these products in this order: [Strawberry, Apple, Banana, Mango, Avocado, Orange, Kiwi, Lemon] and the maximum amount of products per item we can sell each day is 30.")
    print("Data should be as this Example: 11,11,11,11,11,11,11,11\n")

    while True:
        data_str = input("Enter your data values here: \n")
        sold_data = data_str.split(",")

        if validate_data(sold_data):
            print("Data is valid!")
            break

    return sold_data


def validate_data(values):
    """
    This function is to check if there are exactly 8 values in our data
    and to check if all data can be converted into integers.
    """
    try:
        [int(value) for value in values]
        if len(values) != 8:
            raise ValueError(
                f"The data provided is {len(values)}, the required data to be entered has to be 8 values"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please enter 8 values.\n")
        return False

    return True

def update_sold_worksheet(data, worksheet):
    """
    This function is to update sold worksheet, and new row with the list data provided
    """
    print(f"Updating {worksheet} worksheet...\n")
    sold_worksheet = SHEET.worksheet(worksheet)
    sold_worksheet.append_row(data)
    print("Worksheet is successfully updated.\n")

def main():
    """
    Run all program functions
    """  
    store = store_ready()
    data = get_sold_data()
    sold_data = [int(num) for num in data]
    update_sold_worksheet(sold_data, "sold")

main()







