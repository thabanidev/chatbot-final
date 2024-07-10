import gensim.downloader as api
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import string
from intents_file import intents
import numpy as np

nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')

lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))

# Loading Word2Vec model
word_vectors = api.load("word2vec-google-news-300")

def preprocess_text(text: str):
    """Preprocesses the user input."""
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))  # Remove punctuation
    words = nltk.word_tokenize(text)
    words = [lemmatizer.lemmatize(word) for word in words if word not in stop_words]
    return ' '.join(words)

def calculate_similarity(processed_input, pattern):
    """Calculates the cosine similarity between the processed input and pattern using Word2Vec."""
    input_vectors = [word_vectors[word] for word in processed_input.split() if word in word_vectors]
    pattern_vectors = [word_vectors[word] for word in pattern.split() if word in word_vectors]

    if not input_vectors or not pattern_vectors:
        return 0  # No words in common

    similarity = np.dot(np.mean(input_vectors, axis=0), np.mean(pattern_vectors, axis=0)) / (np.linalg.norm(np.mean(input_vectors, axis=0)) * np.linalg.norm(np.mean(pattern_vectors, axis=0)))
    return similarity

def predict_intent(processed_input: str):
    """Predicts the intent of the user input using Word2Vec embeddings."""
    max_similarity = -1
    best_intent = None  # Initialize to None

    for intent in intents:
        for pattern in intent['patterns']:
            similarity = calculate_similarity(processed_input, pattern)
            if similarity > max_similarity:
                max_similarity = similarity
                best_intent = intent
    return best_intent
