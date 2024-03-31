# Person competing in triathlon timings
# Get input for swimming time
activity_1 = int(input("Please enter your swimming time: "))
# Get input for cycling time 
activity_2 = int(input("Please enter your cycling time: "))
# Get input for running time
activity_3 = int(input("Please enter your running time: "))

# Calculate the total time by summing up activities 
total_time = activity_1 + activity_2 + activity_3
# Display the total time
print(f"Total time taken to complete triathlon: {total_time} minutes.")

# Set the qualifying time for award 
qualifying_time = 100 

# Use operators to determine the award time
if total_time == 100:
    print("Well done! Your award is Provincial Colours.")
elif total_time >= 101 and total_time <= 105:
    print("Well done! Your award is Provincial Half Colours.")
elif total_time >= 106 and total_time <= 110:
    print("Well done! Your award is Provincial Scroll.")
# Handle the case where time is below qualifying time
else:
    print("Sorry! You are not entitled to award.")





