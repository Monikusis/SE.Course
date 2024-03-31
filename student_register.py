"""
Write a program that allows user to to register students
Ask user how many students are registering
Create a for loop that runs for that number of students 
Each time loop runs, ask user to enter next student ID number
Write ID numbers to reg_form.txt
Include a dotted line after each student ID 
"""

def register_students(): # Define student registration
    try: 
        num_students = int(input("How many students are registering?")) # Receive user input

        with open('reg.form.txt', 'w') as file: # Create a new txt file 
            for student_id in range(1, num_students + 1): # Loop through student IDs
                student_id = input(f"Enter student ID for student {student_id}: ")
                file.write(f"{student_id}\n") # Write in a txt file which was created
                file.write("..................................\n") # Separate student IDs

        print("Registration completed") # Close the loop 
    except ValueError: # Handle possible errors 
        print("Please enter a valid number.")

if __name__ == "__main__": # Check if script is not imported 
    register_students()