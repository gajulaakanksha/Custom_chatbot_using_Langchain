## Importing necessary libraries
from flask import Flask, request, jsonify                       # To import Flask to create a web API
from langchain_community.document_loaders import WebBaseLoader  # To import WebBaseLoader
from langchain_huggingface import HuggingFaceEmbeddings         # To import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS              # To import FAISS
from langchain.chains import ConversationalRetrievalChain       # To import ConversionalRetrivalChain
from langchain_groq import ChatGroq                             # To import ChatGroq
import os

from dotenv import load_dotenv
load_dotenv()
## load the GROQ API Key
os.environ['GROQ_API_KEY']=os.getenv("GROQ_API_KEY")
groq_api_key=os.getenv("GROQ_API_KEY")


# Step 1: Extract data from the website
def load_documents():
    loader = WebBaseLoader("https://brainlox.com/courses/category/technical")
    documents = loader.load()  #  Loads web pages as documents from the given URL
    return documents           # Returns the extracted documents for further processing

# Step 2: Create embeddings and store them in a vector store
def create_vector_store(documents):
    embedding_model=HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2") # Uses Hugging Face’s "all-MiniLM-L6-v2" model to convert text into embeddings

    vector_store = FAISS.from_documents(documents, embedding_model) #Stores embeddings using FAISS

    return vector_store

# Step 3: Set up the Flask API
app = Flask(__name__)                      # Flask initializes a web application


@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.json                          # Receives a JSON request
        user_input = data["message"]                 # Extracts message
        chat_history = data.get("chat_history", [])  # chat_history

        # Convert chat history from a list of dicts to a list of tuples
        formatted_chat_history = [(entry["user"], entry["bot"]) for entry in chat_history if "user" in entry and "bot" in entry]

        # Load documents and vector store
        documents = load_documents()                  
        vector_store = create_vector_store(documents) 

        llm = ChatGroq(groq_api_key=groq_api_key,model_name="Llama3-8b-8192")  # Uses Groq’s model for chatbot responses
        chain = ConversationalRetrievalChain.from_llm(llm, retriever=vector_store.as_retriever()) # Connects the LLM with the vector database and allows the chatbot to provide relevant answers 
        # Pass correctly formatted chat history
        response = chain.invoke({"question": user_input, "chat_history": formatted_chat_history})
        response_text = response.get("answer", "No answer found")

        return jsonify({
            "response": response_text,         # Returns response_text 
            "chat_history": chat_history + [{"user": user_input, "bot": response_text}]  # Returns updated chat_history

        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500  # Catches and returns any errors as a JSON response with a 500 Internal Server Error



























if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)


