"""
x = "3"
y = 2
c = int(x) + y
print(c)
"""

"""
name = input("Enter your name: ")
age = input("Enter your age: ")
print("Your name is " + name)
print("Your age is ", age)
"""

'''Modulo (mod)'''
print(11 % 3)  # 2
print(4 % 3)   # 1
print(4 % 2)   # 0
print(3 % 4)   # 3
print(0 % 4)   # 0
print(1 % 4)   # 1

'''if...else'''
x = 9

if x < 10:
    print("x is lower than 10.")
else:
    print("x is equal or greater than 10.")

'''
num = input("Enter a number: ")

if int(num) % 2:
    print("The number ", num, " is odd.")  # 1,3,5,...,z+1
else:
    print("The number ", num, " is even.")  # 2,4,6,...,z
'''

print(5//3)
print(0//3)
print(5/3)
print(6/2)

If = 3  # case sensitive

print(2**3)  # 8
print(2*3)   # 6

print(5 < 10)
print(10 < 5)
print(10 == 5)
print(not 10 < 20 or 30 < 20)

#  print(type(input("Enter a word: ")))

print(5, 2)
print("Hello,", "Efi")

_test = 3

x = 1
x = x + 1
print(x)

print(10e3)
print(2e3)

R = 10**9  # 1GW // Int
print(R)
R = 1e9  # 1GW // Float
print(R)

x = 1
y = 1

print((x and False) == False)
print((False and x) == False)
print((y and x) == (x and y))
