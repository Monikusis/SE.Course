


def columns_text(line): #Split the line into a list of strings 
    columns = line.split()
    
# Separate name and birthday
    if len(columns) >= 3:
        name_column = columns[:-2] #Creating a column of names
        birthday_column = columns[-2:] #Creating a column of dates
        name = ''.join(name_column)
        birthday = ''.join(birthday_column)
        return name, birthday
    else:
        #Error handling if no name or date available    
        return "InvalidName", "InvalidBirthday"
    
    
#Read string data from a file
file_path = 'DOB.txt'
names = []
birthdays = []

#Open file with close function
with open(file_path, 'r') as file:
    for line in file:
        name, birthday = columns_text(line)
        names.append(name) #Add names
        birthdays.append(birthday) #Add dates

#Loop through names
print("Name: ")
for name in names:
        print(name)
#Loop through dates
print("\nBirthday: ")
for birthday in birthdays:
     print(birthday)
      