# Custom_chatbot_using_Langchain

## Overview
This project implements a custom chatbot using **LangChain**, designed to extract course data from **Brainlox** and interact with users via a **Flask RESTful API**. The chatbot retrieves relevant information based on user queries using a vector store for efficient search and retrieval.

## Features
- Extracts course data from **https://brainlox.com/courses/category/technical** using LangChain's URL loaders.
- Generates **embeddings** and stores them in a **vector database (FAISS)**.
- Provides a **Flask API** for real-time chatbot interactions.
- Supports **multi-turn conversations** by maintaining chat history.

---

## Installation & Setup
### **1. Clone the Repository**
```sh
 git clone <your-github-repo-url>
 cd <your-repo-folder>
```

### **2. Create a Virtual Environment**
```sh
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### **3. Install Dependencies**
```sh
pip install -r requirements.txt
```

---

## Running the Application
### **1. Start the Flask Server**
```sh
python app.py
```
The server will start at **http://127.0.0.1:5000**

### **2. API Endpoints**
#### **Chat Endpoint** (`POST /chat`)
**Request:**
```json
{
    "message": "what is the duration for the LEARN SCRATCH PROGRAMMING course?",
    "chat_history": [
        {"user": "Hello", "bot": "Hi! How can I help you?"}
    ]
}
```
**Response:**
```json
{
    "response": "The duration is 16 lessons.",
    "chat_history": [
        {"user": "Hello", "bot": "Hi! How can I help you?"},
        {"user": "what is the duration for the LEARN SCRATCH PROGRAMMING course?", "bot": "The duration is 16 lessons."
    ]
}
```

---

## References
- [LangChain Vector Stores](https://python.langchain.com/docs/integrations/vectorstores)
- [LangChain Quickstart Guide](https://python.langchain.com/docs/get_started/quickstart)
- [Brainlox Course Data](https://brainlox.com/courses/category/technical)

