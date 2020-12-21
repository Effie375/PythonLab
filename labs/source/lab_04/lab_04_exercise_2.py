i = 0
athroisma = 0

while i< 6:
  vathmos = int(input("Dwse vathmo: "))
  athroisma = athroisma + vathmos
  i = i + 1

mo = athroisma / 6

if mo > 10:
  print("Kati den paei kala...")
elif mo >= 8.5:
  print("Arista!")
elif mo >= 6.5:
  print("Lian Kalws")
elif mo >= 5:
  print("Kalws")
else:
  print("Kophkes")