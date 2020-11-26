# Python program to multiply two numbers

def multiple(a,b):
    return a * b


if __name__ == "__main__":
    # input value for variable num1
    num1 = int(input("Enter a number: "))
    # input value for variable num2
    num2 = int(input("Enter a number: "))
    # display the product
    print("The product of given numbers is %d." % multiple(num1, num2))
