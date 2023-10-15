from pandas import read_csv
data = read_csv('california_housing_test.csv')
print(data.shape)
print(data.info())
print(data.dtypes)