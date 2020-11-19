ginomeno = 1 
arithmos = 1 

while arithmos != 0: 
    arithmos = input("Dwse arithmo: ") 
    while  not arithmos.isdigit(): 
        arithmos = input("EIPA Dwse arithmo: ")         
    arithmos = int(arithmos)    
    if arithmos != 0: 
        ginomeno = ginomeno * arithmos 

print("Ginomeno: ", ginomeno)
