list = [5,7,8,9,3]

maxThesi = 0; thesi = 0

for item in list:
    if item > list[maxThesi]:
        maxThesi = thesi
    thesi +=1 
print("H maxThesi me ton 1o tropo:", maxThesi)

for i in range(len(list)):
    if list[i] > list[maxThesi]:
        maxThesi = i
print("H maxThesi me ton 2o tropo:", maxThesi)