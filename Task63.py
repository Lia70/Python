# 1. Изобразите отношение households к population с помощью точечного графика
# 2. Визуализировать longitude по отношения к median_house_value, используя линейный график
# 3. Представить гистограмму по housing_median_age
# 4. Изобразить гистограмму по median_house_value с
# оттенком housing_median_age

import seaborn as sns 
from pandas import read_csv
import matplotlib.pyplot as plt
df = read_csv("california_housing_test.csv")
# (sns.scatterplot(data=df, x="households", y="population"))
# sns.relplot(x="latitude", y="median_house_value", kind="line", data=df)
# sns.histplot(data=df, x="housing_median_age")
# sns.displot(data=df, x="median_house_value", hue="housing_median_age")
plt.show()


