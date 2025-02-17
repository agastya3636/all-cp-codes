AI: Lab 5: Introduction to Sentiment Analysis:  approach to Machine Learning

I'll create a simple Python code that demonstrates sentiment analysis using tokenization, POS tagging, NP/VP extraction, and sentiment classification. We'll use the Natural Language Toolkit (nltk) library for these tasks.
Here's the step-by-step code:
Step-by-Step Python Code
pip install nltk scikit-learn
import nltk
from nltk import pos_tag, word_tokenize
from nltk.chunk import RegexpParser
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Download necessary NLTK data
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

# Sample data: 16 sentences with sentiment labels (12 for training, 4 for testing)
data = [
    ("I love this product.", "Positive"),
    ("This is a great day!", "Positive"),
    ("I am very happy with the service.", "Positive"),
    ("I hate waiting in long lines.", "Negative"),
    ("The food was terrible.", "Negative"),
    ("I am disappointed with the results.", "Negative"),
    ("It's an okay experience.", "Neutral"),
    ("The movie was neither good nor bad.", "Neutral"),
    ("I have mixed feelings about the event.", "Neutral"),
    ("The book is alright, not amazing.", "Neutral"),
    ("She enjoyed the dinner very much.", "Positive"),
    ("I absolutely despise this place.", "Negative"),
    ("The game was fine, nothing special.", "Neutral"),
    ("They did not deliver on time.", "Negative"),
    ("He was thrilled with the outcome.", "Positive"),
    ("This was a boring lecture.", "Negative")
]

# Split the data into training and testing sets (12 training, 4 testing)
train_data = data[:12]
test_data = data[12:]

# Extract sentences and labels
train_sentences, train_labels = zip(*train_data)
test_sentences, test_labels = zip(*test_data)

# Function to perform tokenization and POS tagging
def tokenize_and_pos_tag(sentences):
    pos_tagged_sentences = [pos_tag(word_tokenize(sentence)) for sentence in sentences]
    return pos_tagged_sentences

# Tokenization and POS tagging for training data
train_pos_tagged = tokenize_and_pos_tag(train_sentences)
test_pos_tagged = tokenize_and_pos_tag(test_sentences)

# Extract noun phrases (NP) and verb phrases (VP) using a basic grammar
def extract_np_vp(pos_tagged_sentences):
    grammar = r"""
      NP: {<DT>?<JJ>*<NN.*>}
      VP: {<VB.*><NP|PP|CLAUSE>+$}
    """
    chunker = RegexpParser(grammar)
    extracted_phrases = []
    for sent in pos_tagged_sentences:
        tree = chunker.parse(sent)
        phrases = []
        for subtree in tree:
            if isinstance(subtree, nltk.Tree):
                if subtree.label() == 'NP' or subtree.label() == 'VP':
                    phrase = " ".join(word for word, tag in subtree.leaves())
                    phrases.append(phrase)
        extracted_phrases.append(" ".join(phrases))
    return extracted_phrases

# Extract NP and VP phrases
train_phrases = extract_np_vp(train_pos_tagged)
test_phrases = extract_np_vp(test_pos_tagged)

# Convert phrases into a bag of words model
vectorizer = CountVectorizer()
X_train = vectorizer.fit_transform(train_phrases)
X_test = vectorizer.transform(test_phrases)

# Train a simple Naive Bayes classifier
classifier = MultinomialNB()
classifier.fit(X_train, train_labels)

# Predict sentiment for the test data
predicted_labels = classifier.predict(X_test)

# Display test results
print("Test Sentences and Predicted Sentiments:")
for sentence, true_label, predicted_label in zip(test_sentences, test_labels, predicted_labels):
    print(f"Sentence: {sentence}")
    print(f"True Label: {true_label}, Predicted Label: {predicted_label}\n")
************   *************************   ************************
1 A
# Install required packages
import nltk
from nltk import pos_tag, word_tokenize
from nltk.chunk import RegexpParser
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from nltk.sentiment import SentimentIntensityAnalyzer

# Download necessary NLTK data
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('vader_lexicon')

# Initialize the VADER Sentiment Intensity Analyzer
sia = SentimentIntensityAnalyzer()

# Sample data: 16 sentences (12 for training, 4 for testing)
data = [
    "I love this product.",
    "This is a great day!",
    "I am very happy with the service.",
    "I hate waiting in long lines.",
    "The food was terrible.",
    "I am disappointed with the results.",
    "It's an okay experience.",
    "The movie was neither good nor bad.",
    "I have mixed feelings about the event.",
    "The book is alright, not amazing.",
    "She enjoyed the dinner very much.",
    "I absolutely despise this place.",
    "The game was fine, nothing special.",
    "They did not deliver on time.",
    "He was thrilled with the outcome.",
    "This was a boring lecture."
]

