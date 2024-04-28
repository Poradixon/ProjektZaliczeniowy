import zadanie6

# Zarobki osoób o wykształceniu podstawowym dla wszystkich sektorów
wektor =[(3930,68), (4201,68), (3477,65), (3966,65),(4512,68), (3515,61),(3922,69),(4153,69),(3463,68)]

zadanie6.oblicz_krzywa_lorenza(wektor)
wspolczynnik_giniego = zadanie6.oblicz_wspolczynnik_giniego(wektor)
print(f'Współczynnik Giniego: {wspolczynnik_giniego}')

zadanie6.narysuj_krzywa_lorenza(wektor)
