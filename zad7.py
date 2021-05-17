#Zad.7 Do poszczególnych elementów łańcucha możemy się odwoływać przez podanie indeksu.
# Np. pierwszy znak zapisany w zmiennej imie uzyskamy przez imie[0].
# Zapisz dowolną zmienną łańcuchową i wyświetl jej
# drugą i ostatnią literę, wykorzystując indeksy.

#Kacper Strzemieczny 162334

wyraz1 = "kacper"
wyraz2 = "strzemieczny"

i = 1

while i < len(wyraz1):
  print(i)
  i += 1

i = i-1

print(wyraz1[1] + wyraz1[i])
print(wyraz2[1] + wyraz2[i])