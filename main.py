from dotenv import load_dotenv
import os
from PyPDF2 import PdfReader
import streamlit as st
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI
from langchain.callbacks import get_openai_callback

# Load environment variables
load_dotenv()

def process_text(text):
    # Split the text into chunks using langchain
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    chunks = text_splitter.split_text(text)
    
    # Convert the chunks into embeddings to form a knowledge base
    embeddings = OpenAIEmbeddings()
    knowledge = FAISS.from_texts(chunks, embeddings)
    
    return knowledge


def get_all_text(pdf_reader):
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text
    

def main():
    st.title("LLM with your own PDF 💬")

    pdf = st.file_uploader("Upload a PDF Document", type="pdf")
    
    if pdf is not None:
        pdf_reader = PdfReader(pdf)
        text = get_all_text(pdf_reader)
        knowledge = process_text(text)
        
        query = st.chat_input("Ask a question within the context of the PDF")

        cancel_button = st.button("Cancel")
        
        if cancel_button:
            st.stop()
        
        if query:
            with st.chat_message("user"):
                st.write(query)
            docs = knowledge.similarity_search(query)
            llm = OpenAI()
            chain = load_qa_chain(llm, chain_type="stuff")
            
            with get_openai_callback() as cost:
                response = chain.run(input_documents=docs, question=query)
                print(cost)
            
            message = st.chat_message("assistant")
            message.write(response)
                        
if __name__ == "__main__":
    main()