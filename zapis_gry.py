from itertools import islice
ROZMIAR_ZAPISU = 5
plik_profile = open("zapisy_gry.txt", "a")

def split_word(word):
    return [ch for ch in word if ch != '\n']

def wybor_profilu():

    counter = 0
    with open("zapisy_gry.txt") as f:
        for line in f:
            counter += 1

    if (counter - 1) % ROZMIAR_ZAPISU != 0:
        print("Usuwam niekompletny zapis. \n")

    print("Wybierz profil: \n")
    for i in range(1, int(counter / ROZMIAR_ZAPISU) + 1):
        with open("zapisy_gry.txt") as fin:
            for line in islice(fin, ROZMIAR_ZAPISU * i - ROZMIAR_ZAPISU, ROZMIAR_ZAPISU * i - (ROZMIAR_ZAPISU - 1)):
                print("Profil {numer}: ".format(numer=i) + line + "\n")
    wybor = int(input("Nr profilu: \n"))

    save_nick = 'nick'
    save_word = 'slowo'
    save_stars = 0
    save_correct_word = 'dobreslowo'
    save_correct = []
    save_incorrect_word = 'zleslowo'
    save_incorrect = []
    save_clue_index_list = []

    with open("zapisy_gry.txt") as fin:
        for line in islice(fin, (wybor - 1) * ROZMIAR_ZAPISU, (wybor - 1) * ROZMIAR_ZAPISU + 1):
            save_nick = line
    with open("zapisy_gry.txt") as fin:
        for line in islice(fin, (wybor - 1) * ROZMIAR_ZAPISU + 1, (wybor - 1) * ROZMIAR_ZAPISU + 2):
            save_word = line
    with open("zapisy_gry.txt") as fin:
        for line in islice(fin, (wybor - 1) * ROZMIAR_ZAPISU + 2, (wybor - 1) * ROZMIAR_ZAPISU + 3):
            save_stars = int(line)
    with open("zapisy_gry.txt") as fin:
        for line in islice(fin, (wybor - 1) * ROZMIAR_ZAPISU + 3, (wybor - 1) * ROZMIAR_ZAPISU + 4):
            save_correct_word = line
        if save_correct_word != "":
            save_correct = split_word(save_correct_word)
        else:
            save_correct = []
    with open("zapisy_gry.txt") as fin:
        for line in islice(fin, (wybor - 1) * ROZMIAR_ZAPISU + 4, (wybor - 1) * ROZMIAR_ZAPISU + 5):
            save_incorrect_word = line
        if save_incorrect_word != "":
            save_incorrect = split_word(save_incorrect_word)
        else:
            save_incorrect = []
    save_fail_count = len(save_incorrect_word) - 1


    #for letter in save_correct_word:
    #    save_clue_index_list.append(save_word.index(letter))
    #print(save_clue_index_list)
    print(save_word)
    return [save_nick, save_word, save_stars, save_correct, save_incorrect, save_fail_count]

def zapis(nickname, save):
    if nickname is not save[0]:
        print("Brak zapisu o podanym nicku \n")
        raise ValueError

    zapisy = open("zapisy_gry.txt", 'r')
    lines = zapisy.readlines()
    zapisy.close()
    line_index = 0

    if (nickname + "\n") in lines:
        for line in lines:
            if (nickname + "\n") == line:
                line_index = int(lines.index(line))

        lines = lines[:line_index] + lines[(line_index + 5):]
        save = [line + "\n" for line in save]
        lines += save

    else:
        save = [line + "\n" for line in save]
        lines += save


    zapisy = open("zapisy_gry.txt", "w")
    zapisy.writelines(lines)
    zapisy.close()