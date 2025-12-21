from dotenv import load_dotenv
load_dotenv()
import os

import chromadb

client = chromadb.Client()
collection = client.get_or_create_collection("best_friends_memory")

def save_interaction(question: str, answer: str):
    collection.add(
        documents=[answer],
        metadatas=[{"question": question}],
        ids=[str(len(collection.get()["ids"]) + 1)]
    )

def get_similar_questions(question: str, k=3):
    results = collection.query(
        query_texts=[question],
        n_results=k
    )
    return results
