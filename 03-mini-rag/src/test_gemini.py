import os

from dotenv import load_dotenv

# import google.generativeai as genai
from google import genai

load_dotenv()

client  = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
    )

response = client.models.generate_content(
    model = "gemini-3.5-flash",
    contents = "Explain what Rertieval Augmented Generation is in 2 lines"
)

print(response.text)
