# Projects
# Feature Engineering and Model Evaluation

# objective:
    # -Perform end-to-end feature engineering, model evaluation and hyperparameter tuning on a dataset

# Tasks:
    # task1: perform feature engineering
    # task2:  train and evaluate models
    # task3 Apply grid search for hyperparameter tuning
    

import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer

# Task1: perform feature engineering
# load Titanic dataset
url='https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'
df = pd.read_csv(url)

# display first few rows
print(df.head())
print(df.info())

# select relevant features
# PassengerId,Survived,Pclass,Name,Sex,Age,SibSp,Parch,Ticket,Fare,Cabin,Embarked

df = df[['Pclass','Sex','Age','Fare','Embarked','Survived']]

# handle missing values
# df.method({col: Value}, inplace=True)

# df['Age']=df['Age'].fillna(df["Age"].median(), inplace=True)
# df['Embarked']=df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)

df.fillna({'Age' : df["Age"].median()}, inplace=True)
df.fillna({'Embarked' : df['Embarked'].mode()[0]}, inplace=True)
print(df)

# define feature and target
X=df.drop(columns=['Survived'])
y=df['Survived']

# apply feature scaling and encoding
preprocessor = ColumnTransformer(
    transformers = [
        ('numerical', StandardScaler(), ['Age','Fare']),
        ('categorical', OneHotEncoder(), ['Pclass','Sex','Embarked'])
    ]
)

X_preprocessed = preprocessor.fit_transform(X)

# task2:  train and evaluate models
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# train the models and evaluate logistic regression
log_reg=LogisticRegression(max_iter=200)
log_scores=cross_val_score(log_reg, X_preprocessed, y, cv=5, scoring='accuracy')
print(f"logistic regression accuracy: {log_scores.mean():.2f}")

# train and evaluate random forest
rf_model = RandomForestClassifier(random_state=42)
rf_scores = cross_val_score(rf_model, X_preprocessed, y, cv=5, scoring='accuracy')
print(f"Random Forest Accuracy: {rf_scores.mean():.2f}")

# task3 Apply grid search for hyperparameter tuning
from sklearn.model_selection import GridSearchCV

# define hyperparameter grid
param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [None, 10, 20],
    'min_samples_split': [2, 5, 10]
}

# perform grid search
grid_search = GridSearchCV(
    estimator=RandomForestClassifier(random_state=42),
    param_grid=param_grid,
    cv=5,
    scoring='accuracy',
    n_jobs=-1
)

grid_search.fit(X_preprocessed, y)

# display best hyperparameters and best score
print(f"Best hyperparameters: {grid_search.best_params_}")
print(f"Best accuracy: {grid_search.best_score_:.2f}")
