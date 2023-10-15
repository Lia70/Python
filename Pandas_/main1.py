# from pandas import read_csv

# data = read_csv('california_housing_test.csv')
# print(data.shape)
# print(data.info())
# print(data.dtypes)

# print(data.isnull().sum())
# print(data[data['median_income'] < 2]['median_house_value'])
# print(data[['longitude', 'latitude']])

# print(data.iloc[:, :2])
import matplotlib.pyplot as plt 
import seaborn as sns 
df = sns.load_dataset('penguins')
sns.set_style('darkgrid')
sns.jointplot(data=df, x="flipper_length_mm", y="bill_length_mm", true="species")
plt.show()