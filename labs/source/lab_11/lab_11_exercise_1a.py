# Δεχόμαστε [plithos] ονόματα και τα τοποθετούμε σε λίστα την οποία επιστρέφει
def readNames(plithos):
    onomata = []
    for i in range(plithos):
        onoma = input("Δώσε όνομα:")
        onomata.append(onoma)
    return onomata


def longestName(list):
    maxLength = 0
    for onoma in list:
        if len(onoma) > maxLength:
            maxLength = len(onoma)
    return maxLength


plithos = int(input("Δώσε πλήθος: "))
onomata = readNames(plithos)
x = longestName(onomata)

print(f"Το μακρύτερο όνομα έχει μήκος: {x}")
