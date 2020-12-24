ginomeno = 0
arithmos = 1
flag = False

while arithmos != 0:
    arithmos = input("Δώσε αριθμό: ")
    while not arithmos.isdigit():
        arithmos = input("Είπα δώσε αριθμό: ")
    arithmos = int(arithmos)
    if flag is False and arithmos != 0:
        ginomeno = 1
        flag = True
    if arithmos != 0:
        ginomeno = ginomeno * arithmos

print("Γινόμενο:", ginomeno)
