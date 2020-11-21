sum = 0

num = int(input("Enter a number: ")) 

while num:
   digit = num % 10
   num /= 10 
   sum += digit

print("The sum of the digits are %d." % sum)