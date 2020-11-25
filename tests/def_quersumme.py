def quersumme(num):
    qs = 0
    while(num>0):
        qs += num % 10
        num = num // 10
    return qs

num = int(input("Enter a number: "))

qs = num

while(qs >= 10):
    qs = quersumme(qs)

print("Quersumme:", qs)