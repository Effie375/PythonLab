num_1 = float(input("Δώσε έναν αριθμό: ").strip())
num_2 = float(input("Δώσε έναν αριθμό: ").strip())
num_3 = float(input("Δώσε έναν αριθμό: ").strip())

sum = num_1 + num_2 + num_3

if sum > 100:
    mul = num_1 * num_2
    print("Το γινόμενο ισούται με %.2f." % mul)
else:
    sub = num_2 - num_3
    print("Η διαφορά των αριθμών σε απόλυτη τιμή είναι %d." % abs(sub))
