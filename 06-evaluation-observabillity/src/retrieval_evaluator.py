import json

from hybrid_search import hybrid_search

def evaluate_retrieval(test_cases):

    passed = 0

    total = len(test_cases)

    for test_case in test_cases:

        query = test_case["query"]

        expected_keywords = [
            keyword.lower()
            for keyword in test_case["expected_keywords"]
        ]

        results = hybrid_search(
            query,
            top_k=3
        )

        retrieved_text = " ".join(
            [
                result["chunk"].text.lower()
                for result in results
            ]
        )

        success = any(
            keyword in retrieved_text
            for keyword in expected_keywords
        )

        if success:
            passed += 1

        status = "PASS" if success else "FAIL"

        print(f"{status} | {query}")

    print(
        f"Retrieval Accuracy : "
        f"{passed}/{total}"
        )
    
    print(
        f"Percentage : "
        f"{(passed/total)*100:.2f}%"
    )


if __name__ == "__main__":
    with open("data/test_cases.json", "r", encoding="utf-8") as file:
        test_cases = json.load(file)

    evaluate_retrieval(test_cases)

    