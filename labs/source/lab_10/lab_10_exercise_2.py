seasons = int(input("Δώσε κύκλους: "))
episodes = int(input("Δώσε επεισόδια άνα κύκλο: "))

thle8eash = []

for i in range(seasons):
    thl_season = []
    for j in range(episodes):
        thl = float(input("Dwse thle8eash gia %dx%d: " % (i+1,j+1)))
        thl_season.append(thl)
    thle8eash.append(thl_season)

maxThlSeason = 0
maxThlEpi = 0
minThlSeason = 0
minThlEpi = 0
maxMO = 0

for i in range(seasons):
    soumaSeason = 0
    for j in range(episodes):
    if thle8eash[i][j] > thle8eash[maxThlSeason][maxThlEpi]:
        maxThlSeason = i
        maxThlEpi = j
    if thle8eash[i][j] < thle8eash[minThlSeason][maxThlEpi]:
        minThlSeason = i
        minThlEpi = j
    soumaSeason += thle8eash[i][j]

if maxMO < soumaSeason:
    maxMO = soumaSeason
    maxMOSeason = i

print("Eπεισόδιο με μέγιστη τηλεθέαση: %dx%d" % (maxThlSeason+1,maxThlEpi+1))
print("Eπεισόδιο με ελάχιστη τηλεθέαση: %dx%d" % (minThlSeason+1,minThlEpi+1))
print("Σεζόν με μεγαλύτερο μέσο όρο τηλεθέασης:", maxMOSeason+1)