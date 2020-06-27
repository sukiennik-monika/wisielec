import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data = pd.read_csv('npg_test.csv',header=1)
data = data.drop("Unnamed: 0", axis=1)
data.columns = ["Imię","Ilość rozegranych gier","Ilość odgadniętych słów", "% wygranych gier"
    ,"Suma popełnionych błędów","Średnia ilość błędów na grę","Punkty"]

def pts_rank():
    plt.style.use('ggplot')  # wyswietlenie rankingu punktów wykres
    data_sorted = data.sort_values('Punkty', ascending=False)
    sns.barplot(x=data_sorted['Imię'], y=data_sorted['Punkty'], palette='deep')
    plt.xticks(rotation=30)
    plt.xlabel('Gracz')
    plt.ylabel('Zdobyte punkty')
    plt.show()
def adv_stats():
    pd.set_option("display.max_rows", None, "display.max_columns", None)
    data.columns = ['Name','Games played','Games won','Win ratio %','Mistakes made','Avg mistakes per game','Points']
    print(data)
def your_stats(player = 'Player2'):
    data.columns = ["Imię", "Ilość rozegranych gier", "Ilość odgadniętych słów", "% wygranych gier"
        , "Suma popełnionych błędów", "Średnia ilość błędów na grę", "Punkty"]
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

