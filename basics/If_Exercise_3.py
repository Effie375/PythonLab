# greek prints and inputs

first_attempt = int(input("How many meters did you jump in the first attempt? "))
second_attempt = int(input("How many meters did you jump in the second attempt? "))
third_attempt = int(input("How many meters did you jump in the first attempt? "))

average = (first_attempt + second_attempt + third_attempt)/3

print("The average is", round(average, 2), "meter.")

if average > 8:
    print("You qualified for the next race!")