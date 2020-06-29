# -*- coding: windows-1250 -*-
import random
import zapis_gry
import statystyka
# słownik z modelami szubienicy
szubienica = {

    0: """
    _ _ _ _ _
    |       |
    |
    |
    |
    |
    |
    |_ _ _ _ _ _ """,

    1: """
    _ _ _ _ _
    |       |
    |       O
    |
    |
    |
    |
    |_ _ _ _ _ _ """,

    2: """
    _ _ _ _ _
    |       |
    |       O
    |       |
    |
    |
    |
    |_ _ _ _ _ _ """,

    3: """
    _ _ _ _ _
    |       |
    |       O
    |     / |
    |
    |
    |
    |_ _ _ _ _ _ """,

    4: """
    _ _ _ _
    |       |
    |       O
    |     / | \\
    |
    |
    |
    |_ _ _ _ _ _ """,

    5: """
    _ _ _ _
    |       |
    |       O
    |     / | \\
    |       |
    |
    |
    |_ _ _ _ _ _ """,

    6: """
    _ _ _ _
    |       |
    |       O
    |     / | \\
    |       |
    |      |
    |
    |_ _ _ _ _ _ """,

    7: """
    _ _ _ _
    |       |
    |       O
    |     / | \\
    |       |
    |      | |
    |
    |_ _ _ _ _ _ """,

    8: """
    _ _ _ _
    |       |
    |       O
    |     / | \\
    |       |
    |      | |
    |      |
    |_ _ _ _ _ _ """,

    9: """
    _ _ _ _
    |       |
    |       O
    |     / | \\
    |       |
    |      | |
    |      | |
    |_ _ _ _ _ _ """

}

alfabet = ['a', 'ą', 'b', 'c', 'ć', 'd', 'e', 'ę', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'ł', 'm', 'n', 'ń', 'o', 'ó', 'p', 'r', 's', 'ś', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'ź', 'ż']

def zapisz(data, star_count, correct, incorrect):
    data[2] = str(star_count)
    cnt = ""
    for i in correct:
        cnt += i
    data[3] = cnt
    cnt = ""
    for i in incorrect:
        cnt += i
    data[4] = cnt
    zapis_gry.zapis(data[0], data)
    print("Zapisano stan gry. \n")

# funkcja, która sprawdza, czy litera jest w słowie
def check_word(f_guess, f_word, f_fail_count, f_correct, f_incorrect, f_play, f_clue_index_list):

    # jesli gracz odgadnął zadane słowo:
    if f_guess == f_word:
        print(f_word.upper())
        print("Gratulacje - przeżyłeś!")
        f_play = False                      # KONIEC GRY

    # jeśli gracz wprowadził jedną literę:
    elif len(f_guess) == 1:

        # jeśli już wcześniej próbował odgadnąć tę literę:
        if f_guess in f_correct or f_guess in f_incorrect:
            print("Ta litera już była używana, spróbuj innaczej.")
            # wypisanie liter, które były już poprzednio zgadywane:
            print("\nTu pojawiają się podane przez Ciebie błędne litery i hasła: ", ", ".join(f_incorrect))
            print("-" * 100)

        # litera została wprowadzona po raz pierwszy
        else:
            # zgadywana litera jest w słowie
            if f_guess in f_word:
                f_correct.append(f_guess)
                # nie można zastosować wbudowanej funkcji .index(), bo zwraca ona indeks pierwszego napotkanego,
                # znaku, a potrzebujemy indeksu każdej powtarzającej się litery
                i = 0
                for letter in f_word:
                    if letter == f_guess:
                        if i not in f_clue_index_list:
                            f_clue_index_list.append(i)
                    i += 1
                # sprawdzenie czy odgadnięta litera sprawia, że odgadnięte zostało całe słowo
                # w zbiorach kolejność nie ma znaczenia oraz elementy się nie powtarzają, stąd rzutowanie
                if set(f_word) == set(f_correct):
                    print(f_word)
                    print("Gratulacje - przeżyłeś!")
                    f_play = False

            # zgadywanej litery nie ma w słowie
            else:
                f_incorrect.append(f_guess)
                f_fail_count += 1
                print("Tej litery nie ma w Twoim słowie!")
                print(szubienica[f_fail_count])
                # wypisanie liter, które były już poprzednio zgadywane:
                print("\nTu pojawiają się podane przez Ciebie błędne litery i hasła: ", ", ".join(f_incorrect))
                print("-" * 100)

    # gracz wprowadził kilka liter, ale nie są one zadanym słowem
    else:
        # jeśli już próbował odgadnąć taką kombinację
        if f_guess in f_correct or f_guess in f_incorrect:
            print("Już próbowałeś odgadnąć to słowo, spróbuj inaczej.")
        else:
            f_incorrect.append(f_guess)
            f_fail_count += 1
            print("To nie to słowo!")
            print(szubienica[f_fail_count])
            # wypisanie liter, które były już poprzednio zgadywane:
            print("\nTu pojawiają się podane przez Ciebie błędne litery i hasła: ", ", ".join(f_incorrect))
            print("-" * 100)

    return f_fail_count, f_correct, f_incorrect, f_play


