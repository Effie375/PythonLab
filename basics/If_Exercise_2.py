# greek prints and inputs
# print format %

def find_max(number_1, number_2):
    max_number = number_2
    if number_1 > number_2:
        max_number = number_1
    return max_number


num1 = int(input("Enter the first integer number: "))
num2 = int(input("Enter the second integer number: "))

max_num = find_max(num1, num2)

print("The maximum number is: ", max_num)