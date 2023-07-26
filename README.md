# Fruits Market
Fruit Market Sales Data Collector application; The purpose of this Python application is to help manage and analyze sales data for a fruit market store. The code allows the user (the store owner or manager) to input the number of products sold for different types of fruits on a given business day.

Here is the live version of the project.

![Alt Text](./media/1.png)

## How to use:
- Open your terminal, the program will start by asking for your age and the name of your fruit market store. Enter the required information.

- Enter Sales Data: If the business day is over and you are ready to register the products sold, the program will prompt you to input the number of products sold for each fruit type. Provide the quantities separated by commas.

- Validation and Data Update: The program will validate your input and update the sales data in the Google Sheets document.

- Surplus/Deficit Calculation: The program will calculate the surplus or deficit for each fruit based on the current stock and the sales data. It will display the results.

- Stock Calculation: The program will calculate the stock for each fruit type for the next business day, considering the average sales of the last three days and adding 5% to each value. It will display the stock data in a dictionary format.

- Thank You: The program will thank you for using it, and you can close the terminal.

## Features:
- User-friendly:

The program starts by asking for your age and the name of your fruit market store. It ensures that the user is at least 18 years old to proceed.

![Alt Text](./media/2.png)

The program stops if the user is less than 18

![Alt Text](./media/3.png)

The program continues to ask the user to pick a name for their market

![Alt Text](./media/4.png)

- Data Status:
The program will ask the user if the business day is over to start inserting the data or not by sending a yes or no:

In case it isnt done:
![Alt Text](./media/5.png)
It will stop the program from running.

In case it is done, it leads us to the next feature:

- 6-steps outcomes feature:

1. Data Collection:
After the initial setup, the program prompts you to input the number of products sold for each fruit type (e.g., Strawberry, Apple, Banana, Mango, Avocado, Orange, Kiwi, Lemon) on the current business day.

2. Data Validation: The program validates the input data, ensuring that you provide exactly eight values, and each value is a whole number. It asks you to re-enter the data if there are any issues.

3. Data Update: Once the data is validated, the program updates the sales data in the Google Sheets document, making it easy to keep track of the daily sales.

4. Surplus/Deficit Calculation: The program calculates the surplus or deficit for each fruit based on the current stock and the sales data. It shows the additional fruits remaining in the stock or the number of fruits that need to be replenished from the orchard.

5. Stock Calculation: The program calculates the stock for each fruit type for the next business day. It uses the average sales of the last three days and adds 5% to each value to ensure sufficient stock availability.

![Alt Text](./media/7.png)

![Alt Text](./media/8.png)

- User experience: 

Thank You: The program will thank you for using it, and you can close the terminal.


## Other programs used at the same time

The Fruit Market Sales Data Collector uses the gspread library to interact with Google Sheets.

Any data updated will be shown on the Google sheets. In our example we have user previously we can see that our data will be updated in 3 different sheets in the worksheet :

1. The data we have inserted are saved in the Sold sheet (indicated what was sold by the end of the business day):
![Alt Text](./media/9.png)


2. The extra sheet is for the surplus and deficit calculations which show the values that were extra by the end of the day in the stock and the values that was needed to be brought in as a refill during the business day:
![Alt Text](./media/10.png)

3. And last but not least, The stock sheet and thats where the program saves and lets the user know the value that has to be in the stock by the begining of the next business day based of calculating sales averages and adding 5% to the values:
![Alt Text](./media/11.png)

## Testing:
I have manually tested this project by doing the following:
1. Tested the code using PEP8 website and there are no problmes.
2. Tested the code in my local terminal and the Code Institure Heroku terminal.

## Bugs
No bugs or errors found.

## Validator Testing
- PEP8:
No errors were returned from PEP8online.com

## Deployment:
This project was deployed using Code institute's mock terminal for Heroku.
- Steps for Deployment:
1. Create a new Heroku app
2. Set the buildbacks to Python anf NodeJS
3. Link the Heroku app to the repository
4. Deploy and View.

## Credits:
1. Code institute for the deployment terminal
2. Code institute's sample project that was used as a big help.