# Function to automatically label sentences using NLTK's VADER
def label_sentence_with_vader(sentences):
    labeled_data = []
    for sentence in sentences:
        score = sia.polarity_scores(sentence)
        # Assign label based on compound score
        if score['compound'] >= 0.05:
            label = 'Positive'
        elif score['compound'] <= -0.05:
            label = 'Negative'
        else:
            label = 'Neutral'
        labeled_data.append((sentence, label))
    return labeled_data

# Auto-label the sentences using VADER
labeled_data = label_sentence_with_vader(data)

# Split the data into training and testing sets (12 training, 4 testing)
train_data = labeled_data[:12]
test_data = labeled_data[12:]

# Extract sentences and labels
train_sentences, train_labels = zip(*train_data)
test_sentences, test_labels = zip(*test_data)

# Function to perform tokenization and POS tagging
def tokenize_and_pos_tag(sentences):
    pos_tagged_sentences = [pos_tag(word_tokenize(sentence)) for sentence in sentences]
    return pos_tagged_sentences

# Tokenization and POS tagging for training and testing data
train_pos_tagged = tokenize_and_pos_tag(train_sentences)
test_pos_tagged = tokenize_and_pos_tag(test_sentences)

# Extract noun phrases (NP) and verb phrases (VP) using a basic grammar
def extract_np_vp(pos_tagged_sentences):
    grammar = r"""
      NP: {<DT>?<JJ>*<NN.*>}
      VP: {<VB.*><NP|PP|CLAUSE>+$}
    """
    chunker = RegexpParser(grammar)
    extracted_phrases = []
    for sent in pos_tagged_sentences:
        tree = chunker.parse(sent)
        phrases = []
        for subtree in tree:
            if isinstance(subtree, nltk.Tree):
                if subtree.label() == 'NP' or subtree.label() == 'VP':
                    phrase = " ".join(word for word, tag in subtree.leaves())
                    phrases.append(phrase)
        extracted_phrases.append(" ".join(phrases))
    return extracted_phrases

# Extract NP and VP phrases
train_phrases = extract_np_vp(train_pos_tagged)
test_phrases = extract_np_vp(test_pos_tagged)

# Convert phrases into a bag of words model
vectorizer = CountVectorizer()
X_train = vectorizer.fit_transform(train_phrases)
X_test = vectorizer.transform(test_phrases)

# Train a simple Naive Bayes classifier
classifier = MultinomialNB()
classifier.fit(X_train, train_labels)

# Predict sentiment for the test data
predicted_labels = classifier.predict(X_test)

# Display test results
print("Test Sentences and Predicted Sentiments:")
for sentence, true_label, predicted_label in zip(test_sentences, test_labels, predicted_labels):
    print(f"Sentence: {sentence}")
    print(f"True Label: {true_label}, Predicted Label: {predicted_label}\n")
The user can manually label the sentences in the training set as positive, negative, or neutral. This manual labeling helps provide a supervised learning approach for training the model. The manually labeled sentences will act as the ground truth for training the classifier. Once the model is trained on these manually labeled sentences, it can be used to classify the sentiment of the remaining test sentences.
How to Implement Manual Labeling and Use it for Training
To incorporate manual labeling, follow these steps:
Manually Label the Training Data: You will assign each training sentence a sentiment label (positive, negative, or neutral).
Train the Model: Use the manually labeled data to train a machine learning model (e.g., Naive Bayes).
Test the Model: Apply the trained model to classify the sentiment of the test data.
Revised Python Code with Manual Labeling
Here's the updated Python code that allows manual labeling for the training data:
Let's use a simple example of sentiment analysis with the Bag of Words (BoW) approach and a Naive Bayes classifier to demonstrate how we can classify text as positive, negative, or neutral based on the frequency of words.
Example Overview
We'll use 6 sentences, split into 4 for training and 2 for testing. The steps involved are:
Data Preparation: Define the training and test datasets.
Tokenization: Convert sentences into words (tokens).
Vectorization: Convert the text into a BoW model.
Training: Train a Naive Bayes classifier using the training data.
Testing: Use the trained model to predict the sentiment of the test sentences.
1. Data Preparation
Let's use the following sentences for training and testing:
Training Data (4 sentences):
"I love this product." (Positive)
"The service was terrible." (Negative)
"This is an amazing experience." (Positive)
"I am not happy with the food." (Negative)
Testing Data (2 sentences):
"The product is amazing."
"I hate the terrible service."
2. Tokenization
First, we tokenize the sentences into individual words. Tokenization involves splitting sentences into their component words:
Training Data:
Sentence 1: ['I', 'love', 'this', 'product']
Sentence 2: ['The', 'service', 'was', 'terrible']
Sentence 3: ['This', 'is', 'an', 'amazing', 'experience']
Sentence 4: ['I', 'am', 'not', 'happy', 'with', 'the', 'food']
Testing Data:
Sentence 1: ['The', 'product', 'is', 'amazing']
Sentence 2: ['I', 'hate', 'the', 'terrible', 'service']


import nltk
from nltk import pos_tag, word_tokenize
from nltk.chunk import RegexpParser
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Download necessary NLTK data
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

