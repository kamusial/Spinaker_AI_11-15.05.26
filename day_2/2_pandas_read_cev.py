import pandas as pd

df = pd.read_csv('weight-height.csv', sep=';')
print(df)

# df['Height'] = df['Height'] * 2.54
df['Height'] *= 2.54
df['Weight'] /= 2.2
print(df)

print(df.describe().T.round(2).to_string())

import matplotlib.pyplot as plt
plt.hist(df.query("Gender=='Female'")['Weight'], bins=30)
# plt.show()
plt.hist(df.query("Gender=='Male'")['Weight'], bins=30)
plt.show()

df = pd.get_dummies(df)
del df['Gender_Male']
df = df.rename(columns={'Gender_Female': 'Gender'})
# 1 / True = Female    0 / False = Male
print(df)

from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(df[['Height', 'Gender']], df['Weight'])
print(model.coef_)
print(model.intercept_)
