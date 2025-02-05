# Custom_chatbot_using_Langchain

## Overview
This project implements a custom chatbot using **LangChain**, designed to extract course data from **Brainlox** and interact with users via a **Flask RESTful API**. The chatbot retrieves relevant information based on user queries using a vector store for efficient search and retrieval.


## Features
- Extracts course data from **https://brainlox.com/courses/category/technical** using LangChain's URL loaders.
- Generates **embeddings** and stores them in a **vector database (FAISS)**.
- Provides a **Flask API** for real-time chatbot interactions.
- Supports **multi-turn conversations** by maintaining chat history.

---

## Project Features

| Feature               | Description |
|-----------------------|-------------|
| **Web Scraping**      | Extracts course data from Brainlox. |
| **Embeddings**        | Uses Hugging Face embeddings (`all-MiniLM-L6-v2`). |
| **Vector Database**   | Stores embeddings in FAISS for efficient retrieval. |
| **Chatbot API**       | Responds to user queries via a Flask API. |
| **Conversational AI** | Supports chat history for multi-turn conversations. |

---

## Installation & Setup
### Prerequisites
Ensure you have the following installed:
- Python 3.10+
- pip
  
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
After creation store the Groq API Key as :
```
GROQ_API_KEY="Your Groq API Key"
```

### **3. Install Dependencies**
```sh
pip install -r requirements.txt
```

---

## Running the Application
### **Start the Flask Server**
```sh
python app.py
```
The server will start at **http://127.0.0.1:5000**

---

## Test the Chatbot API
Use curl or a tool like Postman to send a POST request

### **API Endpoints
#### **Chat Endpoint** (`POST /chat`)

```http
  POST /http://127.0.0.1:5000/chat
```

| Request Body | Type     | Response                      |
| :-------- | :------- | :-------------------------------- |
| `"message":"what is the duration for the LEARN SCRATCH PROGRAMMING course?"` | `raw` | "response":"The duration is 16 lessons." |


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

## Description
This project is a Flask-based chatbot that uses LangChain, FAISS, and Groq’s LLM to provide intelligent responses based on real-time scraped data. The chatbot extracts course information from Brainlox and enables users to ask questions about technical courses interactively.

#### Key Libraries & Their Roles

| Library                        | Function |
|--------------------------------|---------------------------------------------------------------|
| **Flask**                     | Creates a web API for handling chatbot requests. |
| **WebBaseLoader**              | Loads web pages as documents from the given URL. |
| **HuggingFaceEmbeddings**      | Generates vector embeddings using the `"all-MiniLM-L6-v2"` model. |
| **FAISS**                      | Stores and retrieves vectorized documents efficiently for fast search. |
| **ConversationalRetrievalChain** | Manages conversation memory and retrieves relevant documents. |
| **ChatGroq**                   | Uses Groq’s LLM for generating chatbot responses. |

---

## Example Queries And Outputs

**1. What are the available courses?"**

![f_1](https://github.com/user-attachments/assets/c86c199a-b14f-4fd3-a0b1-c53e0fdb581a)

**2. Show me AI Courses.**

![f_2](https://github.com/user-attachments/assets/99830d92-3aad-465f-bd51-e36b4b00558f)


##  Summary

| Step | Function | Description |
|------|----------|-------------|
| 1️⃣ | `load_documents()` | Scrapes Brainlox course data using LangChain. |
| 2️⃣ | `create_vector_store()` | Converts text into vector embeddings using FAISS. |
| 3️⃣ | **Flask API** | Creates a `POST /chat` endpoint. |
| 4️⃣ | **Chat History Formatting** | Converts chat history into the correct format. |
| 5️⃣ | **Conversational Chain** | Uses **Groq’s LLM** + **FAISS retriever** for responses. |
| 6️⃣ | **Chatbot Response** | Returns a **context-aware answer** with updated history. |

---

##  Conclusion
This Flask-based chatbot effectively combines web scraping, vector storage, and LLM-powered conversation to answer user queries based on real course data.

---

## References
- [LangChain Vector Stores](https://python.langchain.com/docs/integrations/vectorstores)
- [LangChain Quickstart Guide](https://python.langchain.com/docs/get_started/quickstart)
- [Brainlox Course Data](https://brainlox.com/courses/category/technical)

