
from hybrid_search import hybrid_search

results = hybrid_search("migration issue")

for result in results:

    print("\n" + "=" * 60)
    print(
        f"\nFinal Score : "
        f"{result['final_score']:.4f}"
        )
    
    print(
        f"\nVector Score : "
        f"{result['vector_score']:.4f}"
        )
    
    print(
        f"\nKeyword Score : "
        f"{result['keyword_score']:.4f}"
        )
    
    print(
        f"Source : "
        f"{result['chunk'].source}"
    )

    print(result['chunk'].text)
