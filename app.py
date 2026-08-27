import os
import time
import streamlit as st

from langchain_groq import ChatGroq

from langchain_core.prompts import ChatPromptTemplate
from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS

from dotenv import load_dotenv
load_dotenv()

os.environ.pop("SSL_CERT_FILE", None)
os.environ.pop("SSL_CERT_DIR", None)

groq_api_key = os.getenv("GROQ_API_KEY")
google_api_key = os.getenv("GOOGLE_API_KEY")

if not groq_api_key or not google_api_key:
    st.error("API keys are missing. Please check your .env file.")
    st.stop()

st.set_page_config(page_title="Document Q&A", page_icon="📚")
st.title("📚 Groq powered RAG - Smart Document Q&A")

llm = ChatGroq(groq_api_key=groq_api_key, model="openai/gpt-oss-120b")

prompt = ChatPromptTemplate.from_template(
    """
    You are a helpful document question-answering assistant. Answer the question
    using ONLY the information provided in the context below. If the answer cannot
    be found in the context, say: "The answer is not available in the provided documents.
    Do not use outside knowledge. Do not make up information.

    <context>
    {context}
    </context>

    Question : {input}

    Answer :
    """
)

def vector_embedding():
    if "vectors" in st.session_state:
        return

    loader=PyPDFDirectoryLoader("./sample_pdf")
    docs=loader.load()
    if not docs:
        st.error("No PDF documents were found inside ./python_notes")
        return
    st.session_state.docs = docs

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1500,chunk_overlap=200)
    final_documents = text_splitter.split_documents(docs)
    st.session_state.final_documents = final_documents

    embeddings=GoogleGenerativeAIEmbeddings(model="gemini-embedding-001")
    st.session_state.embeddings = embeddings
    print("Number of chunks:", len(final_documents))
    vectors = FAISS.from_documents(final_documents, embeddings)
    st.session_state.vectors = vectors

if st.button("Create Vector Stores"):
    if "vectors" in st.session_state:
        st.info("Vector database is already created")
    else:
        with st.spinner("Loading pdfs, creating chunks and embeddings..."):
            vector_embedding()

        if "vectors" in st.session_state:
            st.success("Vector Store Database is created successfully")
            st.info(
                    f"Loaded {len(st.session_state.docs)} "
                    f"PDF pages/documents and created "
                    f"{len(st.session_state.final_documents)} chunks."
            )
        else:
            st.warning(
                "Vector store could not be created. "
                "Please add PDF files to the './python_notes' folder."
            )

user_question = st.text_input("What you want to know from documents : ")

if st.button("Ask"):
    if not user_question.strip():
        st.warning("Please enter your question")
        st.stop()

    if "vectors" not in st.session_state:
        st.warning("Please create the vector store first.")
        st.stop()

    retriever = st.session_state.vectors.as_retriever(search_kwargs={"k": 4})
    start = time.perf_counter()
    retrieved_docs = retriever.invoke(user_question)
    context = "\n\n".join( doc.page_content for doc in retrieved_docs )
    messages = prompt.invoke( { "context": context, "input": user_question } )
    response = llm.invoke( messages )
    end = time.perf_counter()

    st.subheader("Answer")
    st.write(response.content)
    st.write(f"Response time: {end-start:.2f} seconds")

    with st.expander("🔎 Document Similarity Search"):
        st.write( f"Retrieved {len(retrieved_docs)} "
                f"relevant document chunks." )

        for i, doc in enumerate( retrieved_docs ):
            st.markdown( f"### Document {i + 1}" )
            st.write( doc.page_content )
            st.write( "Source:", doc.metadata.get( "source", "Unknown" ) )

            if "page" in doc.metadata:
                st.write( "Page:", doc.metadata["page"] + 1 )
            st.divider()

st.write("Developed By : Patil Dev")