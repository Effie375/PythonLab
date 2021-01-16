def eisagogiStoixeion():
  onomata = []
  for i in range (10):
    name = input("Δώσε όνομα: ").strip()
    onomata.append(name)

  return onomata


def monadikiLista(lista):
  neaLista = []
  for i in lista:
    if i not in neaLista:
      neaLista.append(i)

  return neaLista


def anazitisi(key, lista):
  done = True
  for i in lista:
    if i == key:
      done = False

  return done

onomata = eisagogiStoixeion()

print(monadikiLista(onomata))

stoixeio = input("Δώσε όνομα που αναζητάς: ").strip()

done = anazitisi(stoixeio, onomata)

if done == True:
  print("Το όνομα που αναζητάς δεν είναι στη λίστα.")
else:
  print(f"Το όνομα {stoixeio}είναι στη λίστα.")
