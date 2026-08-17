import pickle
import numpy as np

from sentence_transformers import SentenceTransformer

MODEL_NAME = "all-MiniLM-L6-v2"

model = SentenceTransformer(MODEL_NAME)

with open("data/knowledge_base.txt", "r", encoding="utf-8") as file:
    documents = [
        line.strip() for line in file if line.strip()
    ]

embeddings = model.encode(documents)

np.save("data/knowledge_base_embeddings.npy", embeddings)

with open("data/knowledge_base.pkl", "wb") as file:
    pickle.dump(documents, file)

print(f"Indexed {len(documents)} documents")
print(f"Embedding Shape : {embeddings.shape}")
