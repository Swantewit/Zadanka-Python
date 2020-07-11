liczba = int(input("Podaj liczbę, którą chcesz poddać działaniu: "))

def silnia(x):
    if x == 1:
        return x
    elif x < 1:
        return str("Wtf. Nie zrobisz silni z ujemnej liczby ani z 0, glupcze")
    else:
        return x*silnia(x-1)

print(silnia(int(liczba)))
print(silnia(int(liczba/2)))
