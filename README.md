# 🚀 Groq powered RAG — Smart Document Q&A

**GroqRAG** is an AI-powered PDF Question Answering application built using **Retrieval-Augmented Generation (RAG)**.

The application allows users to upload PDF documents into a predefined folder and ask questions about their content. It uses **Gemini Embeddings** to convert document chunks into vector representations, **FAISS** for similarity-based retrieval, and a **Groq-hosted LLM** for generating context-aware answers.

---

## 📌 Project Overview

Traditional LLM applications may generate answers using only the model's pre-trained knowledge. GroqRAG follows a **Retrieval-Augmented Generation** approach:

```text
PDF Documents
      ↓
Document Loading
      ↓
Text Chunking
      ↓
Gemini Embeddings
      ↓
FAISS Vector Store
      ↓
Similarity Search
      ↓
Relevant Document Chunks
      ↓
Groq LLM
      ↓
Context-Aware Answer
```

The LLM is instructed to answer using only the retrieved document context, reducing the possibility of unsupported answers.

---

## ✨ Features

* 📄 PDF document processing
* ✂️ Intelligent text chunking
* 🔢 Gemini-based text embeddings
* 🗂️ FAISS vector database
* 🔎 Similarity-based document retrieval
* 🤖 Groq-powered LLM generation
* 💬 Natural-language document Q&A
* 📚 Displays retrieved document chunks
* 📑 Shows source PDF and page information
* ⏱️ Displays response time
* 🖥️ Simple Streamlit interface
* 🔐 Supports user-provided API keys
* ☁️ Can be deployed on Streamlit Community Cloud

---

## 🛠️ Tech Stack

| Technology                     | Purpose                               |
| ------------------------------ | ------------------------------------- |
| Python                         | Core programming language             |
| Streamlit                      | Web application interface             |
| LangChain                      | RAG application framework             |
| Google Gemini                  | Text embeddings                       |
| Groq                           | LLM inference                         |
| FAISS                          | Vector similarity search              |
| PyPDF                          | PDF document loading                  |
| RecursiveCharacterTextSplitter | Document chunking                     |
| python-dotenv                  | Local environment variable management |

---

## 🧠 Models Used

### Embedding Model

```text
gemini-embedding-001
```

Google's Gemini embedding model converts document text into numerical vector representations that can be used for similarity search and information retrieval.

### Generation Model

```text
openai/gpt-oss-120b
```

The application uses this model through the Groq API.

The Groq model can be changed in the Python code if you want to experiment with another supported Groq model.

---

# 📂 Project Structure

```text
GroqRAG/
│
├── app.py
├── requirements.txt
├── .gitignore
├── README.md
│
├── sample_pdf/
│   ├── document1.pdf
│   ├── document2.pdf
│   └── ...
│
└── .env
```

---

# ⚙️ Prerequisites

Before running the project, install:

* Python 3.10+
* pip
* Git
* A Google Gemini API key
* A Groq API key

---

# 🔑 Step 1 — Get Your Gemini API Key

GroqRAG uses Google Gemini for generating document embeddings.

Create your Gemini API key from **Google AI Studio**.

Google currently recommends using the newer authorization-key approach, and new keys created in Google AI Studio are automatically created as auth keys.

Your key will be used as:

```text
GOOGLE_API_KEY=your_google_api_key
```

---

# 🔑 Step 2 — Get Your Groq API Key

Create an account on GroqCloud and generate an API key.

Your key will be used as:

```text
GROQ_API_KEY=your_groq_api_key
```

---

# 📥 Step 3 — Clone the Repository

Open your terminal and run:

```bash
git clone https://github.com/YOUR_USERNAME/GroqRAG.git
```

Move into the project directory:

```bash
cd GroqRAG
```

Replace `YOUR_USERNAME` with your GitHub username.

---

# 🐍 Step 4 — Create a Virtual Environment

Create a Python virtual environment:

### Windows

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

### macOS / Linux

```bash
python3 -m venv venv
```

Activate it:

```bash
source venv/bin/activate
```

After activation, your terminal should show something similar to:

```text
(venv)
```

---

# 📦 Step 5 — Install Dependencies

Install all required packages:

```bash
pip install -r requirements.txt
```

If you don't have a `requirements.txt` file yet, you can create one containing:

```text
streamlit
langchain
langchain-groq
langchain-community
langchain-core
langchain-text-splitters
langchain-google-genai
faiss-cpu
pypdf
python-dotenv
```

Then run:

```bash
pip install -r requirements.txt
```

Streamlit deployments also use the project's dependency file to install required Python packages in the remote environment.

---

# 🔐 Step 6 — Configure Your API Keys

Create a file named:

```text
.env
```

in the root directory of the project.

