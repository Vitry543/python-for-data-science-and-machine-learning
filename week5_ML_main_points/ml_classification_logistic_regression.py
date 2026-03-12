# implement a logistic regression model to classify a dataset(eg: predicitng if a customer will make a purchase)
# Anlayze the model performance using metrics such as accuracy, precision, recall, and F1 score  

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report

# generate the data
np.random.seed(42)
n_samples=200
X=np.random.rand(n_samples, 2)*10
y=(X[: , 0] * 1.5 + X[:, 1] > 15).astype(int)

# create a dataframe
df=pd.DataFrame(X, columns=['age', 'salary'])
df['purchase'] = y

# split the data into train and test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# initialize the logistic regression model
model = LogisticRegression()

# train the model
model.fit(X_train, y_train)

# make predictions
y_pred = model.predict(X_test)

# evaluate the model
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Precision:", precision_score(y_test, y_pred))
print("Recall:", recall_score(y_test, y_pred))
print("F1 Score:", f1_score(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))

# plot the decision boundary
plt.scatter(X[:, 0], X[:, 1], c=y, cmap='viridis', edgecolors='k')
plt.xlabel('Age')
plt.ylabel('Salary')
plt.title('Decision Boundary')
plt.show()

