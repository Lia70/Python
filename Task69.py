# Изобразить гистограмму по flipper_length_mm с оттенком height_group. Сделать анализ

import seaborn as sns 
import matplotlib.pyplot as plt

penguins = sns.load_dataset('penguins')

# penguins['len'] = penguins.apply(f, axis=1)
# penguins.to_csv('penguins.csv')
# print(penguins)

sns.histplot(penguins, x='flipper_length_mm', hue='sex')
plt.show()