Your project should look like:

```text
GroqRAG/
├── app.py
├── requirements.txt
├── .env
└── sample_pdf/
```

Inside `.env`, add:

```env
GROQ_API_KEY=your_groq_api_key_here
GOOGLE_API_KEY=your_google_api_key_here
```

### Example

```env
GROQ_API_KEY=gsk_xxxxxxxxxxxxxxxxx
GOOGLE_API_KEY=AIzaSyxxxxxxxxxxxxxxxx
```

**Do not use these example values as real keys.**

---

# 🚨 IMPORTANT — Protect Your API Keys

Never write API keys directly inside your Python code.

❌ Don't do this:

```python
groq_api_key = "gsk_xxxxxxxxx"
```

❌ Don't commit `.env` to GitHub.

Instead, the application loads keys using:

```python
from dotenv import load_dotenv

load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")
google_api_key = os.getenv("GOOGLE_API_KEY")
```

Groq explicitly recommends environment variables or a secret-management system for API keys.

---

# 🛡️ Step 7 — Create `.gitignore`

Create a file named:

```text
.gitignore
```

Add:

```text
.env
venv/
__pycache__/
*.pyc
.streamlit/secrets.toml
```

This prevents sensitive files and unnecessary Python environment files from being committed.

Streamlit also recommends keeping secrets outside the repository and ensuring secret files are included in `.gitignore`.

---

# 📄 Step 8 — Add PDF Documents

Create the folder:

```text
sample_pdf
```

Place your PDF files inside it:

```text
sample_pdf/
├── Python.pdf
├── Machine_Learning.pdf
└── Artificial_Intelligence.pdf
```

The application loads PDFs using:

```python
loader = PyPDFDirectoryLoader("./sample_pdf")
```

You can add multiple PDF files to this directory.

---

# ▶️ Step 9 — Run the Application

Start Streamlit:

```bash
streamlit run app.py
```

You should see something similar to:

```text
Local URL: http://localhost:8501
```

Open the URL in your browser.

---

# 🧪 Step 10 — Create the Vector Store

After opening the application:

### 1. Add your PDFs

Place your PDF files inside:

```text
sample_pdf/
```

### 2. Click

```text
Create Vector Stores
```

The application will:

```text
Load PDFs
   ↓
Split documents into chunks
   ↓
Generate Gemini embeddings
   ↓
Create FAISS vector store
```

After successful processing, the application will display the number of loaded documents/pages and generated chunks.

---

# 💬 Step 11 — Ask Questions

Enter your question in:

```text
What you want to know from documents:
```

Then click:

```text
Ask
```

The RAG pipeline will:

```text
User Question
      ↓
FAISS Similarity Search
      ↓
Top 4 Relevant Chunks
      ↓
Context Construction
      ↓
Groq LLM
      ↓
Final Answer
```

The application retrieves the four most relevant chunks:

```python
retriever = st.session_state.vectors.as_retriever(
    search_kwargs={"k": 4}
)
```

---

# 🔎 Document Similarity Search

After receiving an answer, expand:

```text
🔎 Document Similarity Search
```

The application displays:

* Retrieved document chunks
* Source PDF
* Page number
* Number of retrieved chunks

This makes the retrieval process more transparent and helps users understand where the answer came from.

---

# ☁️ Deploy on Streamlit Community Cloud

You can deploy this project publicly so recruiters, friends, and other users can access it through a browser.

Streamlit Community Cloud supports GitHub-based deployment and provides built-in secrets management.

## Step 1 — Push the Project to GitHub

Initialize Git:

```bash
git init
```

Add files:

```bash
git add .
```

Commit:

```bash
git commit -m "Initial commit"
```

Rename the branch:

```bash
git branch -M main
```

Add your GitHub repository:

```bash
git remote add origin https://github.com/YOUR_USERNAME/GroqRAG.git
```

Push:

```bash
git push -u origin main
```

---

# 🔐 Step 2 — Do NOT Upload `.env`

Before pushing to GitHub, check:

```bash
git status
```

Make sure `.env` is **not** listed as a file to commit.

Your GitHub repository should contain:

```text
app.py
requirements.txt
README.md
sample_pdf/
.gitignore
```

and should **not** contain:

```text
.env
```

---

# 🌐 Step 3 — Deploy on Streamlit Cloud

Open:

