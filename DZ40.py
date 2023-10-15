# Работать с файлом california_housing_train.csv, который находится в папке sample_data.
# Определить среднюю стоимость дома, где кол-во людей от 0 до 500 (population)

# from pandas import read_csv
# data = read_csv('california_housing_train.csv')
# data[(data['population'] < 500) & (data['population'] > 0)]['median_house_value'].mean()

import pandas as pd

df = pd.read_csv('california_housing_train.csv')
avg = df[(df['population'] > 0) & (df['population'] < 500)]['median_house_value'].mean()
print(avg)
