# Узнать какая максимальная households в зоне минимального значения population
import pandas as pd
df = pd.read_csv('california_housing_train.csv')

# Найти минимальное значение 'population'
min_population = df['population'].min()

# Отфильтровать строки с минимальным значением 'population' и найти максимальное значение 'households'
max_households_in_min_population = df[df['population'] == min_population]['households'].max()
print(max_households_in_min_population) 