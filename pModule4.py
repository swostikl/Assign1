#1.Write a program that uses a while loop to print out all numbers divisible by three in the range of 1-1000.

num=0
while num<=1000:
    num=num+1
    div=num%3
    if div==0:
        print("Number divisible by 3 is : ",num)

#2.Write a program that converts inches to centimeters until the user inputs a negative value. Then the program ends.

# 1 inch = 2.54 cm

while True:
    inches=float(input( " Enter a number in inch (not a  negative number): "))
    if inches<0:
        print("Program ended as it is negative value.")
        break
    cm =2.54*inches
    print(f"{inches} inches is equal to {cm} cm")

#3.Write a program that asks the user to enter numbers until they enter an empty string to quit. Finally,
# the program prints out the smallest and largest number from the numbers it received.


numbers=[]
while True:
    a=input("Enter a number (or press enter to finish):")
    if a=="":
        break
    a = float(a)
    numbers.append(a)
if numbers:
        print(f"The smallest number is ,{min(numbers)}")
        print(f"The largest number is ,{max(numbers)}")


#4.Write a game where the computer draws a random integer between 1 and 10. The user tries to guess
# the number until they guess the right number. After each guess the program prints out a text: Too
# high, Too low or Correct. Notice that the computer must not change the number between guesses.


import random
number_guess= random.randint(1,10)
while True:
    guess=float(input( " Guess a number between 1 and 10: "))
    if guess>number_guess:
        print("Too high.")
    elif guess < number_guess:
        print("Too low.")
    else:
        print(" You have guessed correctly.")
        break

#5.Write a program that asks the user for a username and password. If either or both are incorrect,
# the program ask the user to enter the username and password again. This continues until the
# login information is correct or wrong credentials have been entered five times. If the information
# is correct, the program prints out Welcome. After five failed attempts the program prints out Access
# denied. The correct username is python and password rules.

correct_username="python"
correct_password="rules"
attempts=0
while attempts<5:
    username=input("Enter your username: ")
    password=input("Enter your password: ")
    if username!=correct_username and password!=correct_password:
        print ("Wrong username or password. Try again.")
        attempts+=1
    else:
        print("welcome")
        break
else:
    print("Access denied.")

#6.Implement an algorithm for calculating an approximation for the value of pi (π). Let's assume
# that A is a unit circle. A unit circle has the radius of one, it is centered at the origin
# (0,0). Smallest possible square B is drawn around the unit circle so that circle A is completely
# inside the square. The corners of the square are now (-1,-1), (1, -1), (1, 1), and (-1, 1). If a
# large number of random points are scattered inside the square, the fraction of points that fall
# inside the circle A correlates with the fraction of the area of circle A compared to the area of
# square B: πr^2/4 = π*1^2/4 = π/4. This can be used as a simple method for calculating an
# approximation of the value of pi: Let's generate a large number of random points, such as one
# million, inside square B. Let N be the total number of random points. Each point inside the
# square is tested for whether it resides inside circle A. Let n be the total number of points that
# fall inside circle A. Now we have n/N≈π/4, and from that we get π≈4n/N. Write a program that asks
# the user how many random points to generate, and then calculates the approximate value of pi using
#the method explained above. At the end, the program prints out the approximation of pi to the user.
# (Notice that it is easy to test if a point falls inside circle A by testing if it fulfills the
# in equation x^2+y^2<1.).

import random
def approximate_pi(num_points):
    inside_circle = 0
    for _ in range(num_points):
        x = random.uniform(-1,1)
        y = random.uniform(-1,1)
        if x**2 + y**2 <= 1:
            inside_circle += 1

    pi_approximation = 4 * inside_circle / num_points
    return pi_approximation
# set the number of random points to generate
num_points = 1000000 # given as 1 million

# calculate the value of pi approximate
pi_approximation = approximate_pi(num_points)
print(pi_approximation)


