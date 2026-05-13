import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('diabetes.csv')
print(f'Data {df.shape}')
print(df.describe().T.to_string())
print(f'\nHow many missing values is columns:\n{df.isna().sum()}')

# everywhere, where 0 and N/A put average for column
for col in ['glucose', 'bloodpressure', 'skinthickness', 'insulin',
       'bmi', 'diabetespedigreefunction', 'age']:
    df[col] = df[col].replace(0, np.nan)
    mean_ = df[col].mean()
    df[col] = df[col].replace(np.nan, mean_)

print(f'\nAfter fixing:\nHow many missing values is columns:\n{df.isna().sum()}')

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix

X = df.iloc[:, :-1]
y = df.outcome
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
model = LogisticRegression()
model.fit(X_train, y_train)
print(model.score(X_test, y_test))
print(pd.DataFrame(confusion_matrix(y_test, model.predict((X_test)))))

print(df['outcome'].value_counts())

# change input data. Instead of all 1536 samples, lets take
# 500 healthy and 500 sick people
# and repeat the model
df1 = df.query('outcome==0').sample(n=500)
df2 = df.query('outcome==1').sample(n=500)
df3 = pd.concat([df1, df2])

X = df3.iloc[:, :-1]
y = df3.outcome
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
model = LogisticRegression()
model.fit(X_train, y_train)
print(model.score(X_test, y_test))
print(pd.DataFrame(confusion_matrix(y_test, model.predict((X_test)))))