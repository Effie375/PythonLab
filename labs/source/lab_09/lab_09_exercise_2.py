# Εισαγωγή δεδομένων
seasons = int(input("Δώσε κύκλους: "))
episodes = int(input("Δώσε επεισόδια άνα κύκλο: "))

# Αρχικοποίηση μεταβλητών
thle8eash = []

for i in range(seasons):
    thlSeason = []
    for j in range(episodes):
        # Εισαγωγή δεδομένων
        thl = float(input("Δώσε τηλεθέαση %dx%d: " % (i + 1, j + 1)))
        thlSeason.append(thl)
    thle8eash.append(thlSeason)

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
print("Eπεισόδιο με μέγιστη τηλεθέαση: %dx%d" % (maxThlSeason + 1, maxThlEpi + 1))
print("Eπεισόδιο με ελάχιστη τηλεθέαση: %dx%d" % (minThlSeason + 1, minThlEpi + 1))
print("Σεζόν με μεγαλύτερο μέσο όρο τηλεθέασης:", maxMOSeason + 1)
