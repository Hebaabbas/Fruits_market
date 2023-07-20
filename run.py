import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime
from pprint import pprint


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
    This function is to ask the user if the business day is over and in case it is yes then it would either direct to start inserting the values,
    if not, the system will inform the user to come back later
    """
    while True:
        store_condition = input("Is the business day over now and are you ready to register what was sold for today? Please insert yes or no: ")
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

    print("Welcome to " + store_name.capitalize() + "'s sales data collector.")
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
    This function is to update sold worksheet, 
    which adds a new row with the list of data indicating the value of each type of product still available in our store or how many that was needed to be gotten from the orchard to refill.
    """
    print(f"Updating {worksheet} worksheet...\n")
    sold_worksheet = SHEET.worksheet(worksheet)
    sold_worksheet.append_row(data)
    print("Worksheet is successfully updated.\n")

def update_extra_worksheet(data, worksheet):
    """
    This function is to update extra worksheet, and a new row with the list data provided
    """
    print(f"Updating {worksheet} worksheet...\n")
    extra_worksheet = SHEET.worksheet(worksheet)
    extra_worksheet.append_row(data)
    print("Worksheet is successfully updated.\n")

def calculate_extra_data(sold_row):
    """
    This function is to compare the sold with the stock and calculate the extra for each type of fruit.
    Positive surplus indicates waste/extra that was not sold and still in our store.
    Negative surplus indicates the refill that was brought from our orchard when stock was sold out.
    """
    print("Calculating our surplus and deficit data...\n")
    stock = SHEET.worksheet("stock").get_all_values()
    stock_row = stock[-1]
    print(stock_row)


    extra_data = []
    for stock, sold in zip(stock_row, sold_row):
        extra = int(stock) - sold
        extra_data.append(extra)

    return extra_data

def main():
    """
    Run all program functions
    """
    data = get_sold_data()
    sold_data = [int(num) for num in data]
    update_sold_worksheet(sold_data, "sold")
    new_extra_data = calculate_extra_data(sold_data)
    update_extra_worksheet(new_extra_data, "extra")    

main()








