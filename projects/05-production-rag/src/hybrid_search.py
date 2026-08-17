
from retrieve import retrieve

def keyword_score(query, chunk_text):
    query_terms = set(query.lower().split())

    chunk_terms = set(chunk_text.lower().split())

    matching_terms = (
        query_terms.intersection(chunk_terms)
    )

    return len(matching_terms)


def vector_score(distance):
    return 1 / (1+distance)

def hybrid_search(query, top_k=3):

    faiss_results = retrieve(query, top_k=top_k)

    results = []

    for result in faiss_results:
        chunk = result["chunk"]
        distance = result["distance"]

        keyword = keyword_score(
            query,
            chunk.text
        )

        vector = vector_score(
            distance
        )

        final_score = (
            0.7 * vector
            +
            0.3 * keyword
        )

        results.append(
            {
                "chunk" : chunk,
                "vector_score" : vector,
                "keyword_score" : keyword,
                "final_score" : final_score
            }
        )
    
    results.sort(key=lambda x : x["final_score"], reverse=True)

    return results