# 1. Write a program that asks the user how many dice to roll. The program rolls all the dice once
# and prints out the sum of the numbers. Use a for loop.
import random
dice=int(input("Enter the number of dices to roll: "))
diceSet=[]
total_sum=0
i=0
for i in range(dice):
    dice_roll=random.randint(1,6)
    diceSet.append(dice_roll)
    total_sum+=dice_roll
print(diceSet)
print(f"The total sum of dice rolls is : {total_sum}")


#2.Write a program that asks the user to enter numbers until they input an empty string to quit.At
# the end, the program prints out the five greatest numbers sorted in descending order. Hint: You
#can reverse the order of sorted list items by using the sort method with the reverse=True argument.

numbers=[]
while True:
    num=(input("Enter a number or press enter to quit: "))
    if num=="":
        break
    try:
        number=int(num)
        numbers.append(number)
    except ValueError:
        print(" Invalid number , Please enter a number")
numbers.sort(reverse=True)
print('The five greatest numbers are :', numbers[:5])

#3.Write a program that asks the user for an integer and tells if the number is a prime number.
# Prime numbers are number that are only divisible by one or the number itself.

#For example, 13 is a prime number as it can only be divided by 1 or 13 so that the result is an
# integer.On the other hand, 21 is not a prime number as it is divisible by 3 and 7.

number=int (input("Enter a integer: "))
if number>1:
    for i in range(2,number):
        if number%i==0:
            print(f"{number} is not a prime number")
            break
    else:
        print(f"{number} is a prime number")

else:
    print(f"{number} is not a prime number")


#4. Write a program that asks the user to enter the names of five cities one by on (use a for loop
# for reading the names) and stores them into a list structure. Finally, the program prints out the
# names of the cities one by one, one city per line, in the same order they were read as input. Use
# a for loop for asking the names and a for/in loop to iterate through the list.

# Initialize empty list to store city names
city_name=[]
#Loop to read city names for 5 cities
for i in range(5):
    city = input("Enter a name of city(or press enter to quit): ")
    if city=="":
        break
    else:
        city_name.append(city)
        i=i+1
#use for/in loop to print the name of cities
for city in city_name:
 print(city)





