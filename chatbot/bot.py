import json
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.sequence import pad_sequences
import pickle

# Load FAQ
with open("data/faq.json", "r", encoding="utf-8") as f:
    FAQ_DATA = json.load(f)

# Load trained RNN model, tokenizer, and label encoder
model = tf.keras.models.load_model("chatbot/rnn_model.h5")

with open("chatbot/tokenizer.pkl", "rb") as f:
    tokenizer = pickle.load(f)

with open("chatbot/label_encoder.pkl", "rb") as f:
    lbl_encoder = pickle.load(f)

def get_bot_response(user_input):
    user_input = user_input.lower()
    seq = tokenizer.texts_to_sequences([user_input])
    padded = pad_sequences(seq, maxlen=model.input_shape[1], padding='post')
    
    # Predict intent with confidence check
    pred = model.predict(padded, verbose=0)
    pred_prob = np.max(pred)  # Highest probability of predicted intent
    
    if pred_prob < 0.5:       # If model is not confident
        return FAQ_DATA["fallback"]["answer"]
    
    intent = lbl_encoder.inverse_transform([np.argmax(pred)])[0]
    return FAQ_DATA[intent]["answer"]

