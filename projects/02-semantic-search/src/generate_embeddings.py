from sentence_transformers import SentenceTransformer

MODEL_NAME = "all-MiniLM-L6-v2"

model = SentenceTransformer(MODEL_NAME)


sentences = [
    "Migration count mismatch due to duplicate records",
    "Reconciliation data discrepancy found after data transfer",
    "Dog is playing in the garden"
]

embeddings = model.encode(sentences)

print("\nEmbedding Shape : ", embeddings.shape)

print("\nFirst 10 dimensions : ")
print(embeddings[0])