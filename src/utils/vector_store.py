import os
import chromadb
from typing import List
from langchain_community.embeddings import OpenAIEmbeddings


def get_vector_store(path: str = "./data/vector_store"):
    os.makedirs(path, exist_ok=True)
    client = chromadb.PersistentClient(path)
    return client.get_or_create_collection("resume_docs")


def add_documents(collection, docs: List[str]):
    embeddings = OpenAIEmbeddings()
    for i, doc in enumerate(docs):
        collection.add(
            documents=[doc],
            ids=[f"doc_{i}"],
            embeddings=[embeddings.embed_query(doc)]
        )
