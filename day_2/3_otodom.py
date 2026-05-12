import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import seaborn as sns

df = pd.read_csv('otodom.csv')
print(df)

sns.heatmap(df.iloc[:, 2:].corr(), annot=True)
plt.show()
print(df.describe().T.to_string())