max_players = 7
players = []

for i in range(max_players):
    player = input("Δώσε όνομα παίκτη: ")
    players.append(player)

print("Μη ταξινομημένοι παίκτες: %s" % players)

for i in range(len(players)):
    for j in range(len(players)-1,i,-1):
        if players[j-1] < players[j]:
            temp = players[j-1]
            players[j-1]= players[j]
            players[j] = temp

print("Ταξινομημένοι παίκτες: %s" % players)