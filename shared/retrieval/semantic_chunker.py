
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

MODEL_NAME = "all-MiniLM-L6-v2"

model = SentenceTransformer(MODEL_NAME)

def semantic_chunk_documents(document_text, similarity_threshold=0.2):
    sentences = [
        line.strip() for line in document_text.split("\n") if line.strip()
    ]
    if not sentences:
        return []
    
    embeddings = model.encode(sentences)
    chunks = []
    current_chunk = [sentences[0]]
    for i in range(1, len(sentences)):
        
        score = cosine_similarity([embeddings[i-1]], [embeddings[i]])[0][0]

        if score < similarity_threshold:
            chunks.append("\n".join(current_chunk))
            current_chunk = []
        current_chunk.append(sentences[i])
    
    return chunks