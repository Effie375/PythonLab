while(True):
    vathmos = int(input("Βάλε βαθμό (999 τέλος): "))
    if((vathmos >= 0 and vathmos <= 10) or (vathmos == 999)):
        break;

while(vathmos != 999):
    if(vathmos > 7):
        print("Άριστα")
    elif(vathmos > 4):
        print("Καλά")
    else:
        print("Κόβεται")
    while(True):
        vathmos = int(input("Βάλε βαθμό (999 τέλος): "))
        if((vathmos >= 0 and vathmos <= 10) or (vathmos == 999)):
            break;

print("Τέλος!")
