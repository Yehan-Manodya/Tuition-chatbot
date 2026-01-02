import json
import numpy as np
from sentence_transformers import SentenceTransformer, util

# Load model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Load FAQ data
with open("data/faq.json", "r", encoding="utf-8") as f:
    faq_data = json.load(f)

sentences = []
answers = []

# Prepare dataset
for intent, data in faq_data.items():
    if intent == "fallback":
        continue

    for example in data["keywords"]:
        sentences.append(example)
        answers.append(data["answer"])

# Encode all sentences once
sentence_embeddings = model.encode(sentences, convert_to_tensor=True)

def get_bot_response(user_input, threshold=0.5):
    user_embedding = model.encode(user_input, convert_to_tensor=True)

    similarities = util.cos_sim(user_embedding, sentence_embeddings)[0]
    best_score = float(similarities.max())
    best_idx = int(similarities.argmax())

    if best_score < threshold:
        return faq_data["fallback"]["answer"]

    return answers[best_idx]
