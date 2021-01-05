salary = int(input("Δώσε το μισθό σου: ").strip())

if salary <= 800:
    print("Είσαι χαμηλόμισθος.")
elif salary <= 1400:
    print("Είσαι μεσαία αμειβόμενος.")
else:
    print("Είσαι υψηλόμισθος.")
