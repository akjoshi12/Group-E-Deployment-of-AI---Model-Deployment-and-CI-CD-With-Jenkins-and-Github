import numpy as np
from tensorflow.keras.preprocessing.sequence import pad_sequences
from joblib import load

# Load LSTM model and tokenizer
lstm_model = load('/Users/atrijoshi/Downloads/Manual Library/AI&DS/SEMESTER 3/DevOps/Final Term/GroupE_CICD/models/LSTM_model.pkl')

# Try loading the tokenizer, or rebuild if not found
try:
    tokenizer = load('/Users/atrijoshi/Downloads/Manual Library/AI&DS/SEMESTER 3/DevOps/Final Term/GroupE_CICD/models/tokenizer.pkl')
except FileNotFoundError:
    print("Tokenizer not found. Rebuilding tokenizer...")
    from tensorflow.keras.preprocessing.text import Tokenizer
    tokenizer = Tokenizer(num_words=15000)  # Adjust if necessary

# Sample test cases
sample_texts = [
    "These shoes are very comfortable.",
    "The product quality is poor and disappointing.",
    "Delivery was fast, and the product met expectations.",
]

# Function to test LSTM Model
def test_lstm():
    print("\nTesting LSTM Model...")
    sequences = tokenizer.texts_to_sequences(sample_texts)
    padded_sequences = pad_sequences(sequences, maxlen=100)
    probabilities = lstm_model.predict(padded_sequences)
    predictions = probabilities.argmax(axis=1)
    sentiment_labels = ['Negative', 'Neutral', 'Positive']
    for text, pred in zip(sample_texts, predictions):
        print(f"Text: '{text}' --> Predicted Sentiment: {sentiment_labels[pred]}")
    assert len(predictions) == len(sample_texts), "LSTM model prediction count mismatch."

if __name__ == "__main__":
    test_lstm()
