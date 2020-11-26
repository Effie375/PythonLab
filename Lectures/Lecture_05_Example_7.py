list = [5,7,8,9,3]

key = int(input("Dwse stoixeio pou anazitas: "))

counter = 0
i = 0 

while i < len(list):
    if list[i] == key:
        counter += 1
    i += 1

print("To stoixeio pou anazitas exei eisaxthei %d fores." % counter)    