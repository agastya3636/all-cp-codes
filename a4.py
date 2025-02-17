Lab 9: AI: 2024 :Decision Tree, Classification Tree and Random Forest
Decision Tree


# Importing necessary libraries
import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.tree import plot_tree
import matplotlib.pyplot as plt

# Sample dataset: 10 samples
data = {
    'Dose': [20, 50, 10, 30, 40, 15, 25, 35, 45, 55],
    'Age': [25, 30, 35, 40, 28, 32, 45, 50, 60, 65],
    'Sex': [0, 1, 0, 1, 1, 0, 1, 0, 1, 0],  # 0: Female, 1: Male
    'Effectiveness': [70, 80, 65, 85, 75, 60, 77, 90, 88, 95]  # % effectiveness to cure
}

# Creating a DataFrame
df = pd.DataFrame(data)

# Defining features (Dose, Age, Sex) and target (Effectiveness)
X = df[['Dose', 'Age', 'Sex']]
y = df['Effectiveness']

# Splitting the data into training and test sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initializing the Decision Tree Regressor
regressor = DecisionTreeRegressor(random_state=42)

# Training the model
regressor.fit(X_train, y_train)

# Predicting the effectiveness on test data
y_pred = regressor.predict(X_test)

# Calculating the Mean Squared Error for evaluation
mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error:", mse)

# Printing the predictions vs actual values
print("\nPredicted Effectiveness vs Actual Effectiveness:")
for i in range(len(y_test)):
    print(f"Predicted: {y_pred[i]:.2f}, Actual: {y_test.values[i]}")

# Visualizing the Decision Tree using matplotlib
plt.figure(figsize=(16,10), dpi=300)  # Increase figsize and dpi to make the plot clearer
plot_tree(
    regressor, 
    feature_names=['Dose', 'Age', 'Sex'], 
    filled=True, 
    rounded=True, 
    fontsize=8  # Reduce the font size to avoid overlapping
)
plt.title("Decision Tree Regressor")
plt.show()


Decision Tree Errors

# Importing necessary libraries
import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.tree import plot_tree
import matplotlib.pyplot as plt

# Sample dataset: 10 samples
data = {
    'Dose': [20, 50, 10, 30, 40, 15, 25, 35, 45, 55],
    'Age': [25, 30, 35, 40, 28, 32, 45, 50, 60, 65],
    'Sex': [0, 1, 0, 1, 1, 0, 1, 0, 1, 0],  # 0: Female, 1: Male
    'Effectiveness': [70, 80, 65, 85, 75, 60, 77, 90, 88, 95]  # % effectiveness to cure
}

# Creating a DataFrame
df = pd.DataFrame(data)

# Defining features (Dose, Age, Sex) and target (Effectiveness)
X = df[['Dose', 'Age', 'Sex']]
y = df['Effectiveness']

# Splitting the data into training and test sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initializing the Decision Tree Regressor
regressor = DecisionTreeRegressor(random_state=42)

# Training the model
regressor.fit(X_train, y_train)

# Predicting the effectiveness on test data
y_pred = regressor.predict(X_test)

# Calculating the Mean Squared Error for evaluation
mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error:", mse)

# Calculating R² score
r2 = r2_score(y_test, y_pred)
print("R² Score:", r2)

# Calculating adjusted R² score
n = X_test.shape[0]  # Number of test samples
p = X_test.shape[1]  # Number of predictors (features)
adjusted_r2 = 1 - (1 - r2) * (n - 1) / (n - p - 1)
print("Adjusted R² Score:", adjusted_r2)

# Printing the predictions vs actual values
print("\nPredicted Effectiveness vs Actual Effectiveness:")
for i in range(len(y_test)):
    print(f"Predicted: {y_pred[i]:.2f}, Actual: {y_test.values[i]}")

# Feature importance from the Decision Tree
importance = regressor.feature_importances_
features = ['Dose', 'Age', 'Sex']

print("\nFeature Importances:")
for i, feature in enumerate(features):
    print(f"{feature}: {importance[i]:.4f}")

# Visualizing the Decision Tree using matplotlib
plt.figure(figsize=(16,10), dpi=300)  # Increase figsize and dpi to make the plot clearer
plot_tree(
    regressor, 
    feature_names=features, 
    filled=True, 
    rounded=True, 
    fontsize=8  # Reduce the font size to avoid overlapping
)
plt.title("Decision Tree Regressor")
plt.show()





3. Classification Tree
# Importing necessary libraries
import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from sklearn.tree import plot_tree
import matplotlib.pyplot as plt

# Sample dataset: 10 samples
data = {
    'Dose': [20, 50, 10, 30, 40, 15, 25, 35, 45, 55],
    'Age': [25, 30, 35, 40, 28, 32, 45, 50, 60, 65],
    'Sex': [0, 1, 0, 1, 1, 0, 1, 0, 1, 0],  # 0: Female, 1: Male
    'Disease': [0, 1, 0, 1, 1, 0, 1, 1, 1, 1]  # 0: No disease, 1: Disease
}

