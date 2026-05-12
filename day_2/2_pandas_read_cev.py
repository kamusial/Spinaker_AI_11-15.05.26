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