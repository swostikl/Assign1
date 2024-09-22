# 1. Write a program that asks the user for a number of a month and then prints out the corresponding
# season (spring, summer, autumn, winter). Save the seasons as strings into a tuple in your program.
# We can define each season to last three months, December being the first month  of winter.

def season(month):
    seasons=("winter","spring","summer","autumn")
    if month in (12,1,2):
        return seasons[0] #winter
    if month in (3,4,5):
        return seasons[1] #spring
    if month in (6,7,8):
        return seasons[2] #summer
    if month in (9,10,11):
        return seasons[3] #autumn
    else:
        "No month "
month=int(input("Enter a month (1-12) : "))
season=season(month)
print(f" The month number {month} is {season}")




# 2.Write a program that asks the user to enter names until he/she enters an empty string. After each name is read the
# program either prints out New name or Existing name depending on whether the name was entered for the first time.
# Finally, the program lists out the input names one by one, one below another in any order. Use the set data structure
# to store the names.
def main():
    names=set()
    while True:
        name=input("Enter a name or enter to quit: ")
        if name=="":
            break
        if name in names:
            print("Existing name")
        else:
            print("New name")
            names.add(name)
    print("list of names entered : ")
    for name in names:
     print(name)
main()

# 3.Write a program for fetching and storing airport data. The program asks the user if they want to enter a new
# airport, fetch the information of an existing airport or quit. If the user chooses to enter a new airport, the
# program asks the user to enter the ICAO code and name of the airport. If the user chooses to fetch airport
# information instead, the program asks for the ICAO code of the airport and prints out the corresponding name. If the
# user chooses to quit, the program execution ends. The user can choose a new option as many times they want until
# they choose to quit. (The ICAO code is an identifier that is unique to each airport. For example, the ICAO code of
# Helsinki-Vantaa Airport is EFHK. You can easily find the ICAO codes of different airports online.)
airports = {'VNKA': 'Kathmandu Airport',
           'VNIA':'Deli Airport',
           'VNFA': 'Helsinki Airport',
           'VNCA':'China Airport'
            }
while True:
    print("\nSelect an option")
    print("1. Enter a new airport")
    print("2. Fetch existing airport information")
    print("3. Exit")
    choice = input("Enter your choice (1/2/3): ")
    if choice == '1':
        icao_code = input("Enter the ICAO code of the airport: ")
        if icao_code in airports:
            print(f"The ICAO code {icao_code} has been already added")
        else:
            new_name = input("Enter the new airport name: ")
            if new_name:
                airports[icao_code] = new_name
                print(f"New airport name {new_name}  with ICAO code {icao_code} has been added")
            else:
                print("Error: Airport name is empty")
    elif choice == '2':
        if airports:
            print("Here are the available lists of airports:")
            for key in airports.keys():
                print(key)
            icaoCode = input("Enter the ICAO code of the airport: ").upper()
            if icaoCode in airports:
                print(f"The name of the airport with ICAO code {icaoCode} is: {airports[icaoCode]}")
            else:
                print("Airport not found")
        else:
            print("No airports available in te list")


    elif choice == '3':
        print("Good Bye")
        break
    else:
        print("Invalid option, please select option")