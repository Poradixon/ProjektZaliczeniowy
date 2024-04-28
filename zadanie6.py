import numpy as np
import matplotlib.pyplot as plt

def oblicz_krzywa_lorenza(wektor_par):
    posortowane = sorted(wektor_par, key=lambda x: x[0])
    kumulatywna_suma = np.cumsum([p[1] for p in posortowane])


    suma_y = sum([p[1] for p in posortowane])
    kumulatywna_suma_procentowa = kumulatywna_suma / suma_y

    krzywa_lorenza = np.insert(kumulatywna_suma_procentowa, 0, 0)
    return krzywa_lorenza

def oblicz_wspolczynnik_giniego(wektor_par):
    krzywa_lorenza = oblicz_krzywa_lorenza(wektor_par)

    pole_pod_krzywa = np.trapz(krzywa_lorenza, dx=1 / len(krzywa_lorenza))
    pole_pod_linia_doskonala = 0.5

    wspolczynnik_giniego = (pole_pod_linia_doskonala - pole_pod_krzywa) / pole_pod_linia_doskonala
    return wspolczynnik_giniego

def narysuj_krzywa_lorenza(wektor_par):
    krzywa_lorenza = oblicz_krzywa_lorenza(wektor_par)
    os_x = np.linspace(0, 1, len(krzywa_lorenza))

    plt.plot(os_x, krzywa_lorenza)
    plt.plot([0, 1], [0, 1], 'k--')

    plt.xlabel('Frakcja populacji')
    plt.ylabel('Frakcja dochodu')
    plt.title('Krzywa Lorenza')
    plt.show()

# Dane do sprawdzenia czy wczesniej napisane funkcje poprawnie dzialaja
wektor_par = [(0, 0), (1, 10), (2, 20), (3, 15), (4, 25)]
wspolczynnik_giniego = oblicz_wspolczynnik_giniego(wektor_par)
print(f'Współczynnik Giniego: {wspolczynnik_giniego}')

narysuj_krzywa_lorenza(wektor_par)

## OBLICZANIE WSPOLCZYNNIKA GINIEGO I KRZYWEJ LORENZA DLA WARTOSCI PRAWDZIWYCH W PLIKU 'zadanie6CD.py'