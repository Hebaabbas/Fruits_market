import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime
import json


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('Fruits_market')

# Global variables to store user age and store name
store_name = None
user_age = None

def get_user_info():
    global user_age, store_name

    if user_age is None:
        user_age = int(input("Hello! This is a Fruit market store data collector. Please input your age: \n"))
        if user_age < 18:
            raise SystemExit('The user must be at least 18')

    if store_name is None:
        store_name = input("Please choose a name for the market you'd like to run: \n")

def store_ready():
    """
    This function is to ask the user if the business day is over and in case it is yes then it would either direct to start inserting the values,
    if not, the system will inform the user to come back later
    """
    while True:
        store_condition = input("Is the business day over now and are you ready to register what was sold for today? Please insert yes or no: \n")
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


def update_worksheet(data, worksheet):
    """
    This function allows the user update the worksheet based on the data provided
    """
    print(f"Updating {worksheet} worksheet...\n")
    worksheet_to_update = SHEET.worksheet(worksheet)
    worksheet_to_update.append_row(data)
    print(f"{worksheet} worksheet is successfully updated.\n")



def calculate_extra_data(sold_row):
    """
    This function is to compare the sold with the stock and calculate the extra for each type of fruit.
    Positive surplus indicates waste/extra that was not sold and still in our store.
    Negative surplus indicates the refill that was brought from our orchard when stock was sold out.
    """
    print("Calculating our surplus and deficit data...\n")
    stock = SHEET.worksheet("stock").get_all_values()
    stock_row = stock[-1]
    print("Current stock data:", stock_row)


    extra_data = []
    for stock, sold in zip(stock_row, sold_row):
        extra = int(stock) - sold
        extra_data.append(extra)
        
    print("Positive numbers are what the store had surplus from the stock and negative are what the owner had to refill:", extra_data)

    return extra_data




def get_last_3_entries_sold():
    """
    Collects the last 3 entries from sold column worksheet which
    shows how many entries were sold during the last 3 business days
    and returns the data as a list of lists. 
    """
    sold = SHEET.worksheet("sold")

    columns = []
    for ind in range(1, 9):
        column = sold.col_values(ind)
        columns.append(column[-3:])

    return columns

def calculate_stock_data(data):
    """
    Calculate the average stock for each fruit type, adding 5% on each value and rounding it
    """
    print("Calculating stock data...\n")
    new_stock_data = []

    for column in data:
        int_column = []
        for num in column:
            try:
                int_column.append(int(num))
            except ValueError:
                continue
            
        average = sum(int_column) / len(int_column)
        stock_num = average * 1.05
        new_stock_data.append(round(stock_num))

    print("After calculating the average and adding 5% to our stock, our stock for tomorrow's business day is:", new_stock_data)

    return new_stock_data

def get_fruit_names():
    """
    Get the list of fruit names for the dictionary keys
    """
    return ["Strawberry", "Apple", "Banana", "Mango", "Avocado", "Orange", "Kiwi", "Lemon"]

def create_stock_dictionary(fruit_names, stock_data):
    """
    Create a dictionary of fruit names and their corresponding stock values
    """
    stock_dict = dict(zip(fruit_names, stock_data))
    return stock_dict

def main():
    """
    Run all program functions
    """
    get_user_info()
    store_ready()
    data = get_sold_data()
    sold_data = [int(num) for num in data]
    update_worksheet(sold_data, "sold")
    new_extra_data = calculate_extra_data(sold_data)
    update_worksheet(new_extra_data, "extra")    
    sold_columns = get_last_3_entries_sold()
    stock_data= calculate_stock_data(sold_columns)
    update_worksheet(stock_data, "stock")
    
    # Get the fruit names and create the stock dictionary
    fruit_names = get_fruit_names()
    stock_dict = create_stock_dictionary(fruit_names, stock_data)

    # Print the stock dictionary to the terminal
    print("\nStock for tomorrow's business day to be filled with:")
    print(stock_dict)

main()
print("Thank you for using our market program for today, welcome back tomorrow!")







