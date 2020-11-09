import datetime

def calc_year(age):
    now_year = datetime.datetime.today().year
    return now_year + 100 - age 


my_name = input("Enter your name: ")

try:
    my_age = int(input("Enter your age: "))
except:
    print("Please enter an integer!")
else:
    end_year = calc_year(my_age)
    print(my_name, " in ", end_year, " will be 100 years old.")