
![App Screenshot](img.png)
---

## 🧠 NLP Text Analyzer (Streamlit App)

An interactive web app built with **Streamlit** and **NLTK** that performs core NLP tasks including tokenization, stemming, lemmatization, POS tagging, and named entity recognition. Designed for clarity, speed, and beginner-friendly interaction.

---

### 🚀 Features

- 🔤 **Tokenization** — Splits input text into individual words
- 🌱 **Stemming & Lemmatization** — Reduces words to their base forms
- 🏷️ **POS Tagging** — Identifies parts of speech for each token
- 🧠 **Named Entity Recognition** — Extracts entities like people, places, and organizations
- 💾 **Pickle Integration** — Modular backend functions loaded via serialized `.pkl` file
- 🎨 **Styled UI** — Clean layout with column-based button grouping for better UX

---

### 📦 Tech Stack

| Tool        | Purpose                          |
|-------------|----------------------------------|
| Streamlit   | Frontend UI                      |
| NLTK        | NLP processing                   |
| Pickle      | Function serialization           |
| Python      | Core logic and app structure     |

---

### 📁 File Structure

```
streamlit-nlp-analyzer/
├── app.py                 # Streamlit frontend
├── models/
│   └── nlp_functions.pkl  # Serialized NLP functions
├── nlp_backend.py         # Modular NLP logic
├── nlp_functions.py       # Preprocessing utilities
└── README.md              # Project documentation
```

---

### 🧪 How to Run Locally

```bash
git clone https://github.com/<your-username>/streamlit-nlp-analyzer.git
cd streamlit-nlp-analyzer
pip install -r requirements.txt
streamlit run app.py
```
---

