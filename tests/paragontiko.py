'''n = int(input("Dwse enan thetiko arithmo:"))
f = 1
for i in range (2,n+1):
    f = f * i
print(str(n) + "paragontiko = " + str(f))
'''

n = int(input("Dwse enan thetiko arithmo:"))
f = 1
i = 1
while i <= n:
    f = f * i
    i = i + 1
print(str(n),  "paragontiko = " + str(f))
