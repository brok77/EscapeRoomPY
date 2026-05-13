print("=== ESCAPE ROOM ===")
print("Budzisz się w zamkniętym pokoju...")
print("Musisz znaleźć kod i uciec.\n")

klucz = False
kod = False

while True:

    print("\nCo chcesz zrobić?")
    print("1 - Sprawdź biurko")
    print("2 - Otwórz szafkę")
    print("3 - Włącz komputer")
    print("4 - Sprawdź drzwi")
    print("5 - Pokaż ekwipunek")
    print("6 - Zakończ grę")

    wybor = input("\nTwój wybór: ")

    # BIURKO
    if wybor == "1":
        print("\nW biurku znajdujesz kartkę.")
        print("Jest na niej napis:")
        print("'Hasło do komputera: PYTHON'")

    # SZAFKA
    elif wybor == "2":

        if klucz == False:

            if kod == True:
                print("\nWpisujesz kod do szafki...")
                print("Szafka się otworzyła!")
                print("Znalazłeś klucz!")
                klucz = True

            else:
                print("\nSzafka jest zamknięta.")
                print("Potrzebujesz kodu.")

        else:
            print("\nSzafka jest już pusta.")

    # KOMPUTER
    elif wybor == "3":

        if kod == False:

            haslo = input("\nPodaj hasło do komputera: ")

            if haslo == "PYTHON":
                print("\nHasło poprawne!")
                print("Na ekranie pojawia się kod do szafki: 1440")
                kod = True

            else:
                print("\nBłędne hasło!")

        else:
            print("\nKomputer jest już odblokowany.")

    # DRZWI
    elif wybor == "4":

        if klucz == True:
            print("\nUżywasz klucza...")
            print("Drzwi się otwierają!")
            print("UCIEKŁEŚ Z POKOJU!")
            print("WYGRANA!")
            break

        else:
            print("\nDrzwi są zamknięte.")
            print("Musisz znaleźć klucz.")

    # EKWIPUNEK
    elif wybor == "5":

        print("\n=== EKWIPUNEK ===")

        if klucz == True:
            print("- Klucz")
        else:
            print("- Brak klucza")

        if kod == True:
            print("- Kod do szafki")
        else:
            print("- Brak kodu")

    # WYJŚCIE
    elif wybor == "6":
        print("\nKoniec gry.")
        break

    # BŁĘDNY WYBÓR
    else:
        print("\nNiepoprawny wybór!")