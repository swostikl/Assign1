#1. Write a function that returns a random dice roll between 1 and 6. The function should not have
# any parameters. Write a main program that rolls the dice until the result is 6. The main program
# should print out the result of each roll.
import random
def roll():
    while True:
        dice_roll = random.randint(1, 6)
        result = 0
        if result!=6:
            result = dice_roll
            print(f'The rolled dice a {result}')
            if result == 6:
                break
roll()

#2.Modify the function above so that it gets the number of sides on the dice as a parameter. With
# the modified function you can for example roll a 21-sided role-playing dice. The difference to
# the last exercise is that the dice rolling in the main program continues until the program gets
# the maximum number on the dice, which is asked from the user at the beginning.

import random
def dice_roll(sides):
    return random.randint(1,sides)
def main():
    sides = int(input('Enter the sides ? '))
    attempt=0
    while True:
        rolls=dice_roll(sides)
        attempt=attempt+1
        print(f'The dice rolled for {attempt} and get  {rolls}')
        if rolls==sides:
            print(f'you rolled the maximum number! {sides}')
            break
main()






#3.Write a function that gets the quantity of gasoline in American gallons and returns the number
# converted to litres. Write a main program that asks for a volume in gallons from the user and
# converts the value to liters. The conversion must be done by using the function. Conversions
# continue until the user inputs a negative value.

def quantity_gallons(gallons):
    litres = gallons * 3.78541
    return litres
while True:
    user_input = float(input('Enter the quantity of gasoline(in American gallons): '))
    if user_input<0:
        break
    else:
        convert = quantity_gallons(user_input)
        print(f"A volume of gasoline is {convert:.2f} in litres")


#4.Write a function that gets a list of integers as a parameter. The function returns the sum of
# all the numbers in the list. For testing, write a main program where you create a list, call the
# function, and print out the value it returned.

def sum_list(numbers):
    return sum(numbers)
def main():
    my_list=[1,2,3,4,5]
    result=sum_list(my_list)
    print(f" The sum of my list : {result}")
main()

#5.Write a function that gets a list of integers as a parameter. The function returns a second list
# that is otherwise the same as the original list except that all uneven numbers have been removed.
# For testing, write a main program where you create a list, call the function, and then print out
# both the original and  the cut-down list.


def remove_odd_numbers(number):
# function takes list of integer, removes odd number and return only even number in new list
    return[num for num in number if num % 2==0]
#test function
#creating list of integer
original_list=[1,1, 1,2,2,3,4,5,6,7,8,9,10]
#call function to remove odd num
second_list=remove_odd_numbers(original_list)

#print result
print (f"original_list: {original_list}")
print (f"second_list: {second_list}")

#0r next process



#6.Write a function that receives two parameters: the diameter of a round pizza in centimeters and
# the price of the pizza in euros. The function calculates and returns the unit price of the pizza
# per square meter. The main program asks the user to enter the diameter and price of two pizzas
# and tells the user which pizza provides better value for money (which of them has a lower unit
# price). You must use the function you wrote for calculating the unit prices.

def pizza():
    diameter1 =float(input('Enter the diameter1(in cm): '))
    diameter2 =float(input('Enter the diameter2(in cm): '))
    #unit price of pizza is per square meter
    pizza1=float(input('enter the price of pizza1(in euros): '))
    pizza2=float(input('enter the price of pizza2(in euros): '))
    # to find out put the formula of area of circle i.e. area= pi/4*d**2
    area1=(3.14/4)*diameter1**2
    area2=(3.14/4)*diameter2**2

    price1=pizza1/area1
    price2=pizza2/area2
    if price1>price2:
        print(f'The price of pizza is {price2:.2f} euros per square meter, buy pizza 2')
    elif price1<price2:
        print(f'The price of pizza is {price1:.2f}  euros per square meter, buy pizza 1')
pizza()







