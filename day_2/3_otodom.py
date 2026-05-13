import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import seaborn as sns

df = pd.read_csv('otodom.csv')
print(df)

sns.heatmap(df.iloc[:, 2:].corr(), annot=True)
plt.show()
print(df.describe().T.to_string())

plt.hist(df['price'], bins=50)
plt.show()

# chart - price to size
plt.scatter(df['space'], df['price'])
plt.show()

# lets take 50% medium prices
q1 = df.describe().T.loc['price', '25%']
q3 = df.describe().T.loc['price', '75%']
df = df[(df.price >= q1) & (df.price <= q3)]
sns.histplot(df.price)
plt.show()

X = df.iloc[:, 2:]      # no id, no price
y = df.price
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = LinearRegression()
# lets make linear regression like yesterday - 10 minutes
model.fit(X_train, y_train)
print(pd.DataFrame(model.coef_, X.columns))

print(f'Model accuracy: {model.score(X_test, y_test)}')