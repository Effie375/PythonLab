num = 1 # don't use 0!
counter = 0

while num != 0:
    num = float(input("Enter a number: "))
    if num > 0:
        counter += 1

if counter > 0:
    print("\nThe positive numbers are %d." % counter)
else:
    print("\nThe are not any positive numbers.")