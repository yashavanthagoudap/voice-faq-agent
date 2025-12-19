# 🎧 AI-Powered Voice FAQ Agent (Python Backend)

## 📌 Overview

This project implements an **AI-powered voice-based customer support agent** that answers user questions **strictly from a provided FAQ PDF**.

The agent accepts **live microphone input**, converts speech to text, retrieves the most relevant answer from the FAQ document, converts the response back to speech, and maintains a **full conversation transcript**.

If a user asks a question **outside the scope of the FAQ**, or if the speech input is **unclear**, the agent gracefully handles the situation by **requesting clarification** or **transferring the call to a live agent**, exactly as required by the assignment.

---

## ✨ Key Features

* 🎙️ Live voice interaction using microphone input (Streamlit)
* 🗣️ Speech-to-Text (STT) using **Vosk** (fully open-source, offline)
* 🔍 FAQ-based question answering (PDF-only)
* 🧠 Semantic retrieval using sentence embeddings + FAISS
* 🔊 Text-to-Speech (TTS) for spoken responses
* 🚫 Strict non-hallucination policy
* 🤝 Graceful clarification for unclear speech
* 📞 Explicit live-agent transfer for out-of-scope questions
* 🧾 Complete conversation transcript generation

---

## 🏗️ Architecture Overview

User (Microphone)
↓
Streamlit UI
↓
Speech-to-Text (Vosk)
↓
FAQ Retriever (Embeddings + FAISS)
↓
Response Decision Logic
• Answer from FAQ
• Ask for clarification
• Transfer to live agent
↓
Text-to-Speech
↓
Audio response to user

---

## 🧰 Technology Stack

| Component      | Technology                  |
| -------------- | --------------------------- |
| Frontend       | Streamlit                   |
| Speech-to-Text | Vosk (open-source, offline) |
| Text-to-Speech | gTTS                        |
| PDF Parsing    | PyPDF                       |
| Retrieval      | FAISS                       |
| Embeddings     | sentence-transformers       |
| Language       | Python 3.10+                |

---

## 📂 Project Structure

voice_faq_agent/
├── app.py                  – Streamlit UI & call flow
├── voice_agent.py          – Core agent logic
├── pdf_loader.py           – PDF parsing & chunking
├── retriever.py            – Semantic retrieval with confidence scoring
├── stt.py                  – Speech-to-Text (Vosk)
├── tts.py                  – Text-to-Speech
├── transcript.py           – Conversation transcript handling
├── data/
│   └── NTTA VEHICLE BAN FAQs.FINAL.pdf
├── models/
│   ├── vosk-model-small-en-us-0.15/
│   
├── requirements.txt
└── README.md

---

## ⚙️ Setup Instructions

### 1️⃣ Create Virtual Environment

python -m venv venv
venv\Scripts\activate

---

### 2️⃣ Install Dependencies

pip install -r requirements.txt

---

### 3️⃣ Download Required Models

#### Vosk Speech Model

Download and extract **vosk-model-small-en-us-0.15**
[https://alphacephei.com/vosk/models](https://alphacephei.com/vosk/models)

Place it inside:
models/vosk-model-small-en-us-0.15/

---

### 4️⃣ Place FAQ PDF

Move the provided FAQ document into the **data/** directory.

Any PDF placed inside `data/` is automatically loaded by the system.

---

### 5️⃣ Run the Application

streamlit run app.py

Open in browser:
[http://localhost:8501](http://localhost:8501)

---

## 🔄 How It Works (End-to-End Flow)

1. User speaks via microphone
2. Speech is converted to text using Vosk
3. The query is semantically matched against the FAQ PDF
4. System decision logic:

   * Strong match → Answer from FAQ
   * Weak / unclear match → Ask user to repeat
   * No match → Transfer to live agent
5. Response is converted to speech
6. Full conversation transcript is displayed

---

## 🚫 Out-of-Scope Handling

If a question **cannot be answered** using the FAQ document, the agent responds with:

“I do not have an answer to that question, let me transfer your call to the live agent.”

This behavior strictly follows the assignment requirement and prevents hallucination.

---

## ❓ Handling Unclear Speech

When speech recognition produces ambiguous or low-confidence results, the agent responds with:

“I’m sorry, I couldn’t clearly understand that. Could you please repeat or rephrase your question?”

This ensures correctness, safety, and a natural conversational experience.

---

## ✅ Conclusion

This project demonstrates a **robust, safe, and production-aligned voice support agent** that:

* Answers strictly from provided documentation
* Never hallucinates responses
* Gracefully handles uncertainty
* Delivers a realistic, voice-first customer support experience

