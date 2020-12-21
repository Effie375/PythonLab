# Diavasma etous
etos = int(input("Dwse etos: "))

#An diaireitai me 4 einai dysekto
if etos % 4 == 0:
  # Ektos an diareitai kai me 100
  if etos % 100 == 0:
    # Alla kai se auth thn periptwsh an diareitai me 400 einai disekto
    if etos % 400 == 0:
      disekto = True
    else:
      disekto = False
  else:
    disekto = True
else:
  disekto = False

# Ektypwsh apotelesmatwn
if disekto:
  print("Einai disekto")
else:
  print("Den einai disekto")