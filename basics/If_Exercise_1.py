salary = int(input("Δώσε το μισθό σου: ").strip())

if salary <= 800:
    print(f"Είσαι χαμηλόμισθος.")
elif salary <= 1400:
    print(f"Είσαι μεσαία αμειβόμενος.")
else:
    print(f"Είσαι υψηλόμισθος.")
