import pickle
import faiss
import numpy as np

from sentence_transformers import SentenceTransformer

from chunk import Chunk
from semantic_chunker import semantic_chunk_documents

MODEL_NAME = "all-MiniLM-L6-v2"

model = SentenceTransformer(MODEL_NAME)

with open("data/knowledge_base.txt", "r", encoding="utf-8") as file:
    document = file.read()

raw_chunks = semantic_chunk_documents(document, similarity_threshold=0.20)

chunks = []

for idx, text in enumerate(raw_chunks):

    chunks.append(
        Chunk(
            chunk_id=idx,
            text=text,
            source="knowledge_base.txt",
            section=idx+1
        )
    )

embeddings = model.encode(
    [chunk.text for chunk in chunks]
)

embeddings = np.array(
    embeddings,
    dtype=np.float32
)

dimension = embeddings.shape[1]

index = faiss.IndexFlatL2(dimension)

index.add(embeddings)

faiss.write_index(
    index,
    "data/chunk_index.faiss"
)

with open("data/chunks.pkl", "wb") as file:
    pickle.dump(chunks, file)

print(f"Indexed {len(chunks)} chunks")