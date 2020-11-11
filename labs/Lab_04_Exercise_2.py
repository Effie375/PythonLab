sinolo = 0
i = 0

while i < 6:
    bathmos = input("Dwse bathmo: ")
    while not bathmos.isdigit():
        bathmos = input("Dwse ksana bathmo: ")
    bathmos = float(bathmos)
    sinolo = sinolo + bathmos
    i += 1

mesos_oros = (sinolo/6)

if (mesos_oros >= 8.5 and mesos_oros <= 10):
    print("arista me meso oro", mesos_oros)
elif (mesos_oros >= 6.5 and mesos_oros <= 8.49):
    print("lian kalos me meso oro", mesos_oros)
elif (mesos_oros >= 5 and mesos_oros <= 6.49):
    print("kalos me meso oro", mesos_oros)
else:
    print("kopikes")