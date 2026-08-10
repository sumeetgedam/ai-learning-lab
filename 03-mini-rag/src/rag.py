

def build_prompt(query, retrieved_docs) :
    context = "\n\n".join(
        [
            f"Document {i+1} : {doc}"
            for i, (doc, score) in enumerate(retrieved_docs)
        ]
    )

    return f"""
You are a helpful assistant.

Use ONLY the provided context

If the answer is not present in the context, say:
"I could not find sufficient information in the provided documents"

Context :
{context}

Question: 
{query}
                              
Answer:
"""
