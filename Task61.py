# 1. Определить какое максимальное и минимальное значение median_house_value
# 2. Показать максимальное median_house_value, где median_income = 3.1250
# 3. Узнать какая максимальная population в зоне минимального значения median_house_value

from pandas import read_csv
data = read_csv('california_housing_test.csv')
print(f"{data['median_house_value'].max()}, {data['median_house_value'].min()}")
print(data[data['median_income'] == 3.1250]['median_house_value'].max())
print(data[data['median_house_value'] == data['median_house_value'].min()]['population'].max())