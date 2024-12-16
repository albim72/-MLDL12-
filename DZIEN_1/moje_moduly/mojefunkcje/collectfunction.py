def czytaj_liste(lista):
    print("Elementy listy: ")
    for i,j in enumerate(lista):
        print(f"numer indeksu elemnetu listy: {i}, wartośc: {j}")
    print("_" *60)


def czytaj_slownik(slownik):
    print("Elementy słownika: ")
    for x,y in slownik.items():
        print(f"element -> {x}: {y}")
    print("_" * 60)

