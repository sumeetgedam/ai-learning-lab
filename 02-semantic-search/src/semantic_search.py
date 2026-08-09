from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

DOCUMENT_PATH = "data/documents.txt"
model = SentenceTransformer("all-MiniLM-L6-v2")

sentences = []


with open(DOCUMENT_PATH, "r", encoding="utf8") as file:
    for line in file:
        sentences.append(line.strip())

embeddings = model.encode(sentences)

query = input("Enter Query : ")
query_embeddings = model.encode(query)

similarities = cosine_similarity(
        [query_embeddings],
        embeddings
    )[0]

result = list(zip(sentences, similarities))

result.sort(key=lambda x : x[1], reverse=True)


print("\nTop 5 query similarity : ")
for doc, score in result[:5]:
    print(f"{score:.4f} -> {doc}")