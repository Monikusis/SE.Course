"""
Create a list called menu, containing at least 4 items
Create a dictionary called stock, which contains the stock value for each item
Another dictionary called price, which contain prices for each item
Calculate total_stock worth in cafe. 
Loop through appropriate dictionaries and lists
Tip: 'items' can be set as keys
item_value = (stock[items] * price[items])
Print out result of calculation
"""
import math
#Creating menu list 
menu_list = ["Orange juice", "Coffee", "Toast", "Eggs"]

#Creating Dictionary for stock
stock = {"Orange juice": 50,
               "Coffee": 75,
               "Toast": 45,
               "Eggs": 65
               }

stock_items = stock.values()

#Creating price dictionary 
price = {"Orange juice": 4.99,
             "Coffee": 3.50,
             "Toast": 5.50,
             "Eggs": 6.99
             }

price_list = price.values()

#Calculating total worth of stock 
total_stock_worth = 0

#Loop through items to count total worth
for item in stock:
    item_value = stock[item] * price[item]
    total_stock_worth += item_value # Assign value to total_stock_worth

#Print output 
print("Total value of cafe stock is: £", total_stock_worth)


