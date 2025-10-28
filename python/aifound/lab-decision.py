import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.preprocessing import LabelEncoder
import warnings
warnings.filterwarnings('ignore')

df = pd.read_csv('titanic.csv')

print("DATA PREPROCESSING")

features = ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked']
target = 'Survived'

data = df[features + [target]].copy()

data['Age'].fillna(data['Age'].median(), inplace=True)
data['Fare'].fillna(data['Fare'].median(), inplace=True)
data['Embarked'].fillna(data['Embarked'].mode()[0], inplace=True)

le_sex = LabelEncoder()
le_embarked = LabelEncoder()
data['Sex'] = le_sex.fit_transform(data['Sex'])
data['Embarked'] = le_embarked.fit_transform(data['Embarked'])

print(f"\nMissing values after preprocessing:")
print(data.isnull().sum())

X = data[features]
y = data[target]

print(f"\nFeatures shape: {X.shape}")
print(f"Survival rate: {y.mean():.2%}")

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)

print(f"\nTraining set size: {X_train.shape[0]} ({X_train.shape[0]/len(X)*100:.1f}%)")
print(f"Test set size: {X_test.shape[0]} ({X_test.shape[0]/len(X)*100:.1f}%)")

# Save train and test sets
train_data = pd.concat([X_train, y_train], axis=1)
test_data = pd.concat([X_test, y_test], axis=1)
train_data.to_csv('train.csv', index=False)
test_data.to_csv('test.csv', index=False)

print("DECISION TREE WITH INFORMATION GAIN (ENTROPY)")

dt_entropy = DecisionTreeClassifier(
    criterion='entropy',
    max_depth=8,
    min_samples_split=22,
    min_samples_leaf=9,
    random_state=42
)

dt_entropy.fit(X_train, y_train)
y_pred_entropy = dt_entropy.predict(X_test)

print(f"\nTree Depth: {dt_entropy.get_depth()}")
print(f"Number of Leaves: {dt_entropy.get_n_leaves()}")

print("\nClassification Report:")
print(classification_report(y_test, y_pred_entropy,
                          target_names=['Not Survived', 'Survived']))
accuracy_entropy = accuracy_score(y_test, y_pred_entropy)
print(f"Accuracy: {accuracy_entropy:.8f}")

cm_entropy = confusion_matrix(y_test, y_pred_entropy)
print("\nConfusion Matrix:")
print(cm_entropy)


print("MODEL 2: DECISION TREE WITH GINI INDEX")

dt_gini = DecisionTreeClassifier(
    criterion='gini',
    max_depth=8,
    min_samples_split=22,
    min_samples_leaf=9,
    random_state=42
)

dt_gini.fit(X_train, y_train)
y_pred_gini = dt_gini.predict(X_test)

print(f"\nTree Depth: {dt_gini.get_depth()}")
print(f"Number of Leaves: {dt_gini.get_n_leaves()}")

print("\nClassification Report:")
print(classification_report(y_test, y_pred_gini,
                          target_names=['Not Survived', 'Survived']))

accuracy_gini = accuracy_score(y_test, y_pred_gini)
print(f"\nAccuracy: {accuracy_gini:.4f}")

cm_gini = confusion_matrix(y_test, y_pred_gini)
print("\nConfusion Matrix:")
print(cm_gini)


comparison_df = pd.DataFrame({
    'Metric': ['Accuracy', 'Tree Depth', 'Number of Leaves'],
    'Information Gain (Entropy)': [
        f"{accuracy_entropy:.4f}",
        dt_entropy.get_depth(),
        dt_entropy.get_n_leaves()
    ],
    'Gini Index': [
        f"{accuracy_gini:.4f}",
        dt_gini.get_depth(),
        dt_gini.get_n_leaves()
    ]
})

print("\n", comparison_df.to_string(index=False))

if accuracy_entropy > accuracy_gini:
    print(f"\nInformation Gain performs better with {(accuracy_entropy - accuracy_gini)*100:.2f}% higher accuracy")
elif accuracy_gini > accuracy_entropy:
    print(f"\nGini Index performs better with {(accuracy_gini - accuracy_entropy)*100:.2f}% higher accuracy")
else:
    print("\nBoth criteria perform equally well")


print("FEATURE IMPORTANCE")
feat_imp_df = pd.DataFrame({
    'Feature': features,
    'Entropy': dt_entropy.feature_importances_,
    'Gini': dt_gini.feature_importances_
})
feat_imp_df = feat_imp_df.sort_values('Entropy', ascending=False)
print("\n", feat_imp_df.to_string(index=False))










