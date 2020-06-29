import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from csv import writer

def pts_rank():
    data = pd.read_csv('npg_test.csv', header=0)
    data.columns = ["Imię", "Ilość rozegranych gier", "Ilość odgadniętych słów", "% wygranych gier"
        , "Suma popełnionych błędów", "Średnia ilość błędów na grę", "Punkty"]
    plt.style.use('ggplot')  # wyswietlenie rankingu punktów wykres
    data_sorted = data.sort_values('Punkty', ascending=False)
    sns.barplot(x=data_sorted['Imię'], y=data_sorted['Punkty'], palette='deep')
    plt.xticks(rotation=30)
    plt.xlabel('Gracz')
    plt.ylabel('Zdobyte punkty')
    plt.show()
def adv_stats():
    data = pd.read_csv('npg_test.csv', header=0)
    pd.set_option("display.max_rows", None, "display.max_columns", None)
    data.columns = ['Name','Games played','Games won','Win ratio %','Mistakes made','Avg mistakes per game','Points']
    print(data)
def your_stats():
    data = pd.read_csv('npg_test.csv', header=0)
    data.columns = ["Imię", "Ilość rozegranych gier", "Ilość odgadniętych słów", "% wygranych gier"
        , "Suma popełnionych błędów", "Średnia ilość błędów na grę", "Punkty"]
    print("Wybierz profil, którego statystyki chcesz zobaczyć:")
    for player in data['Imię']:
        print(player)
    player = str(input())
    i = 0
    for player_loop in data['Imię']:
        if player == player_loop:
            for name in data['Imię']:
                if name != player:
                    i += 1
                    continue
                break
            print(data.iloc[i, :])
        else:
            continue
    if i == 0 and player != data.iloc[0,0]:
        print("Twoje wyniki nie znajdują się jeszcze w bazie danych. Rozegraj choć jeden mecz, a twoje statystki "
              "się tu pojawią")

def append_list_as_row(file_name, list_of_elem):
    # Open file in append mode
    with open(file_name, 'a+', newline='') as write_obj:
        # Create a writer object from csv module
        write_obj.write('\n')
        csv_writer = writer(write_obj)
        # Add contents of list as last row in the csv file
        csv_writer.writerow(list_of_elem)

def calc_save_stats(player, win, mistakes, star_used, letters,level):
    data = pd.read_csv('npg_test.csv', header=0)
    # obliczanie pkt za grę
    points = 5 * letters
    if win == 1:
        points += 25
    if star_used == False:
        points += 20
    if level == 'łatwy':
        pass
    elif level == 'średni':
        points = points * 1.5
    elif level == 'łatwy':
        points = points * 2
    stat = [player, win, mistakes, points]
    sprawdzacz = 0
    ktory_gracz=0
    for player in data['name']:
        if player == stat[0]:   #update statystyk dla gracza, który już kiedyś grał
            data.loc[ktory_gracz,'games played'] += 1
            data.loc[ktory_gracz,'games won'] += stat[1]
            data.loc[ktory_gracz,'win ratio'] = str(round(data.loc[ktory_gracz,'games won'] /
                                                    data.loc[ktory_gracz,'games played'] * 100,2))+"%"
            data.loc[ktory_gracz,'mistakes total'] += stat[2]
            data.loc[ktory_gracz,'avg mistakes'] = round(data.loc[ktory_gracz,'mistakes total'] /
                                                         data.loc[ktory_gracz,'games played'],1)
            data.loc[ktory_gracz,'points'] += round(stat[3],0)
            data.to_csv('npg_test.csv',index=False,header=1)
            sprawdzacz +=1
        ktory_gracz +=1
    if sprawdzacz == 0 : #wpisanie do statystyk nowego profilu
        dane_do_zapisu = [stat[0],1,stat[1],stat[1]*100,stat[2],stat[2],stat[3]]
        append_list_as_row('npg_test.csv', dane_do_zapisu)








