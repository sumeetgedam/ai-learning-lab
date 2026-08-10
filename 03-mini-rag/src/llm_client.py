import os

from dotenv import load_dotenv
from google import genai

from retrieve import retrieve
from rag import build_prompt

load_dotenv()

client  = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

def generate_answer(query):
    docs = retrieve(query, top_k=3)

    prompt = build_prompt(
        query=query,
        retrieved_docs=docs
    )

    response = client.models.generate_content(
        model = "gemini-3.5-flash",
        contents = prompt
    )

    return response.text

if __name__=="__main__":
    query = input("Enter your question  : ")

    answer = generate_answer(query)

    print("\nAnswer\n")
    print(answer)