def game(mode, nick, word_, stars_, correct_=[], incorrect_=[], fail_count_=0):
    stats_player = nick
    stats_letters = len(word_)
    stats_stars_used = False
    if stars_ == 3:
        stats_level = "łatwy"
    elif stars_ == 2:
        stats_level = "średni"
    elif stars_ == 1:
        stats_level = "trudny"
    else:
        raise ValueError
    star_count = stars_
    word = word_[:-1].lower()
    correct = correct_
    incorrect = incorrect_
    clue_index_list = []
    play = True
    fail_count = fail_count_
    data = [nick, word, star_count, correct, incorrect]

    # dodanie spacji do haseł, które mają więcej słów
    if " " in word:
        correct.append(" ")
        i = 0
        for letter in word:
            if letter == " ":
                clue_index_list.append(i)
            i += 1

    if mode == "2":
        print("Odgadnięte litery: " + str(correct) + "\n")
        print("Błędne litery: " + str(incorrect) + "\n")
        print("Słowo, które musisz odgadnąć:")
        for underscore in word:
            if underscore not in correct:
                print("_ ", end=" ")
            else:
                print(underscore, end=" ")
        print(" ")


    while (play is True) and (fail_count < 9):
        print("Aby dokonać zapisu stanu gry kliknij:\t ss \n")
        print("Aby wyjść z gry kliknij:\t qq\n")

        # FUNKCJONALNOŚĆ - GWIAZDKA = PODPOWIEDŹ
        clue = False
        if star_count > 0:
            if mode == "1":
                print("Twoje hasło:")
                for letter in word:
                    if letter in correct:
                        print(letter, end=" ")
                    else:
                        print("_ ", end=" ")
            print(" ")
            print("Pozostałe podpowiedzi: " + ("* " * star_count))
            answer = input("Czy chcesz skorzystać z gwiazdki? (t/n)")
            #zamieniłbym na: jeśli chcesz skorzystać z gwiazdki, wprowadź (np) znak
            # kropki- tak żeby nie musieć za każdym razem dawań n, kiedy sie nie chce
            if answer == "t":
                stats_stars_used = True
                # losowanie indeksu litery w słowie:
                while not clue:
                    clue_index = random.randint(0, len(word) - 1)
                    if answer == "ss":
                        print("Gra zapisana, jednak nie będzię ona zaliczona do Twoich statystyk.")
                        zapisz(data, star_count, correct, incorrect)
                    elif answer == "qq":
                        print("Wychodzisz z gry, twoje postępy nie zostaną zapisane.")
                        return 0
                    elif clue_index not in clue_index_list:
                        clue_index_list.append(clue_index)
                        result_clue= check_word(word[clue_index], word, fail_count, correct, incorrect, play, clue_index_list)  # funkcja czy w słowie
                        print("Oto Twoja podpowiedź:")
                        for letter in word:
                            if letter in correct:
                                print(letter, end=" ")
                            else:
                                print("_ ", end=" ")
                        print(" ")
                        print(szubienica[fail_count])
                        # wypisanie liter, które były już poprzednio zgadywane:
                        print("\nTu pojawiają się podane przez Ciebie błędne litery i hasła: ", ", ".join(incorrect))
                        print("-" * 100)
                        star_count -= 1
                        play = result_clue[3]
                        clue = True
            elif answer == "n":
                clue = False

            else:
                print("Podaj 't' lub 'n'.")
                print("-" * 30)
                clue = True
        else:
            print("Twoje hasło:")
            for letter in word:
                if letter in correct:
                    print(letter, end=" ")
                else:
                    print("_ ", end=" ")
            print(" ")
            print("Skończyły Ci się podpowiedzi!")

        # CIĄG DALSZY
        if clue is False:
            init_correct = len(correct)
            guess = input("Zgadnij literę lub hasło: ").lower()
            if guess == "ss":
                zapisz(data, star_count, correct, incorrect)
            elif guess == "qq":
                return 0
            elif guess in alfabet or len(guess) > 1:
                result = check_word(guess, word, fail_count, correct, incorrect, play, clue_index_list)
                if init_correct < len(correct):
                    print("Dobrze, coraz mniej do zgadywania!")
                    for letter in word:
                        if letter in correct:
                            print(letter, end=" ")
                        else:
                            print("_ ", end=" ")
                    print(" ")
                    print(szubienica[fail_count])
                    # wypisanie liter, które były już poprzednio zgadywane:
                    print("\nTu pojawiają się podane przez Ciebie błędne litery i hasła: ", ", ".join(incorrect))
                    print("-" * 100)
                play = result[3]
                fail_count = result[0]
                correct = result[1]             #nie musi w sumie tego być
                incorrect = result[2]           #nie musi w sumie tego być
            elif len(guess) == 1:
                print("Nie podano litery")
                print("-" * 100)

    if fail_count == 9:
        stats_win = 0
        print("Przegrałeś!")
        print("Twoim hasłem było: ", word)  
        stats_mistakes = fail_count
    else:
        stats_win = 1
        stats_mistakes = fail_count
        print("Udało Ci się!")
        if mode == "2":
            zapis_gry.zapis(nick, data)
    if mode =="1":
        statystyka.calc_save_stats(stats_player,stats_win,stats_mistakes,stats_stars_used
                               ,stats_letters,stats_level)
    return 0
