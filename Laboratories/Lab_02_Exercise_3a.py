import datetime

def calc_year(age):
    now_year = datetime.datetime.today().year
    return now_year + 100 - age 


my_name = input("Δώσε το όνομα σου: ")

try:
    my_age = int(input("Δώσε την ηλικία σου: "))
except:
    print("Παρακαλώ δώσε ακέραιο αριθμό!")
else:
    end_year = calc_year(my_age)
    print("%s το %d θα είναι 100 ετών." % (my_name, end_year))