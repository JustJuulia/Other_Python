def zadanie1():
    tablica = []
    with open("liczby.txt", "r") as file:
        for line in file:
            liczba = line.strip()
            if liczba[0] == liczba[-1]:
                tablica.append(liczba)
        return print("pierwsza liczba co ma taka sama liczbe na poczatku i koncu to: ",tablica[0],"a ilosc takich liczba to: ",len(tablica))
def zadanie2():
    dobre_trojki = []
    wszystkie_cyfry = []
    with open("liczby.txt", "r") as file:
        for line in file:
            liczba = line.strip()
            wszystkie_cyfry.append(liczba)
        ilosc = len(wszystkie_cyfry)
        for first_adder in range(ilosc):
            liczba_1 = int(wszystkie_cyfry[first_adder])
            for second_adder in range(ilosc):
                liczba_2 = int(wszystkie_cyfry[second_adder])
                for third_adder in range(ilosc):
                    liczba_3 = int(wszystkie_cyfry[third_adder])
                    if liczba_1 != liczba_2 and liczba_1 != liczba_3 and liczba_2 != liczba_3:
                        if liczba_1 % liczba_2 == 0 and liczba_2 % liczba_3 == 0:
                            dobre_trojki.append({liczba_1, liczba_2, liczba_3})
    with open("trojki.txt", "w") as file:
        for i in range(len(dobre_trojki) - 1):
            file.write(str(dobre_trojki[i]) + "\n")
    return print('dobrych trojek jest: ', len(dobre_trojki))


zadanie1()
zadanie2()