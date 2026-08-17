import pickle
import faiss
import numpy as np

from sentence_transformers import SentenceTransformer

MODEL_NAME = "all-MiniLM-L6-v2"

model = SentenceTransformer(MODEL_NAME)

index = faiss.read_index(
    "data/chunk_index.faiss"
)

with open(
    "data/chunks.pkl",
    "rb"
) as file:
    chunks = pickle.load(file)



def retrieve(query, top_k = 3):

    query_embedding = model.encode(
        query
    )

    query_embedding = np.array(
        [query_embedding],
        dtype=np.float32
    )

    top_k = min(top_k, len(chunks))

    distances, indices = index.search(
        query_embedding,
        top_k
    )

    result = []

    for idx, distance in zip(indices[0], distances[0]):
        result.append(
            {
                "chunk" : chunks[idx],
                "distance" : distance
            }
        )

    return result



