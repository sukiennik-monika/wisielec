import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data = pd.read_csv('C:/Users/Bartek/Desktop/STUDIA/npg/projekt/npg_test.csv',header=1)
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
    if player not in data['Imię']:
        print('Nie rozegrałeś jeszcze żadnych gier- kiedy ukończysz choć jedną grę, twoje statystyki się tu pojawią')
    else:
        for name in data['Imię']:
            if name != player:
                i += 1
                continue
            break
        print(data.iloc[i, :])