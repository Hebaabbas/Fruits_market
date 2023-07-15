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

market_name = input("Hello! This is a Fruit market store data collector. Please choose a name for the market you'd like to run: ")
user_age= int(input("And now please input your age: "))
if user_age < 18:
    raise SystemExit('The user must be at least 18')


def get_sold_data():

        today = datetime.now().date()

        print("Welcome to " + market_name.capitalize() + "'s sales data collector.")
        print("Please enter how many products were sold on the date of " + str(today))
        print("Data provided are to be 8 values for different fruits kind, separated by commas.")
        print("Data provided represents these products in this order: [Strawberry ,Apple ,Banana ,Mango ,Avocado ,Orange ,Kiwi ,Lemon] and the maximum amount of products per item we can sell each day is 30. ")
        print("Data shold be as this Example: 11,11,11,11,11,11,11,11\n")

        data_str = input("Enter your data values here: \n")
        print(f"The data provided is {data_str}")

get_sold_data()


