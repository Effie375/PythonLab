protasi = input("Γράψε μία πρόταση: ")

count = 0

for i in protasi:
    if i == " ":
        count += 1

print(count)
