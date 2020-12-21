lista = []

for i in range(5):
  ypolista = []
  for j in range(10):
    n = int(input("Δώσε αριθμό: "))
    ypolista.append(n)
  lista.append(ypolista)

meg_athroisma = 0

for ypolista in lista:
  athroisma = 0 
  for i in ypolista:
    athroisma += i 
  if athroisma > meg_athroisma:
    meg_athroisma = athroisma 
    meg_lista = ypolista
        
print(meg_lista)