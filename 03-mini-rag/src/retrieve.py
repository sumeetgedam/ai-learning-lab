import pickle
import numpy as np

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model  = SentenceTransformer("all-MiniLM-L6-v2")

embeddings = np.load("data/knowledge_base_embeddings.npy")

with open("data/knowledge_base.pkl", "rb") as file:
    documents = pickle.load(file)

def retrieve(query, top_k=3) :

    query_embedding = model.encode(query)

    scores = cosine_similarity(
        [query_embedding],
        embeddings
    )[0]

    results = list(zip(documents, scores))

    results.sort(key=lambda x: x[1], reverse=True)

    
    return results[:top_k]