# Creating a DataFrame
df = pd.DataFrame(data)

# Defining features (Dose, Age, Sex) and target (Disease)
X = df[['Dose', 'Age', 'Sex']]
y = df['Disease']

# Splitting the data into training and test sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initializing the Decision Tree Classifier
classifier = DecisionTreeClassifier(random_state=42)

# Training the model
classifier.fit(X_train, y_train)

# Predicting the disease outcome on test data
y_pred = classifier.predict(X_test)

# Calculating the accuracy of the model
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# Displaying a detailed classification report
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# Visualizing the Decision Tree using matplotlib
plt.figure(figsize=(16,10), dpi=300)
plot_tree(
    classifier, 
    feature_names=['Dose', 'Age', 'Sex'], 
    class_names=['No Disease', 'Disease'], 
    filled=True, 
    rounded=True, 
    fontsize=8
)
plt.title("Decision Tree Classifier")
plt.show()

Multistage Classification Tree Classifier

# Importing necessary libraries
import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from sklearn.tree import plot_tree
import matplotlib.pyplot as plt

# Modified dataset: 12 samples to better showcase multistage classification
data = {
    'Dose': [20, 50, 10, 30, 40, 15, 25, 35, 45, 55, 60, 65],
    'Age': [25, 30, 35, 40, 28, 32, 45, 50, 60, 65, 48, 33],
    'Sex': [0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1],  # 0: Female, 1: Male
    'Smoking': [0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0],  # 0: Non-smoker, 1: Smoker
    'Disease': [0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0]  # 0: No Disease, 1: Disease
}

# Creating a DataFrame
df = pd.DataFrame(data)

# Defining features (Dose, Age, Sex, Smoking) and target (Disease)
X = df[['Dose', 'Age', 'Sex', 'Smoking']]
y = df['Disease']

# Splitting the data into training and test sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initializing the Decision Tree Classifier with max depth to force multistage splits
classifier = DecisionTreeClassifier(random_state=42, max_depth=4)

# Training the model
classifier.fit(X_train, y_train)

# Predicting the disease outcome on test data
y_pred = classifier.predict(X_test)

# Calculating the accuracy of the model
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# Displaying a detailed classification report
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# Printing the test data along with the predictions
print("\nSample Predictions:")
for i in range(len(y_test)):
    print(f"Test Sample {i + 1} -> Features: {X_test.iloc[i].to_dict()} | Actual: {y_test.iloc[i]} | Predicted: {y_pred[i]}")

# Visualizing the Decision Tree using matplotlib
plt.figure(figsize=(16,10), dpi=300)
plot_tree(
    classifier, 
    feature_names=['Dose', 'Age', 'Sex', 'Smoking'], 
    class_names=['No Disease', 'Disease'], 
    filled=True, 
    rounded=True, 
    fontsize=8
)
plt.title("Multistage Decision Tree Classifier")
plt.show()
5. Random Forest Classification

# Importing necessary libraries
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, f1_score, classification_report
import matplotlib.pyplot as plt
import seaborn as sns

# Sample dataset: 10 samples
data = {
    'Dose': [20, 50, 10, 30, 40, 15, 25, 35, 45, 55],
    'Age': [25, 30, 35, 40, 28, 32, 45, 50, 60, 65],
    'Sex': [0, 1, 0, 1, 1, 0, 1, 0, 1, 0],  # 0: Female, 1: Male
    'Effectiveness': [70, 80, 65, 85, 75, 60, 77, 90, 88, 95]  # % effectiveness to cure
}

# Creating a DataFrame
df = pd.DataFrame(data)

# Introducing a binary classification target 'Cure' (0: Less effective, 1: More effective)
# Threshold: If Effectiveness >= 80, label it as '1' (effective), else '0' (not effective)
df['Cure'] = np.where(df['Effectiveness'] >= 80, 1, 0)

# Defining features (Dose, Age, Sex) and target (Cure)
X = df[['Dose', 'Age', 'Sex']]
y = df['Cure']

# Splitting the data into training and test sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initializing the Random Forest Classifier
classifier = RandomForestClassifier(random_state=42, n_estimators=100)

# Training the model
classifier.fit(X_train, y_train)

# Predicting the 'Cure' on test data
y_pred = classifier.predict(X_test)

# Calculating accuracy and F1 score for evaluation
accuracy = accuracy_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

print("Accuracy:", accuracy)
print("F1 Score:", f1)

# Detailed classification report
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# Showing the predictions for each test sample
print("\nTest Sample Classification Results:")
for i in range(len(X_test)):
    print(f"Sample {i + 1}: Predicted Cure = {y_pred[i]}, Actual Cure = {y_test.values[i]}")

# Visualizing feature importance
importances = classifier.feature_importances_
features = X.columns
indices = np.argsort(importances)[::-1]

plt.figure(figsize=(8, 6))
sns.barplot(x=importances[indices], y=features[indices], palette="viridis")
plt.title("Feature Importances in Random Forest")
plt.xlabel('Importance')
plt.ylabel('Feature')
plt.show()

