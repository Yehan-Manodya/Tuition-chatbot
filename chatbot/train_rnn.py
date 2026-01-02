import pickle
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense, Dropout
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

# Load preprocessed data
with open("chatbot/padded_sequences.pkl", "rb") as f:
    X = pickle.load(f)

with open("chatbot/labels_encoded.pkl", "rb") as f:
    y = pickle.load(f)

# Split into train and test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Number of classes
num_classes = len(set(y))

# Build the RNN model
model = Sequential([
    Embedding(input_dim=1000, output_dim=32, input_length=X.shape[1]),
    LSTM(64),
    Dropout(0.2),
    Dense(num_classes, activation='softmax')
])

model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Train the model
history = model.fit(
    X_train, np.array(y_train),
    epochs=200,
    batch_size=8,
    validation_data=(X_test, np.array(y_test)),
    verbose=1
)

# Save the trained model
model.save("chatbot/rnn_model.h5")
print("RNN model saved as rnn_model.h5")

# Evaluate on test data
loss, acc = model.evaluate(X_test, np.array(y_test), verbose=0)
print(f"\nTest Accuracy: {acc*100:.2f}%")

# Predict and generate classification report
y_pred = np.argmax(model.predict(X_test), axis=1)
print("\nClassification Report:")
print(classification_report(y_test, y_pred))
