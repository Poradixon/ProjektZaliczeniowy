
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import skew, kurtosis

data = pd.read_csv('manhattan.csv')


# Dane do wykresu powierzchnia a cena wynajmu
x1 = data['size_sqft']
y1 = data['rent']

#Dane do wykresu ilosc lazienek w mieszkaniach
liczby_zaleznosci = data['bathrooms'].value_counts()
x2 = liczby_zaleznosci.index
y2 = liczby_zaleznosci.values

#Dane do wykresu ilosc sypialni w mieszkaniach
liczby_zaleznosci = data['bedrooms'].value_counts()
x3 = liczby_zaleznosci.index
y3 = liczby_zaleznosci.values


plt.bar(x1, y1)
plt.xticks(range(min(x1), max(x1)+1, 500))
plt.xlim(right=max(x1))
plt.xlabel('Powierzchnia')
plt.ylabel('Cena')
plt.title('Wykres przedstawiający powierzchnie mieszkania a cene wynajmu')

plt.subplot(1,2,1)
plt.bar(x2,y2)
plt.xlabel('Ilość łazienek')
plt.ylabel('Ilość mieszkań')
plt.title('Ilość mieszkań posiadających daną ilość łazienek')

plt.subplot(1,2,2)
plt.bar(x3,y3)
plt.xlabel('Ilość sypialni')
plt.ylabel('Ilość mieszkań')
plt.title('Ilość mieszkań posiadających daną ilość sypialni')

plt.tight_layout()

#Aby wykresy były dobrze widoczne, nalezy wyświetlić je na całym ekranie. Kod ponizej powzwala na to, natomiast rózni sie on w zaleznosci od systemu operacyjnego.

#Dla Windows
#mng = plt.get_current_fig_manager()
#mng.window.state('zoomed')

#Dla MacOS
# mng = plt.get_current_fig_manager()
#mng.full_screen_toggle()

#Aby uzyskac lepsze rezultaty zachecam do odkomentowania odpowiedniego kawalku kodu przed uruchomieniem skryptu
plt.show()

#Statystyki opisowe

def oblicz_statystyki_opisowe(wektor):
    statystyki = {
        'liczba obserwacji': len(wektor),
        'srednia': np.mean(wektor),
        'odchylenie standardowe': np.std(wektor),
        'wspolczynnik zmiennosci': (np.std(wektor) / np.mean(wektor)) * 100,
        'minimum': np.min(wektor),
        '10 percentyl': np.percentile(wektor, 10),
        '1 kwartyl': np.percentile(wektor, 25),
        'mediana': np.median(wektor),
        '3 kwartyl': np.percentile(wektor, 75),
        '90 percentyl': np.percentile(wektor, 90),
        'maksimum': np.max(wektor),
        'rozstep danych': np.max(wektor) - np.min(wektor),
        'rozstep miedzykwartylowy': np.percentile(wektor, 75) - np.percentile(wektor, 25),
        'skosnosc': skew(wektor),
        'kurtoza': kurtosis(wektor)
    }

    tabela_statystyk = pd.DataFrame(list(statystyki.items()), columns=['Statystyka', 'Wartosc'])
    return tabela_statystyk

dane1 =  data['size_sqft'] #oblicznie statystyk na podstawie powierzchni mieszkan
dane2 = data['rent'] #oblicznie statystyk na podstawie cen wynajmu mieszkan

print(oblicz_statystyki_opisowe(dane1), '\n')
print(oblicz_statystyki_opisowe(dane2))

# Zeby zbytnio nie komplikowac kodu postanowilem kolejna czesc zadania przeniesc do osobnego pliku o nazwie 'zadanie1CD.py§
# model liniowy do predykcji ceny wynajmu znjduje sie w kolejnym pliku


