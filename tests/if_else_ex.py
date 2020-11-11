# Exercise 1

salary = int(input("Enter your salary: "))

if salary <= 800:
    print("You are low paid.\n")
elif salary <= 1400:
    print("You are middle paid.\n")
else:
    print("You are high paid.\n")

# Exercise 2

def find_max(number_1, number_2):
    max_number = number_2

    if number_1 > number_2:
        max_number = number_1
    return max_number


num1 = int(input("Enter the first integer number: "))
num2 = int(input("Enter the second integer number: "))

max_num = find_max(num1, num2)

print("The maximum number is: ", max_num, "\n")

# Exercise 3

first_attempt = int(input("How many meters did you jump in the first attempt? "))
second_attempt = int(input("How many meters did you jump in the second attempt? "))
third_attempt = int(input("How many meters did you jump in the first attempt? "))

average = (first_attempt + second_attempt + third_attempt)/3

print("The average is: ", round(average, 2), " meter.\n")

if average > 8:
    print("You qualified for the next race!\n")
 
# Exercise 4

car_displacement = int(input("How much displacement does your car has? "))

if car_displacement <= 1100:
    print("The tax corresponds to 100€.\n")
elif car_displacement <= 1400:
    print("The tax corresponds to 150€.\n")
elif car_displacement <= 2000:
    print("The tax corresponds to 225€.\n")
else:
    print("The tax corresponds to 600€.\n")
