def menu():
    print(f"Wybierz opcje")
    print(f"1. Utworz haslo")
    print(f"2. Wpisz haslo")
    print(f"0. Wyjdz")


option = -1
menu()
while option != 0:
    option = int(input("Wybor :"))
    if option == 0:
        print("Wyjscie")
        break

    elif option == 1:
        dane = input("Podaj haslo do zapisania")

        with open("baza_danych.txt", "w", encoding="utf-8") as baza_danych:
            baza_danych.write(dane)
        print("Hasło zostało zapisane")

    elif option == 2:

        with open("baza_danych.txt", "r", encoding="utf-8") as baza_danych:
                baza_danych = baza_danych.read()
                podane_haslo = input("Wpisz haslo: ")




        if baza_danych == podane_haslo:
            print("Haslo prawidlowe")
        else:
            print("Haslo bledne")
            menu()