# Sample data: 16 sentences (12 for training, 4 for testing)
data = [
    "I love this product.",
    "This is a great day!",
    "I am very happy with the service.",
    "I hate waiting in long lines.",
    "The food was terrible.",
    "I am disappointed with the results.",
    "It's an okay experience.",
    "The movie was neither good nor bad.",
    "I have mixed feelings about the event.",
    "The book is alright, not amazing.",
    "She enjoyed the dinner very much.",
    "I absolutely despise this place.",
    "The game was fine, nothing special.",
    "They did not deliver on time.",
    "He was thrilled with the outcome.",
    "This was a boring lecture."
]

# Manually label the training data
training_data_labels = [
    ("I love this product.", "Positive"),
    ("This is a great day!", "Positive"),
    ("I am very happy with the service.", "Positive"),
    ("I hate waiting in long lines.", "Negative"),
    ("The food was terrible.", "Negative"),
    ("I am disappointed with the results.", "Negative"),
    ("It's an okay experience.", "Neutral"),
    ("The movie was neither good nor bad.", "Neutral"),
    ("I have mixed feelings about the event.", "Neutral"),
    ("The book is alright, not amazing.", "Neutral"),
    ("She enjoyed the dinner very much.", "Positive"),
    ("I absolutely despise this place.", "Negative")
]

# Separate training data and test data
train_sentences, train_labels = zip(*training_data_labels)
test_sentences = data[12:]

# Function to perform tokenization and POS tagging
def tokenize_and_pos_tag(sentences):
    pos_tagged_sentences = [pos_tag(word_tokenize(sentence)) for sentence in sentences]
    return pos_tagged_sentences

# Tokenization and POS tagging for training and testing data
train_pos_tagged = tokenize_and_pos_tag(train_sentences)
test_pos_tagged = tokenize_and_pos_tag(test_sentences)

# Extract noun phrases (NP) and verb phrases (VP) using a basic grammar
def extract_np_vp(pos_tagged_sentences):
    grammar = r"""
      NP: {<DT>?<JJ>*<NN.*>}
      VP: {<VB.*><NP|PP|CLAUSE>+$}
    """
    chunker = RegexpParser(grammar)
    extracted_phrases = []
    for sent in pos_tagged_sentences:
        tree = chunker.parse(sent)
        phrases = []
        for subtree in tree:
            if isinstance(subtree, nltk.Tree):
                if subtree.label() == 'NP' or subtree.label() == 'VP':
                    phrase = " ".join(word for word, tag in subtree.leaves())
                    phrases.append(phrase)
        extracted_phrases.append(" ".join(phrases))
    return extracted_phrases

# Extract NP and VP phrases for training and testing
train_phrases = extract_np_vp(train_pos_tagged)
test_phrases = extract_np_vp(test_pos_tagged)

# Convert phrases into a bag of words model
vectorizer = CountVectorizer()
X_train = vectorizer.fit_transform(train_phrases)
X_test = vectorizer.transform(test_phrases)

# Train a simple Naive Bayes classifier
classifier = MultinomialNB()
classifier.fit(X_train, train_labels)

# Predict sentiment for the test data
predicted_labels = classifier.predict(X_test)

# Display test results
print("Test Sentences and Predicted Sentiments:")
for sentence, predicted_label in zip(test_sentences, predicted_labels):
    print(f"Sentence: {sentence}")
    print(f"Predicted Label: {predicted_label}\n")













Bow approach for NLP

import nltk
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Download necessary NLTK data
nltk.download('punkt')

# Training and testing data
train_sentences = [
    "I love this product.",        # Positive
    "The service was terrible.",   # Negative
    "This is an amazing experience.",  # Positive
    "I am not happy with the food."    # Negative
]
train_labels = ['Positive', 'Negative', 'Positive', 'Negative']

test_sentences = [
    "The product is amazing.",
    "I hate the terrible service."
]

# Vectorization using CountVectorizer
vectorizer = CountVectorizer()
X_train = vectorizer.fit_transform(train_sentences)
X_test = vectorizer.transform(test_sentences)

# Display token vectors
print("Feature Names (Vocabulary):", vectorizer.get_feature_names_out())
print("\nTraining Data Word Vectors:")
for sentence, vector in zip(train_sentences, X_train.toarray()):
    print(f"Sentence: '{sentence}' -> Vector: {vector}")

print("\nTesting Data Word Vectors:")
for sentence, vector in zip(test_sentences, X_test.toarray()):
    print(f"Sentence: '{sentence}' -> Vector: {vector}")

# Train the Naive Bayes classifier
classifier = MultinomialNB()
classifier.fit(X_train, train_labels)

# Predict sentiment for the test data
predicted_labels = classifier.predict(X_test)

# Display test results
print("\nTest Sentences and Predicted Sentiments:")
for sentence, predicted_label in zip(test_sentences, predicted_labels):
    print(f"Sentence: {sentence} -> Predicted Sentiment: {predicted_label}")
