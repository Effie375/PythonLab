team_a = input("Δώσε τους πόντους της πρώτης ομάδας: ").strip()
team_b = input ("Δώσε τους πόντους της δεύτερης ομάδας: ").strip()

if not(team_a.isdigit() and team_b.isdigit()):
    team_a = input("Παρακαλώ δώσε τους πόντους της πρώτης ομάδας: ").strip()
    team_b = input ("Παρακαλώ δώσε τους πόντους της πρώτης ομάδας: ").strip()

team_a = int(team_a)
team_b = int(team_b)

if team_a == 25:
    print("Η πρώτη ομάδα είναι νικήτρια!")
else:
    print("Η δεύτερη ομάδα είναι νικήτρια!")
