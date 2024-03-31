# Define function for hotel costs
def calculate_hotel_cost(num_nights):
    night_rate = 100 
    return num_nights * night_rate 

# Define function for plane costs 
def calculate_plane_cost(destination_city):
    ticket_price = 800
    return ticket_price 

# Define function for car rental costs 
def calculate_car_rental_cost(rental_days):
    daily_rental_rate = 50 
    return rental_days * daily_rental_rate 

# Function for calculating total holiday costs 
def calculate_total_holiday_cost(destination_city, num_nights, rental_days):
    total_cost = calculate_hotel_cost(num_nights) + calculate_plane_cost(destination_city) + calculate_car_rental_cost(rental_days)
    return total_cost 

# Get user inputs 
destination_city = input("Enter the destination city: ")
num_nights = int(input("Enter the number of nights for your stay: "))
rental_days = int(input("Enter the number of days for your car rental: "))

# Calculate and print all the details 
print("\nDetails of your holiday:")
print(f"Flight cost: £{calculate_plane_cost(destination_city)}")
print(f"Hotel cost for {num_nights} nights: £{calculate_hotel_cost(num_nights)}")
print(f"Car rental cost: £{calculate_car_rental_cost(rental_days)}")
print("-----------------------")
print(f"Total holiday cost: £{calculate_total_holiday_cost(destination_city, num_nights, rental_days)}")
