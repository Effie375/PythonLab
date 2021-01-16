num_1 = float(input("Δώσε έναν αριθμό: ").strip())
num_2 = float(input("Δώσε έναν αριθμό: ").strip())
num_3 = float(input("Δώσε έναν αριθμό: ").strip())

sum = num_1 + num_2 + num_3

if sum > 100:
    mul = num_1 * num_2
    print(f"Το γινόμενο ισούται με {mul:.2f}.")
else:
    sub = num_2 - num_3
    print(f"Η διαφορά των αριθμών σε απόλυτη τιμή είναι {abs(sub)}.")
