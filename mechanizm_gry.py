# -*- coding: windows-1250 -*-
import random

# s�ownik z modelami szubienicy
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

alfabet = ['a', '�', 'b', 'c', '�', 'd', 'e', '�', 'f', 'g', 'h', 'i', 'j', 'k', 'l', '�', 'm', 'n', '�', 'o', '�', 'p', 'r', 's', '�', 't', 'u', 'v', 'w', 'x', 'y', 'z', '�', '�']

# funkcja, kt�ra sprawdza, czy litera jest w s�owie
def check_word(f_guess, f_word, f_fail_count, f_correct, f_incorrect, f_play, f_clue_index_list):

    # jesli gracz odgadn�� zadane s�owo:
    if f_guess == f_word:
        print(f_word.upper())
        print("Gratulacje - prze�y�e�!")
        f_play = False                      # KONIEC GRY

    # je�li gracz wprowadzi� jedn� liter�:
    elif len(f_guess) == 1:

        # je�li ju� wcze�niej pr�bowa� odgadn�� t� liter�:
        if f_guess in f_correct or f_guess in f_incorrect:
            print("Ta litera ju� by�a u�ywana, spr�buj innaczej.")
            # wypisanie liter, kt�re by�y ju� poprzednio zgadywane:
            print("\nTu pojawiaj� si� podane przez Ciebie b��dne litery i has�a: ", ", ".join(f_incorrect))
            print("-" * 100)

        # litera zosta�a wprowadzona po raz pierwszy
        else:
            # zgadywana litera jest w s�owie
            if f_guess in f_word:
                f_correct.append(f_guess)
                # nie mo�na zastosowa� wbudowanej funkcji .index(), bo zwraca ona indeks pierwszego napotkanego,
                # znaku, a potrzebujemy indeksu ka�dej powtarzaj�cej si� litery
                i = 0
                for letter in f_word:
                    if letter == f_guess:
                        if i not in f_clue_index_list:
                            f_clue_index_list.append(i)
                    i += 1
                # sprawdzenie czy odgadni�ta litera sprawia, �e odgadni�te zosta�o ca�e s�owo
                # w zbiorach kolejno�� nie ma znaczenia oraz elementy si� nie powtarzaj�, st�d rzutowanie
                if set(f_word) == set(f_correct):
                    print(f_word)
                    print("Gratulacje - prze�y�e�!")
                    f_play = False

            # zgadywanej litery nie ma w s�owie
            else:
                f_incorrect.append(f_guess)
                f_fail_count += 1
                print("Tej litery nie ma w Twoim s�owie!")
                print(szubienica[f_fail_count])
                # wypisanie liter, kt�re by�y ju� poprzednio zgadywane:
                print("\nTu pojawiaj� si� podane przez Ciebie b��dne litery i has�a: ", ", ".join(f_incorrect))
                print("-" * 100)

    # gracz wprowadzi� kilka liter, ale nie s� one zadanym s�owem
    else:
        # je�li ju� pr�bowa� odgadn�� tak� kombinacj�
        if f_guess in f_correct or f_guess in f_incorrect:
            print("Ju� pr�bowa�e� odgadn�� to s�owo, spr�buj inaczej.")
        else:
            f_incorrect.append(f_guess)
            f_fail_count += 1
            print("To nie to s�owo!")
            print(szubienica[f_fail_count])
            # wypisanie liter, kt�re by�y ju� poprzednio zgadywane:
            print("\nTu pojawiaj� si� podane przez Ciebie b��dne litery i has�a: ", ", ".join(f_incorrect))
            print("-" * 100)

    return f_fail_count, f_correct, f_incorrect, f_play


def game(word_, stars):
    star_count = stars
    #(dostosowa� do poziom�w trudno�ci odpowiedni� ilo��, po z��czeniu plik�w- pewnie jako argument funkcji- ale to p�niej)
    word = word_[:-1]
    correct = []
    incorrect = []
    clue_index_list = []
    play = True
    fail_count = 0
    # guess_count = 0        EW. DO STATYSTYK

    # dodanie spacji do hase�, kt�re maj� wi�cej s��w
    if " " in word:
        correct.append(" ")
        i = 0
        for letter in word:
            if letter == " ":
                clue_index_list.append(i)
            i += 1

    while (play is True) and (fail_count < 9):

        # FUNKCJONALNO�� - GWIAZDKA = PODPOWIED�
        clue = False
        if star_count > 0:
            print("Twoje has�o:")
            for letter in word:
                if letter in correct:
                    print(letter, end=" ")
                else:
                    print("_ ", end=" ")
            print(" ")
            print("Pozosta�e podpowiedzi: " + ("* " * star_count))
            answer = input("Czy chcesz skorzysta� z gwiazdki? (t/n)")
            #zamieni�bym na: je�li chcesz skorzysta� z gwiazdki, wprowad� (np) znak
            # kropki- tak �eby nie musie� za ka�dym razem dawa� n, kiedy sie nie chce
            if answer == "t":
                # losowanie indeksu litery w s�owie:
                while not clue:
                    clue_index = random.randint(0, len(word) - 1)
                    if clue_index not in clue_index_list:
                        clue_index_list.append(clue_index)
                        result_clue= check_word(word[clue_index], word, fail_count, correct, incorrect, play, clue_index_list)  # funkcja czy w s�owie
                        print("Oto Twoja podpowied�:")
                        for letter in word:
                            if letter in correct:
                                print(letter, end=" ")
                            else:
                                print("_ ", end=" ")
                        print(" ")
                        print(szubienica[fail_count])
                        # wypisanie liter, kt�re by�y ju� poprzednio zgadywane:
                        print("\nTu pojawiaj� si� podane przez Ciebie b��dne litery i has�a: ", ", ".join(incorrect))
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
            print("Twoje has�o:")
            for letter in word:
                if letter in correct:
                    print(letter, end=" ")
                else:
                    print("_ ", end=" ")
            print(" ")
            print("Sko�czy�y Ci si� podpowiedzi!")

        # CI�G DALSZY
        if clue is False:
            init_correct = len(correct)
            guess = input("Zgadnij liter� lub has�o: ").lower()
            if guess in alfabet or len(guess) > 1:
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
                    # wypisanie liter, kt�re by�y ju� poprzednio zgadywane:
                    print("\nTu pojawiaj� si� podane przez Ciebie b��dne litery i has�a: ", ", ".join(incorrect))
                    print("-" * 100)
                play = result[3]
                fail_count = result[0]
                correct = result[1]             #nie musi w sumie tego by�
                incorrect = result[2]           #nie musi w sumie tego by�
            elif len(guess) == 1:
                print("Nie podano litery")
                print("-" * 100)

    if fail_count == 9:
        print("Przegra�e�!")
        print("Twoim has�em by�o: ", word)
    '''else:
        print("Uda�o Ci si�!")'''

    return 0