import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = [15, 7]
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


data = pd.read_csv('manhattan.csv')

df = pd.DataFrame(data)
y = df[['rent']]

x = df[[
  'bedrooms',
  'bathrooms',
  'size_sqft',
  'min_to_subway',
  'floor',
  'building_age_yrs',
  'no_fee',
  'has_roofdeck',
  'has_washer_dryer',
  'has_doorman',
  'has_elevator',
  'has_dishwasher',
  'has_patio',
  'has_gym'
]]


x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.8, test_size=0.2, random_state=6)

print(x_train.shape)
print(x_test.shape)
 
print(y_train.shape)
print(y_test.shape)


mlr = LinearRegression()
mlr.fit(x_train, y_train)

y_predict = mlr.predict(x_test)

#Tutaj wpisuje fikcyjne dane mojego mieszkania, tak aby sprawdzic czy cena wynajmu jest adekwatna
moje_mieszkanie = [[3, 1.5, 820, 3, 2, 10, 1, 1, 0, 0, 0, 1, 1, 0]]
 
predict = mlr.predict(moje_mieszkanie)
 
print("Predicted rent: $%.2f" % predict)

print('\n',mlr.coef_)

plt.scatter(df[['bedrooms']], df[['rent']], alpha=0.4)
plt.xlabel("Sypialnie")
plt.ylabel("Cena wynajmu")
plt.title("Ilosc sypialni a cena wynajmu")
plt.show()

print("Train:")
print(mlr.score(x_train, y_train))

print("Test:")
print(mlr.score(x_test, y_test))

residuals = y_predict - y_test
 
plt.scatter(y_predict, residuals, alpha=0.4)
plt.title('Residuals')
 
plt.show()


#Korelacja miedzy zmiennymi
korelacja = x.corr()
print("Macierz korelacji: \n")
print(korelacja)