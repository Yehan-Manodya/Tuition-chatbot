import pickle
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense, Dropout

# Load preprocessed data
with open("chatbot/padded_sequences.pkl", "rb") as f:
    X = pickle.load(f)

with open("chatbot/labels_encoded.pkl", "rb") as f:
    y = pickle.load(f)

# Get number of classes
num_classes = len(set(y))

# Build the RNN model
model = Sequential([
    Embedding(input_dim=1000, output_dim=16, input_length=X.shape[1]),
    LSTM(32),
    Dropout(0.2),
    Dense(num_classes, activation='softmax')
])

model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Train the model
model.fit(X, np.array(y), epochs=200, verbose=1)

# Save the trained model
model.save("chatbot/rnn_model.h5")
print("RNN model saved as rnn_model.h5")
