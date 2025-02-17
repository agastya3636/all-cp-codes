Lab 10: AI: Supervised Classification: LDA, KNN, Naïve Bayes Classifier

1. Supervised Classification: LDA, KNN, Naïve Bayes Classifier using numeric data
import numpy as np
import matplotlib.pyplot as plt
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

# Training Data (RGB values for Red Apple, Green Grapes, and Blueberry)
# Format: [R, G, B]
red_apple = [[255, 0, 0], [250, 10, 5], [245, 20, 15]]
green_grapes = [[0, 255, 0], [5, 250, 10], [10, 245, 15]]
blueberry = [[0, 0, 255], [10, 5, 250], [20, 15, 245]]

# Labels for the classes: 0 = Red Apple, 1 = Green Grapes, 2 = Blueberry
X_train = np.array(red_apple + green_grapes + blueberry)
y_train = np.array([0] * 3 + [1] * 3 + [2] * 3)

# Test Data (unknown data points to test the classifier)
X_test = np.array([[240, 30, 20],  # Should be Red Apple
                   [0, 250, 5],    # Should be Green Grapes
                   [15, 10, 240],  # Should be Blueberry
                   [255, 40, 10]]) # Should be Red Apple

y_test = np.array([0, 1, 2, 0])  # Ground truth labels for testing

# 1. LDA Classifier
lda = LDA()
lda.fit(X_train, y_train)
y_pred_lda = lda.predict(X_test)
accuracy_lda = accuracy_score(y_test, y_pred_lda)
print(f'LDA Classification Accuracy: {accuracy_lda * 100:.2f}%')

# 2. KNN Classifier
def knn_classification(k):
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)
    y_pred_knn = knn.predict(X_test)
    accuracy_knn = accuracy_score(y_test, y_pred_knn)
    print(f'KNN (k={k}) Classification Accuracy: {accuracy_knn * 100:.2f}%')

# Test KNN with different k values
for k in [1, 3, 5]:
    knn_classification(k)

# 3. Naive Bayes Classifier
nb = GaussianNB()
nb.fit(X_train, y_train)
y_pred_nb = nb.predict(X_test)
accuracy_nb = accuracy_score(y_test, y_pred_nb)
print(f'Naive Bayes Classification Accuracy: {accuracy_nb * 100:.2f}%')

# Scatter plot for training data
plt.figure(figsize=(8, 6))
# Plot Red Apples
plt.scatter(X_train[y_train == 0][:, 0], X_train[y_train == 0][:, 1], 
            color='red', label='Red Apple (Train)', marker='o', s=100)
# Plot Green Grapes
plt.scatter(X_train[y_train == 1][:, 0], X_train[y_train == 1][:, 1], 
            color='green', label='Green Grapes (Train)', marker='s', s=100)
# Plot Blueberries
plt.scatter(X_train[y_train == 2][:, 0], X_train[y_train == 2][:, 1], 
            color='blue', label='Blueberry (Train)', marker='^', s=100)

# Plot Test Samples
plt.scatter(X_test[:, 0], X_test[:, 1], color='black', label='Test Samples', 
            marker='x', s=200, edgecolor='white')

# Adding labels and title
plt.title('Fruit Classification (RGB Space)')
plt.xlabel('R (Red)')
plt.ylabel('G (Green)')
plt.legend()
plt.grid(True)
plt.show()

2. Supervised Classification: Naïve Bayes Classifier using text data
import numpy as np
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer

# Define the training data: Normal (0) and Spam (1) messages
messages = [
    "Dear Lunch",  # Normal
    "Friend Lunch",  # Normal
    "Dear Friend",  # Normal
    "Lunch Money",  # Normal
    "Dear Money",  # Normal
    "Lunch Lunch",  # Normal
    "Friend Dear",  # Normal
    "Lunch Lunch Money",  # Normal
    "Dear Friend Money",  # Spam
    "Dear Friend Money Money",  # Spam
    "Money Dear Friend",  # Spam
    "Money Money Friend Dear",  # Spam
]

# Labels: 0 = Normal, 1 = Spam
y_train = np.array([0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1])

# Convert the text messages to token counts (Bag-of-Words model)
vectorizer = CountVectorizer()
X_train = vectorizer.fit_transform(messages)

# Initialize and train the Naive Bayes Classifier
nb = MultinomialNB()
nb.fit(X_train, y_train)

# Define the test messages
test_messages = [
    "Dear Friend",  # Should be classified as Normal
    "Dear Lunch Money Money Money Money"  # Should be classified as Spam
]

# Convert the test messages to token counts using the same vectorizer
X_test = vectorizer.transform(test_messages)

# Predict the classes for the test messages
y_pred = nb.predict(X_test)

# Display the results
for i, message in enumerate(test_messages):
    label = 'Spam' if y_pred[i] == 1 else 'Normal'
    print(f"Message: '{message}' -> Classified as: {label}")