[Streamlit Community Cloud](https://share.streamlit.io/?utm_source=chatgpt.com)

Then:

1. Sign in using GitHub.
2. Click **Create app**.
3. Select your GitHub repository.
4. Select the `main` branch.
5. Select your Streamlit entry file:

```text
app.py
```

6. Open **Advanced settings**.
7. Add your secrets.
8. Deploy the application.

---

# 🔑 Step 4 — Add API Keys to Streamlit Secrets

In Streamlit Cloud, add:

```toml
GROQ_API_KEY = "your_groq_api_key"
GOOGLE_API_KEY = "your_google_api_key"
```

Streamlit Community Cloud provides a Secrets section where you can securely configure secrets without committing them to GitHub.

### Important

Your current code uses:

```python
os.getenv("GROQ_API_KEY")
os.getenv("GOOGLE_API_KEY")
```

Streamlit's secrets system can expose root-level secrets as environment variables, so this approach can work without putting the keys in your repository.

---

# ⚠️ Important Deployment Consideration

This project currently loads PDFs from:

```text
./sample_pdf
```

Therefore, the PDFs included in the GitHub repository are the documents available to the deployed application.

If you want users to upload **their own PDFs through the browser**, the application should be modified to use Streamlit's file uploader:

```python
st.file_uploader()
```

and dynamically process the uploaded documents.

That would make the project a more complete multi-user document Q&A application.

---

# 🔒 Security Best Practices

Never:

* ❌ Commit `.env`
* ❌ Hard-code API keys
* ❌ Put API keys in frontend/client-side code
* ❌ Share API keys in screenshots
* ❌ Upload API keys to GitHub
* ❌ Put API keys directly into `app.py`

Always:

* ✅ Use environment variables locally
* ✅ Use Streamlit Secrets when deploying
* ✅ Add `.env` to `.gitignore`
* ✅ Rotate/revoke compromised API keys
* ✅ Use separate API keys/projects for different environments when appropriate

Groq's security guidance specifically recommends avoiding hard-coded keys and using environment variables or secret-management systems.

---

# 🧩 RAG Components

### 1. Document Loader

```python
PyPDFDirectoryLoader
```

Loads PDF documents from the `sample_pdf` directory.

### 2. Text Splitter

```python
RecursiveCharacterTextSplitter
```

Current configuration:

```python
chunk_size = 1500
chunk_overlap = 200
```

### 3. Embedding Model

```python
GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-001"
)
```

Converts text chunks into vector representations.

### 4. Vector Database

```python
FAISS
```

Stores and searches document embeddings.

### 5. Retriever

```python
as_retriever(search_kwargs={"k": 4})
```

Retrieves the four most relevant document chunks.

### 6. LLM

```python
ChatGroq(
    groq_api_key=groq_api_key,
    model="openai/gpt-oss-120b"
)
```

Generates the final answer using the retrieved context.

---

# 📊 Key Configuration

You can customize these parameters in `app.py`:

### Chunk Size

```python
chunk_size=1500
```

Controls the approximate amount of text in each chunk.

### Chunk Overlap

```python
chunk_overlap=200
```

Keeps some overlapping content between neighboring chunks.

### Number of Retrieved Chunks

```python
search_kwargs={"k": 4}
```

Controls how many relevant chunks are passed to the LLM.

---

# 🐛 Troubleshooting

## API Keys Missing

If you see:

```text
API keys are missing. Please check your .env file.
```

Check that your `.env` contains:

```env
GROQ_API_KEY=your_key
GOOGLE_API_KEY=your_key
```

Also make sure the `.env` file is located in the project root.

---

## No PDF Documents Found

Make sure your folder structure is:

```text
GroqRAG/
├── app.py
└── sample_pdf/
    └── your_file.pdf
```

Not:

```text
python_notes/
```

because the current application loads:

```python
./sample_pdf
```

---

## Vector Store Already Created

The application stores the FAISS object in:

```python
st.session_state.vectors
```

If it already exists during the current Streamlit session, clicking the button again will not recreate it.

---

## Gemini Embedding Quota Error

You may encounter a `429 RESOURCE_EXHAUSTED` error if the Gemini API quota or rate limit has been reached.

Check your Gemini API usage and limits before repeatedly recreating embeddings.

---

## Groq Rate Limit

Groq applies rate limits to API usage. Limits are associated with projects, so usage in one project does not directly consume the limits of another project.

If you reach a rate limit, check your Groq project usage and limits rather than continuously retrying requests.


---

# 📚 Learning Outcomes

This project demonstrates practical knowledge of:

* Retrieval-Augmented Generation (RAG)
* Large Language Model APIs
* Embeddings
* Vector databases
* Semantic similarity search
* LangChain
* FAISS
* Prompt engineering
* PDF document processing
* Streamlit application development
* API key management
* Cloud deployment

---

# 👨‍💻 Author

**Patil Dev**

B.TECH '26 Artificial Intelligence

---

## ⭐ If You Found This Project Useful

If this project helped you understand RAG, embeddings, vector databases, or LLM integration, consider giving the repository a ⭐ on GitHub.

---