# from dotenv import load_dotenv
# load_dotenv()
import os
import faiss
import pickle
from sentence_transformers import SentenceTransformer

# Config
BASE_DIR = "memory"
MODEL_NAME = "all-MiniLM-L6-v2"

os.makedirs(BASE_DIR, exist_ok=True)

embedding_model = SentenceTransformer(MODEL_NAME)
DIM = embedding_model.get_sentence_embedding_dimension()

def user_paths(username: str):
    user_dir = os.path.join(BASE_DIR, f"user_{username}")
    os.makedirs(user_dir, exist_ok=True)
    
    index_path = os.path.join(user_dir, "faiss.index")
    data_path = os.path.join(user_dir, "memory.pkl")

    return index_path, data_path

def load_user_memory(username: str):
    index_path, data_path = user_paths(username)

    if os.path.exists(index_path):
        index = faiss.read_index(index_path)
        with open(data_path, "rb") as f:
            faiss_memory = pickle.load(f)
    else:
            index = faiss.IndexFlatL2(DIM)
            faiss_memory = []
    return index, faiss_memory


def save_notes(username: str, notes: list[str], source: str):
    index, faiss_memory = load_user_memory(username)

    embeddings = embedding_model.encode(notes)

    for note, emb in zip(notes, embeddings):
        index.add(emb.reshape(1, -1))
        faiss_memory.append({
            "note": note, "source": source})

    index_path, data_path = user_paths(username)
    faiss.write_index(index, index_path)

    with open(data_path, "wb") as f:
        pickle.dump(faiss_memory, f)

def retrieve_memory(username: str, query: str, k=3):
    index, faiss_memory = load_user_memory(username)

    if index.ntotal == 0:
        return []
    
    query_emb = embedding_model.encode([query])
    _, indices = index.search(query_emb, k)

    results = []
    for i in indices[0]:
        results.append(faiss_memory[i]["note"])
    return results

def make_notes(answer: str):
    notes = []

    for line in answer.split("\n"):
        line = line.strip("-• ").strip()
        if len(line) > 20:
            notes.append(line)

    return notes


