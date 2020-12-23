# Python program to multiply two numbers

def _multiple(num1, num2):
    return num1 * num2


if __name__ == '__main__':
    # input value for variable number_1
    number_1 = int(input("Enter a number: "))
    # input value for variable number_2
    number_2 = int(input("Enter a number: "))
    # display the product
    print("The product of given numbers is %d." % _multiple(number_1, number_2))
