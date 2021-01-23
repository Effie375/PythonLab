vathmos = int(input("Βάλε βαθμό (999 τέλος): ").strip())

while(vathmos != 999):
    if(vathmos > 7):
        print("Άριστα")
    elif(vathmos > 4):
        print("Καλά")
    else:
        print("Κόβεται")
    vathmos = int(input("Βάλε βαθμό (999 τέλος): ").strip())

print("Τέλος")
