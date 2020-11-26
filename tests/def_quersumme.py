# Python program to sum all the digits of an input number

def quersumme(num):
    qs = 0
    # while loop to iterate through all the digits of input number
    while(num>0):
        qs += num % 10
        num = num // 10
    return qs


if __name__ == "__main__":
    num = int(input("Enter a number: "))
    qs = num
    while(qs >= 10):
        qs = quersumme(qs)
    # displaying output
    print("Quersumme:", qs)
    
