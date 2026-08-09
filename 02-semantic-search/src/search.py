import pickle
import numpy as np

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model  = SentenceTransformer("all-MiniLM-L6-v2")

embeddings = np.load("data/documents_embeddings.npy")

with open("data/documents.pkl", "rb") as file:
    documents = pickle.load(file)

query = input("Enter query : ")

query_embedding = model.encode(query)

scores = cosine_similarity(
    [query_embedding],
    embeddings
)[0]

results = list(zip(documents, scores))

results.sort(key=lambda x: x[1], reverse=True)

print("\nTop 5 results : ")
for doc, score in results[:5]:
    print(f"{score:.4f} -> {doc}")