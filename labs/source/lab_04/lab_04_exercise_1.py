# Eisagwgh dedomenwn
zaria1 = input("Dwse 1h zaria: ")
zaria2 = input("Dwse 2h zaria: ")

# Elegxoume an auto pou egrapse o xrhsths einai noumera
if zaria1.isdigit() and zaria2.isdigit():
    # Metatropi apo str se int
    zaria1 = int(zaria1)
    zaria2 = int(zaria2)
    # elegxoume an ta noumera twn zariwn htan metaksi 1 - 6
    if (zaria1 >= 1 and zaria1 <= 6) and (zaria2 >= 1 and zaria2 <= 6):
        if zaria1 == 4 and zaria2 == 4:
            print("Ntortia")
        elif (zaria1 == 1 and zaria2 == 2) or (zaria1 == 2 and zaria2 == 1):
            print("Assodyo")
        elif zaria1 == zaria2:
            print("Diples", zaria1 + zaria2)
        else:
            print(zaria1 + zaria2)
    else:
        print("Error! Giati oi zaries einai ektos orion 1 kai 6?")
else:
    print("Error! Giati egrapses leksi?")
