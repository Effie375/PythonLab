team_a = input("Enter the points of the first team: ")
team_b = input ("Enter the points of the second team: ")


if not(team_a.isdigit() and team_b.isdigit()):
    team_a = input("Please enter the points of the first team: ")
    team_b = input ("Please enter the points of the second team: ")

team_a = int(team_a)
team_b = int(team_b)

if team_a == 25:
    print("\nThe first team is the winner!")
else:
    print("\nThe second team is the winner!")
