def odd_even(a):
    if a % 2 == 0:
        print(a,"is even.")
        return 0
    else:
        print(a, "is odd.")
        return 2

x = odd_even(5)
print(x)
