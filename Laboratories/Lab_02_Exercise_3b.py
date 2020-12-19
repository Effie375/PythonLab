now_year = 2020

my_name = input("Δώσε το όνομά σου: ").strip()
my_age = int(input("Δώσε την ηλικία σου: ").strip())

end_year = 100 + now_year - my_age

print(f"{my_name} το {end_year} θα είναι 100 ετών.")