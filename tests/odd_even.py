def check_num(_num):
   if _num % 2:
      return 1
   else:
      return 0


num = int(input("Enter a number: "))

if check_num(num):
   print("The", num, "is odd.")
else:
   print("The", num, "is even.")
