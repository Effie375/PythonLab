# Python program to check if the input number is odd or even.
# A number is even if division by 2 gives a remainder of 0.
# If the remainder is 1, it is an odd number.

def _check_odd_even(num):
    if (num % 2 == 0):
        return 0
    else:
        return 1


if __name__ == '__main__':    
    a = _check_odd_even(5)
    b = _check_odd_even(4)
    print(a, b)