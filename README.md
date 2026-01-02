# 🎓 Tuition Class Chatbot

A simple **FAQ-based chatbot** built using **Python and Flask** for a tuition class.  
The chatbot can answer common questions such as class time, subjects, fees, location, and contact details.

This project is built using **free and open-source tools** and is suitable for beginners learning backend development, Flask, and GitHub workflow.

---

## ✨ Features

- Web-based chat interface
- FAQ-based chatbot logic
- Simple keyword matching
- Flask backend API
- Easy to extend and customize
- Beginner-friendly project structure

---

## 🛠️ Tech Stack

- **Python 3**
- **Flask**
- **HTML, CSS, JavaScript**
- **Git & GitHub**

---

## 📂 Project Structure

tuition-chatbot/
│
├── app.py # Flask application
├── requirements.txt # Python dependencies
├── README.md # Project documentation
│
├── data/
│ └── faq.json # Chatbot knowledge base
│
├── chatbot/
│ └── bot.py # Chatbot logic
│
├── templates/
│ └── index.html # Chat UI
│
└── venv/ # Virtual environment (not pushed)


---

## 🚀 How to Run the Project Locally

### 1️⃣ Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/tuition-chatbot.git
cd tuition-chatbot

2️⃣ Create a virtual environment
python -m venv venv

3️⃣ Activate the virtual environment
venv\Scripts\activate

4️⃣ Install dependencies
pip install -r requirements.txt

5️⃣ Run the Flask app
python app.py

6️⃣ Open in browser
http://127.0.0.1:5000

Example Questions to Try

hello

class time

what subjects do you teach

fees

where are you located

contact number

#How the Chatbot Works (Simple Explanation)

User types a message in the browser

JavaScript sends the message to Flask (/chat endpoint)

Flask calls chatbot logic

Chatbot matches keywords with FAQ data

Response is sent back to the user

#Limitations

Keyword-based matching only

No machine learning (yet)

Not deployed online (runs locally)

🔮 Future Improvements

Add Sinhala language support 🇱🇰

Improve intent matching using NLP

Deploy online using free hosting (Render)

Add database support

Improve UI design

👤 Author

Yehan Manodya

This project was created as a personal learning project and uploaded to GitHub for practice and portfolio purposes.