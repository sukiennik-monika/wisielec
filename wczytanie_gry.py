from itertools import islice
from Wisielec import mechanizm_gry
import random
ROZMIAR_ZAPISU = 5
plik_profile = open("zapisy_gry.txt", "a+")

def split_word(word):
    return [ch for ch in word if ch != '\n']

def wybor_profilu():

    counter = 0
    with open("zapisy_gry.txt") as f:
        for line in f:
            counter += 1
    print("Wybierz profil: \n")
    for i in range(1, int(counter / ROZMIAR_ZAPISU) + 1):
        with open("zapisy_gry.txt") as fin:
            for line in islice(fin, ROZMIAR_ZAPISU * i - ROZMIAR_ZAPISU, ROZMIAR_ZAPISU * i - (ROZMIAR_ZAPISU - 1)):
                print("Profil {numer}: ".format(numer=i) + line + "\n")
    wybor = int(input("Nr profilu: \n"))

    save_word = 'slowo'
    save_stars = 0
    save_correct_word = 'dobreslowo'
    save_correct = []
    save_incorrect_word = 'zleslowo'
    save_incorrect = []
    save_clue_index_list = []

    with open("zapisy_gry.txt") as fin:
        for line in islice(fin, (wybor - 1) * ROZMIAR_ZAPISU + 1, (wybor - 1) * ROZMIAR_ZAPISU + 2):
            save_word = line
    with open("zapisy_gry.txt") as fin:
        for line in islice(fin, (wybor - 1) * ROZMIAR_ZAPISU + 2, (wybor - 1) * ROZMIAR_ZAPISU + 3):
            save_stars = int(line)
    with open("zapisy_gry.txt") as fin:
        for line in islice(fin, (wybor - 1) * ROZMIAR_ZAPISU + 3, (wybor - 1) * ROZMIAR_ZAPISU + 4):
            save_correct_word = line
        if save_correct_word != 'brak':
            save_correct = split_word(save_correct_word)
        else:
            save_correct = []
    with open("zapisy_gry.txt") as fin:
        for line in islice(fin, (wybor - 1) * ROZMIAR_ZAPISU + 4, (wybor - 1) * ROZMIAR_ZAPISU + 5):
            save_incorrect_word = line
        if save_incorrect_word != 'brak':
            save_incorrect = split_word(save_incorrect_word)
        else:
            save_incorrect = []
    save_fail_count = len(save_incorrect_word) - 1

    print(save_word)
    print(save_correct_word)
    #for letter in save_correct_word:
    #    save_clue_index_list.append(save_word.index(letter))
    #print(save_clue_index_list)

    return [save_word, save_stars, save_correct, save_incorrect, save_fail_count]



def game_save(word_, stars_, correct_,incorrect_, fail_count_):
    star_count = stars_
    # (dostosować do poziomów trudności odpowiednią ilość, po złączeniu plików- pewnie jako argument funkcji- ale to później)
    word = word_
    correct = correct_
    incorrect = incorrect_
    clue_index_list = []
    play = True
    fail_count = fail_count_
    print("Słowo, które musisz odgadnąć:")
    for underscore in word:
        print("_ ", end=" ")
    print(" ")

    while (play is True) and (fail_count < 9):

        # FUNKCJONALNOŚĆ - GWIAZDKA = PODPOWIEDŹ
        clue = False
        if star_count > 0:
            print("Pozostałe podpowiedzi: " + ("* " * star_count))
            answer = input("Czy chcesz skorzystać z podpowiedzi? (*/n): ")
            # zamieniłbym na: jeśli chcesz skorzystać z gwiazdki, wprowadź (np) znak
            # kropki- tak żeby nie musieć za każdym razem dawań n, kiedy sie nie chce
            if answer == "*":
                # losowanie indeksu litery w słowie:
                while not clue:
                    clue_index = random.randint(0, len(word) - 1)
                    if clue_index not in clue_index_list:
                        clue_index_list.append(clue_index)
                        mechanizm_gry.check_word(word[clue_index], word, fail_count, correct, incorrect, play,
                                   clue_index_list)  # funkcja czy w słowie
                        star_count -= 1
                        play = result[3]
                        clue = True
            elif answer == "n":
                clue = False
            else:
                print("Podaj '*' lub 'n'.")
                print("-" * 30)
                clue = True
        else:
            print("Skończyły Ci się podpowiedzi!")
            # WAŻNE jeśli rozegrasz grę tak, żeby w momencie wygranej skończyły Ci się wszystkie gwaizdki, tj twoja ostatnia
            # litera zostaje odsłonięta dzięki gwiazdce to gra się nie kończy- wyświetla się komunikat o braku gwiazdek i gra
            # trwa dalej pomimo tego że hasło już zostało zgadnięte. Muszisz pokombinować z tymi elif, else if itd.

        # CIĄG DALSZY
        if clue is False:
            guess = input("Zgadnij literę lub słowo: ").lower()
            result = mechanizm_gry.check_word(guess, word, fail_count, correct, incorrect, play, clue_index_list)
            play = result[3]
            fail_count = result[0]
            correct = result[1]  # nie musi w sumie tego być
            incorrect = result[2]  # nie musi w sumie tego być

    if fail_count == 9:
        print("Przegrałeś!")
        print("Twoim hasłem było: ", word)
    else:
        print("Udało Ci się!")

    return 0