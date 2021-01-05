first_attempt = float(input("Πόσα μέτρα πήδηξες την 1η φορά; ").strip())
second_attempt = float(input("Πόσα μέτρα πήδηξες την 2η φορά; ").strip())
third_attempt = float(input("Πόσα μέτρα πήδηξες την 3η φορά; ").strip())

average = (first_attempt + second_attempt + third_attempt) / 3

print(f"Ο μέσος όρος είναι {average:.2f} μέτρα.")

if average > 8:
    print("Προκριθήκατε στον επόμενο αγώνα!")
