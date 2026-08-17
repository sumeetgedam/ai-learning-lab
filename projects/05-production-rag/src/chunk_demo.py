from chunker import (
    chunk_by_paragraph, 
    chunk_by_paragraph_with_limit,
    chunk_with_overlap
)

from semantic_chunker import semantic_chunk_documents

with open("data/knowledge_base.txt", "r", encoding="utf-8") as file:

    document = file.read()

chunks = semantic_chunk_documents(document, similarity_threshold=0.20)

print(f"\nTotal Chunks : {len(chunks)}")

for idx, chunk in enumerate(chunks):

    print("\n"+ "=" * 60)

    print(f"Chunk {idx}")

    print("-" * 60)

    print(chunk)

    print("-" * 60)

    print(f"Words : {len(chunk.split())}")