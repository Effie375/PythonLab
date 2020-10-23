# Askisi 3a

import datetime

name = input("Dwse to onoma sou: ")
age = int(input("Dwse tin ilikia sou: "))
year = datetime.datetime.today().year

x = 100 - age
y = year + x
print("O/H ", name, "to etos ", y, " tha einai 100 xronon.")
