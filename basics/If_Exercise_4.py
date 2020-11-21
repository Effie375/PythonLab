car_displacement = int(input("How much displacement does your car has? "))

if car_displacement <= 1100:
    print("The tax corresponds to 100€.\n")
elif car_displacement <= 1400:
    print("The tax corresponds to 150€.\n")
elif car_displacement <= 2000:
    print("The tax corresponds to 225€.\n")
else:
    print("The tax corresponds to 600€.\n")
