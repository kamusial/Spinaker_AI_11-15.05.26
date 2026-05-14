import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
# from pyexpat import features
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix

# solve "iris"" problem with Decission Tree Cassifier

df = pd.read_csv('iris.csv')
print(df['class'].value_counts())
print(df)

species = {
    'Iris-setosa': 0, 'Iris-versicolor': 1, 'Iris-virginica':2
}
df['class_value'] = df['class'].map(species)
print(df['class_value'].value_counts())

X = df.iloc[:, :2]
y = df.class_value
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = DecisionTreeClassifier(max_depth=5)
model.fit(X_train, y_train)
print(model.score(X_test, y_test))
print(pd.DataFrame(confusion_matrix(y_test, model.predict(X_test))))
print(pd.DataFrame(model.feature_importances_, X.columns))

from mlxtend.plotting import plot_decision_regions
plot_decision_regions(X.values, y.values, model)
plt.show()