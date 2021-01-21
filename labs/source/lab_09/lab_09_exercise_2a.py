# Εισαγωγή δεδομένων
seasons = int(input("Δώσε κύκλους: ").strip())
episodes = int(input("Δώσε επεισόδια άνα κύκλο: ").strip())

# Αρχικοποίηση μεταβλητών
thle8eash = []

for i in range(seasons):
    thl_season = []
    for j in range(episodes):
        # Εισαγωγή δεδομένων
        thl = float(input("Δώσε τηλεθέαση %dx%d: " % (i + 1, j + 1)).strip())
        thl_season.append(thl)
    thle8eash.append(thl_season)

# Αρχικοποίηση μεταβλητών
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

# Εκτύπωση αποτελεσμάτων
print(f"Eπεισόδιο με μέγιστη τηλεθέαση: {maxThlSeason+1}x{maxThlEpi+1}")
print(f"Eπεισόδιο με ελάχιστη τηλεθέαση: {minThlSeason+1}x{minThlEpi+1}")
print(f"Σεζόν με μεγαλύτερο μέσο όρο τηλεθέασης: {maxMOSeason+1}")
