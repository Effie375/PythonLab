ginomeno = 0
arithmos = 1
flag = False

while arithmos != 0:
    arithmos = input("Dwse arithmo: ")
    while  not arithmos.isdigit(): 
        arithmos = input("EIPA Dwse arithmo: ")         
    arithmos = int(arithmos)
    if (flag == False):
        if arithmos != 0:
            ginomeno = 1
        flag = True
    if arithmos != 0:
        ginomeno = ginomeno * arithmos

print("Ginomeno: ", ginomeno)

