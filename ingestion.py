from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
import os
import pinecone
from langchain_pinecone import PineconeVectorStore
import streamlit as st

load_dotenv()

# Configurar Pinecone como único retriever
try:
    # Obtener API key desde las variables de entorno
    pinecone_api_key = os.environ.get("PINECONE_API_KEY")
    # Usar el índice legal-docs por defecto, pero permitir configuración mediante variable de entorno
    index_name = os.environ.get("PINECONE_INDEX_NAME", "timbre")
    
    # Inicializar Pinecone y configurar el retriever
    pc = pinecone.Pinecone(api_key=pinecone_api_key)
    
    # Configurar el retriever con Pinecone
    retriever = PineconeVectorStore(
        index_name=index_name,
        embedding=OpenAIEmbeddings(),
        text_key="text"
    ).as_retriever()
    
    print(f"Pinecone configurado correctamente con el índice: {index_name}")
    
except Exception as e:
    print(f"Error al configurar Pinecone: {str(e)}")
    # Usar un retriever nulo que devuelva lista vacía como fallback
    class NullRetriever:
        def invoke(self, query):
            print(f"Error: No se pudo configurar un retriever válido. Query: {query}")
            return []
    
    retriever = NullRetriever()
