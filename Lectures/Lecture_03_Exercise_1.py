num_1 = float(input("Enter a number: "))
num_2 = float(input("Enter a number: "))
num_3 = float(input("Enter a number: "))

sum = num_1 + num_2 + num_3

if sum > 100:
    mul = num_1 * num_2
    print("To ginomeno twn aritmwn %.2f kai %.2f isoutai me %.2f." % (num_1, num_2, mul))
else:
   sub = num_2 - num_3
   print("H diafora twn arithmwn %.2f kai %.2f se apoluti timi einai %d." % (num_2, num_3, abs(sub)))