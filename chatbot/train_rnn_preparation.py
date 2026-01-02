import json
import numpy as np
import pickle
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Load FAQ JSON
with open("data/faq.json", "r", encoding="utf-8") as f:
    faq_data = json.load(f)

# Prepare sentences and labels
sentences = []
labels = []

for intent, data in faq_data.items():
    for keyword in data["keywords"]:
        sentences.append(keyword.lower())
        labels.append(intent)

print("Step 1: Sentences and labels created.")

# Encode labels (intent -> numeric)
lbl_encoder = LabelEncoder()
labels_encoded = lbl_encoder.fit_transform(labels)

print("Step 2: Labels encoded.")

# Tokenize sentences
tokenizer = Tokenizer(num_words=1000, oov_token="<OOV>")
tokenizer.fit_on_texts(sentences)
sequences = tokenizer.texts_to_sequences(sentences)

# Pad sequences so all have same length
padded_sequences = pad_sequences(sequences, padding='post')

print("Step 3: Sentences tokenized and padded.")

# Save prepared data, tokenizer, and label encoder for RNN training
with open("chatbot/padded_sequences.pkl", "wb") as f:
    pickle.dump(padded_sequences, f)

with open("chatbot/labels_encoded.pkl", "wb") as f:
    pickle.dump(labels_encoded, f)

with open("chatbot/tokenizer.pkl", "wb") as f:
    pickle.dump(tokenizer, f)

with open("chatbot/label_encoder.pkl", "wb") as f:
    pickle.dump(lbl_encoder, f)

print("All data saved successfully!")
