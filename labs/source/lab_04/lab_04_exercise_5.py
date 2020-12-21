athroisma = 0

number = int(input("Δώσε αριθμό: "))

while number != 0:
  tel_pshfio = number % 10
  number = number // 10
  athroisma += tel_pshfio

print("Άθροισμα:", athroisma)