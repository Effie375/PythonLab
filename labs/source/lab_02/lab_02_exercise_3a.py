import datetime


def calc_year(age):
    now_year = datetime.datetime.today().year
    return now_year + 100 - age


my_name = input("Δώσε το όνομα σου: ").strip()

try:
    my_age = int(input("Δώσε την ηλικία σου: ").strip())
except ValueError:
    print("Παρακαλώ δώσε ακέραιο αριθμό!")
else:
    end_year = calc_year(my_age)
    print(f"{my_name} το {end_year} θα είναι 100 ετών.")
