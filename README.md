# Mini-RAG — Document Question Answering System

A simple **Retrieval-Augmented Generation (RAG)** application that allows users to ask questions about their own documents and retrieve relevant information using semantic search.

The project uses **document chunking, embeddings, vector storage, and retrieval** to find the most relevant information from a PDF before generating an answer.

---

## Project Overview

**Mini-RAG** is an AI-powered document question-answering system.

Instead of searching through a large PDF manually, users can ask questions in natural language. The system searches the uploaded document for relevant content and uses the retrieved information to provide a useful answer.

### Example

**User Question:**

> What is Artificial Intelligence?

The system searches the stored document for relevant sections and returns an answer based on the retrieved information.

---

## Objectives

* Build a simple Retrieval-Augmented Generation application.
* Allow users to ask questions about documents.
* Convert document text into smaller chunks.
* Generate embeddings for document chunks.
* Store embeddings in a vector database.
* Retrieve relevant information using semantic similarity.
* Provide answers based on the retrieved document content.

---

##  How the System Works

The Mini-RAG system follows these main steps:

```text
                  PDF Document
                       │
                       ▼
                Extract Text
                       │
                       ▼
                 Text Chunking
                       │
                       ▼
              Generate Embeddings
                       │
                       ▼
              Store in Vector DB
                       │
                       ▼
                  User Query
                       │
                       ▼
             Query Embedding
                       │
                       ▼
             Semantic Retrieval
                       │
                       ▼
             Relevant Documents
                       │
                       ▼
                  Final Answer
```

---

##  Key Features

### 1.  Document Processing

The system reads information from PDF documents and prepares the content for retrieval.

### 2.  Text Chunking

Large document content is divided into smaller chunks so that relevant information can be retrieved efficiently.

### 3.  Embeddings

The project uses the **`all-MiniLM-L6-v2`** sentence-transformer model to convert text into numerical vector representations.

### 4.  Semantic Search

Instead of matching only exact keywords, the system searches for information based on the semantic meaning of the query.

### 5.  Vector Database

**ChromaDB** is used to store and retrieve document embeddings.

### 6.  Question Answering

Users can ask questions related to the indexed document and retrieve relevant information.

---

##  Technologies Used

| Technology               | Purpose                       |
| ------------------------ | ----------------------------- |
| Python                   | Main programming language     |
| ChromaDB                 | Vector database               |
| Sentence Transformers    | Text embeddings               |
| all-MiniLM-L6-v2         | Embedding model               |
| PyPDF                    | PDF text extraction           |
| LangChain Text Splitters | Document chunking             |
| Flask                    | Application/backend framework |
| HTML/CSS                 | User interface                |

---

##  Project Structure

```text
mini-rag-main/
│
├── documents/
│   └── ai_notes.pdf
│
├── app.py
├── query.py
├── requirements.txt
├── .gitignore
├── README.md
│
└── data/
    └── chroma_db/
```

> Note: The `data/` directory is excluded from GitHub using `.gitignore` because it contains locally generated/vector database data.

---

##  Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/msaibabu2006-maker/min_rag_main.git
```

### Step 2: Open the Project

```bash
cd min_rag_main
```

### Step 3: Create a Virtual Environment

```bash
python -m venv venv
```

### Step 4: Activate the Virtual Environment

For Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### Step 5: Install Dependencies

```bash
pip install -r requirements.txt
```

---

##  Running the Project

Start the application using:

```bash
python app.py
```

The application will start locally.

Open the local URL displayed in the terminal in your web browser.

---

##  Example Usage

1. Start the application.
2. Provide or use the available PDF document.
3. Ask a question related to the document.
4. The system converts the question into an embedding.
5. ChromaDB searches for the most relevant document chunks.
6. The retrieved information is used to provide the answer.

### Example Questions

```text
What is Artificial Intelligence?

What are the applications of AI?

What are the advantages of Artificial Intelligence?

Explain machine learning.

What is deep learning?
```

---

##  What is RAG?

**RAG stands for Retrieval-Augmented Generation.**

It combines information retrieval with AI-generated responses.

A basic RAG system works like this:

```text
User Question
      ↓
Retrieve Relevant Information
      ↓
Provide Retrieved Context
      ↓
Generate Answer
```

This allows an AI application to use information from a specific knowledge source instead of relying only on information stored in the language model.

---

##  Why Use RAG?

Traditional AI systems may not have access to a user's private or newly created documents.

RAG allows an application to retrieve information from external sources such as:

* PDFs
* Documents
* Websites
* Databases
* Company knowledge bases

This makes RAG useful for building document-based AI assistants.

---

##  Project Workflow

### Document Processing

```text
PDF
 ↓
Text Extraction
 ↓
Text Cleaning
 ↓
Chunking
 ↓
Embedding Generation
 ↓
ChromaDB
```

### Query Processing

```text
User Question
 ↓
Query Embedding
 ↓
Similarity Search
 ↓
Relevant Chunks
 ↓
Answer
```

---

##  Future Improvements

The project can be further improved by adding:

* 🔹 Support for multiple PDF documents
* 🔹 Chat history
* 🔹 Better conversational memory
* 🔹 Source citations for answers
* 🔹 Multiple document formats
* 🔹 Improved user interface
* 🔹 Authentication
* 🔹 Cloud deployment
* 🔹 Advanced RAG techniques
* 🔹 LLM integration
* 🔹 Document upload functionality

---

##  Learning Outcomes

Through this project, I learned about:

* Python application development
* Retrieval-Augmented Generation
* Natural Language Processing
* Text embeddings
* Semantic search
* Vector databases
* Document processing
* PDF text extraction
* Python virtual environments
* Git and GitHub
* Building AI-based applications

---

##  Future Vision

The goal of this project is to develop it into a more complete **AI document assistant** capable of handling multiple documents and providing accurate, context-aware answers with source references.

---

##  Author

**M. Sai Babu**

B.Tech — Computer Science and Engineering

Gudlavalleru Engineering College

GitHub:
https://github.com/msaibabu2006-maker

---

##  Project

If you find this project useful, consider giving the repository a ⭐ on GitHub.

---

##  License

This project is created for **educational and learning purposes**.
