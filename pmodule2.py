
from random import random, randint

name1=input("Enter first name: ")
print("Hello", name1)


import math
#find out area of circle
radius=float(input("Enter radius of circle: "))
area=math.pi*radius*radius
print("The area of the circle is ", area)


#Area of rectangle and perimeter of rectangle
l=float(input("Enter the length of rectangle: "))
b=float(input("Enter the width of rectangle: "))
area=l*b
perimeter=2*l+2*b
print("Area of rectangle: ",area)
print("Perimeter of rectangle: ",perimeter)



#a program that asks the user for three integer numbers.
# The program prints out the sum, product, and average of the numbers.
a=float(input("Enter a value of first integer: "))
b=float(input("Enter a value of second integer: "))
c=float(input("Enter a value of third integer: "))
sum=a+b+c
product=a*b*c
average=sum/product
print("The sum is", sum)
print("The product is", product)
print("The average is", average)


#Given
pounds_per_talent =20
lots_per_pound =32
grams_per_lots =13.3
#covert total_lots into full kilograms and grams

talent=float(input("Enter the number of talent: "))
pounds=float(input("Enter the number of pounds: "))
lots=float(input("Enter the number of lots: "))
talent_pounds=(talent*20)+pounds
total_lots=(talent_pounds*32)+lots
total_grams=(total_lots*13.3)
kilogram=int(total_grams/1000)
remaining_grams=float(total_grams%1000)
print(f"The weight in modern units {kilogram} and remaining grams{remaining_grams :.2f}")


#Two random combinations of numbers for a combination lock:
#a 3-digit code where each number is between 0 and 9.
code1=randint(0, 9)
code2=randint(0,9)
code3=randint(0,9)
combination=f"{code1}{code2}{code3}"
print(f"The combination for 3-digit code",combination)






#a 4-digit code where each number is between 1 and 6.
code_num1=randint(1,6)
code_num2=randint(1,6)
code_num3=randint(1,6)
code_num4=randint(1,6)
code_combination=f"{code_num1}{code_num2}{code_num3}{code_num4}"
print(f"the combination for 4-digit code" ,code_combination)

















