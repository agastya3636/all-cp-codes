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
    "The new update is fantastic, everything works smoothly.",
    "I absolutely hate the new layout, it's confusing.",
    "The customer service was prompt and very helpful.",
    "I'm not satisfied with the product, it broke in a week.",
    "The event was well-organized and enjoyable.",
    "I don't like how the app crashes frequently.",
    "The meal was delicious and perfectly cooked.",
    "The delivery took way too long, very frustrating.",
    "The movie was good, but I've seen better.",
    "The new features are okay, but not groundbreaking.",
    "The music at the party was amazing, I had so much fun.",
    "The instructions were unclear and hard to follow.",
    "The book was a decent read, nothing too exciting.",
    "The service was terrible, I won't be coming back.",
    "The scenery was breathtaking, truly a beautiful place.",
    "The meeting was productive but also quite tiring."
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
