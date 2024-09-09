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

# def num(a):
#     a=random.randint(1,a)
#     return a
# #put user defined sides on dice
# roll_dice=int(input('Enter the number of dice: '))




#3.Write a function that gets the quantity of gasoline in American gallons and returns the number
# converted to litres. Write a main program that asks for a volume in gallons from the user and
# converts the value to liters. The conversion must be done by using the function. Conversions
# continue until the user inputs a negative value.

def quantity():
    while True:
        try:
            gasoline=float(input('Enter the quantity of gasoline(in American gallons): '))
# 1 american gallon is 3,78541 liter
            convert=gasoline*3.78541
            if convert<0:
                     print('The gas is negative, please try again')
            else:
                    print(f"A volume of gasoline is {convert:.2f}")
                    break
        except ValueError:
            print('invalid input, please try again')
quantity()

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


lis=[]
def main():
    odd_num=0
    while True:
        num=int(input('Enter the integers(or press enter to quit): '))
        if num%2==0:
            lis.append(num)
        else:
            odd_num=odd_num+1
main()

for number in lis:
    print(number)


#6.Write a function that receives two parameters: the diameter of a round pizza in centimeters and
# the price of the pizza in euros. The function calculates and returns the unit price of the pizza
# per square meter. The main program asks the user to enter the diameter and price of two pizzas
# and tells the user which pizza provides better value for money (which of them has a lower unit
# price). You must use the function you wrote for calculating the unit prices.

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
    print(f'The price of pizza is {price2:.2f} per square meter, buy pizza 2')
elif price1<price2:
    print(f'The price of pizza is {price1:.2f} per square meter, buy pizza 1')








