from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer("all-MiniLM-L6-v2")

sentences = [
    "Migration count mismatch due to duplicate records",
    "Reconciliation data discrepancy found after data transfer",
    "Dog is playing in the garden"
]

embeddings = model.encode(sentences)

mirgation_vs_reconciliation = cosine_similarity(
    [embeddings[0]],
    [embeddings[1]]
)[0][0]

migration_vs_dog = cosine_similarity(
    [embeddings[0]],
    [embeddings[2]]
)[0][0]

print("\nMigration <--> Reconciliation : ", round(mirgation_vs_reconciliation, 4))
print("\nMigration <--> Dog : ", round(migration_vs_dog, 4))