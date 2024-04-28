import numpy as np
import pandas as pd
from scipy.stats import skew, kurtosis

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


wektor = input("Podaj wektor liczb rzeczywistych, oddzielajac je przecinkami: ")
try:
    wektor = list(map(float, wektor.split(',')))
    wynik = oblicz_statystyki_opisowe(wektor)
    print(wynik)
except ValueError:
    print("Wprowadzono niepoprawne dane.")