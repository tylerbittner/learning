import pandas as pd
from sklearn.datasets import load_breast_cancer

import matplotlib.pyplot as plt

dataset = load_breast_cancer()
cols = []
for i in range(10, 40):
    cols.append(''.join(['V', str(i)]))

df = pd.DataFrame(dataset['data'], columns=cols)
df['target'] = dataset.target

print(df.head())
print('-' * 20)

# Show data types
df.info()
print('-' * 20)

# Show descriptive/summary stats
print(df.describe())
print('-' * 20)

# Show target variable value distribution
print(df['target'].value_counts())
print('-' * 20)

print('Showing density curve...')
df['V11'].plot.kde()
plt.show()

print('Showing histogram...')
df['V11'].plot.hist()
plt.show()

# *Note diff syntax for boxplot!
print('Showing box plot...')
df.boxplot(['V11', 'V12', 'V13'])
plt.show()

print('Showing single scatter plot...')
df.plot.scatter(x='V11', y='V12')
plt.show()

print('Showing scatter matrix...')
pd.plotting.scatter_matrix(df[['V11', 'V12', 'V13']], figsize=(5, 5))
plt.show()


# Correlations
import numpy as np
import seaborn as sns 

print('Correlations:')
abbrev_cols = cols[:10]
print(f'abbrev_cols={abbrev_cols}')
heatmap = np.corrcoef(df[abbrev_cols].values.T)
sns.heatmap(heatmap, yticklabels=abbrev_cols, xticklabels=abbrev_cols, cmap='PiYG', annot=True)
plt.show()

