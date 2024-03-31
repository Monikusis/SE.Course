"""
Task - calculate user's total holiday cost
It includes plane cost, hotel cost, car-rental cost 
Get user inputs:
city_flight
num_nights
rental_days
Create following 4 functions: 
hotel_cost 
plane_cost
car_rental
holiday_cost
Print out all details 
"""

# Define function for hotel costs
def hotel_cost(num_nights):
    night_cost = 100 
    return num_nights * night_cost 

# Define function for plane costs 
def plane_cost(city_flight):
    flight_cost = 800
    return flight_cost 

# Define function car rental costs 
def car_rental(rental_days):
    day_cost = 50 
    return rental_days * day_cost 

# Function for total holiday costs 
def holiday_cost(city_flight, num_nights, rental_days):
    total_cost = hotel_cost(num_nights) + plane_cost(city_flight) + car_rental(rental_days)
    return total_cost 

# Get user inputs 
city_flight = input("Enter the destination city: ")
num_nights = int(input("Enter the number of nights for your stay: "))
rental_days = int(input("Enter the number of days for your car rental: "))

# Calculate and print all the details 
print("\nDetails of your holiday:")
print(f"Flight cost: £{plane_cost(city_flight)}")
print(f"Hotel cost for {num_nights} nights: £{hotel_cost(num_nights)}")
print(f"Car rent cost: {car_rental(rental_days)}")
print("-----------------------")
print(f"Total holiday cost: £{holiday_cost(city_flight, num_nights, rental_days)}")
