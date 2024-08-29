# 1 .Write a program that asks a fisher the length of a zander in centimeters.If the zander does not
# fulfill the size limit, the program instructs to release the fish back into the lake and notifies
# the user of how many centimeters below the size limit the caught fish was.
# A zander must be 42 centimeters or longer to meet the size limit.

Fisher=float(input("Enter the length of the zander in cm: "))
length=42
if Fisher >= length:
    print("The caught fish was size limit.")
else:
    belows_size=length-Fisher
    print("Release fish back into lake.", "The size limit is less by cm :",belows_size)


#2.Write a program that asks the user to enter the cabin class of a cruise ship and then prints out a written description according to the list below. You must use an if/elif/else structure in your solution.

# LUX: upper-deck cabin with a balcony.
# A: above the car deck, equipped with a window.
# B: windowless cabin above the car deck.
# C: windowless cabin below the car deck.
# If the user enters an invalid cabin class, the program outputs an error message Invalid cabin class.


Cabin=(input("Enter the cabin class of a cruise ship:(A/B/C/LUX) : ")).upper()
if Cabin=="LUX":
    print("LUX:upper-deck  cabin with a balcony.")
elif Cabin=="A":
    print("A:above the car deck, equipped with a window.")
elif Cabin=="B":
    print("B:windowless cabin above the car deck.")
elif Cabin=="C":
    print("C:windowless cabin below the car deck.")
else:
    print("Invalid cabin entered.")

#Write a program that asks for the biological gender and hemoglobin value (g/l). The program the notifies the user if the hemoglobin value is low, normal or high.

#A normal hemoglobin value for adult females is between 117-155 g/l.
#A normal hemoglobin value for adult males is between 134-167 g/l.

gender=input("Enter your gender(m/f): ")
hemoglobin_value=float(input("Enter your hemoglobin value(g/l): "))
if gender=="m" and 134<=hemoglobin_value<=167:
    print("Your hemoglobin is normal")
else:
    if gender=="m" and hemoglobin_value<134:
        print("Your hemoglobin is low")
    elif gender=="m" and hemoglobin_value>167:
        print("Your hemoglobin is high")
    if gender=="f" and  117 <=hemoglobin_value <=155:
        print("Your hemoglobin is normal")
    if hemoglobin_value<117:
        print("Your hemoglobin is low")
    if hemoglobin_value>155:
        print("Your hemoglobin is high")



#Write a program that asks the user to enter a year and notifies the user whether the input year is a
#leap year. A year is a leap year if it is divisible by four. However, years divisible by 100 are leap years only if they are also divisible by 400.



year=int(input("Enter your year: "))
if year%4==0:
    print("Leap year")
    if year%100==0 and year%400==0:
        print ("leap year")
else:
    print("Not leap year")




