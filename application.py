import Engine


def main():
    is_game_alive = True
    engine = Engine.Engine()
    menu_options = {
        1: "Nowa gra",
        2: "Zasady gry",
        3: "Ustawienia gry",
        4: "Zakończ grę"
    }
    while is_game_alive:
        print_options(menu_options)
        try:
            chosen_option = int(input("Wybierz opcję: "))
        except Exception as e:
            print("Wpisz numer...")
            continue
        if chosen_option == 1:
            stats = engine.run()
            to_print = str(input("Czy chcesz zapisać wynik rundy do pliku? [y/n]: "))
            if to_print == 'y':
                write_to_file(stats)
            else:
                print("Wyniki rozgrywki:")
                print(stats)

        elif chosen_option == 2:
            rules()
        elif chosen_option == 3:
            settings(engine)
        elif chosen_option == 4:
            is_game_alive = False
        else:
            print("Wpisz numer w przedziale 1-4")


def print_options(collection):
    for opt in collection.keys():
        print(f"{opt}---{collection[opt]}")


def rules():
    print("Tekstowa gra w której komputer (Host) losuje słowo, które jest izogramem \n"
          "(izogram jest to wyraz w którym nie powtarzają się żadne litery) i informuje użytkownika (Guesser)"
          " o ilości liter w słowie.\nUżytkownik (Guesser) stara się zgadnąć co to za słowo. Komputer (Host) po"
          "każdej próbie zwraca liczbę Bulls & Cows.\nLiczba przy słowie Cows oznacza literę występującą"
          "w słowie lecz na złej pozycji,"
          " liczba przy słowie Bulls oznacza na poprawną literę i pozycję.\nGra kończy się kiedy "
          "liczba przy Bulls będzie taka sama jak długość"
          " słowa wylosowanego przez komputer.")


def choose_difficulty_level(engine):
    options = {
        1: "łatwy",
        2: "średni",
        3: "trudny"
    }
    print_options(options)
    try:
        level = int(input("Wybierz poziom trudności: "))
    except Exception as e:
        print("Wpisz numer...")
        return
    if level not in options.keys():
        print("Aby zmienić poziom trudności wpisz numer w przedziale 1-3")
    else:
        engine.difficulty = level


def set_attempts(engine):
    try:
        attempts = int(input("Wybierz ilość prób: "))
    except Exception as e:
        print("Wpisz numer...")
        return
    if attempts <= 0:
        print("Ilość prób musi być większa od zera")
    else:
        engine.attempts = attempts


def settings(engine):
    options = {
        1: "Poziom trudności",
        2: "Ilość prób",
        3: "Wyjdź z ustawień"
    }
    is_in_settings = True
    while is_in_settings:
        print_options(options)
        try:
            setting = int(input("Wybierz opcję: "))
        except Exception as e:
            print("Wpisz numer...")
            continue
        if setting == 1:
            choose_difficulty_level(engine)
        elif setting == 2:
            set_attempts(engine)
        elif setting == 3:
            is_in_settings = False
        else:
            print("Wpisz numer w przedziale 1-3")


def write_to_file(stats):
    try:
        with open("highscores.txt", 'a') as file:
            file.write(f"Wyniki rozgrywki:\n")
            for stat in stats:
                file.write(f"{stat}\n")
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
