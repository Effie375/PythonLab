# Δημιουργία λίστας
list = [4,8,3,]

for i in range(1,5):
  for j in range(4, i-1, -1):
    if list[j-1] > list[j]:
      temp = list[j-1]
      list[j-1] = list[j]
      list[j] = temp