def find_max(number_1, number_2):
    max_number = number_2
    if number_1 > number_2:
        max_number = number_1
    return max_number


num1 = int(input("Δώσε έναν αριθμό: ").strip())
num2 = int(input("Δώσε άλλον έναν αριθμό: ").strip())

max_num = find_max(num1, num2)

print(f"Ο μεγαλύτερος αριθμός είναι: {max_num}")
