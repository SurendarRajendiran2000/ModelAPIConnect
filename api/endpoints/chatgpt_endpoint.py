import os
import openai
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")


def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]

    response = openai.ChatCompletion.create(

        model=model,
        messages=messages,
        temperature=0,
    )
    return response.choices[0].message["content"]


prompt = """
RAG, or retrieval-augmented generation, is a new way to understand and create language. It combines two kinds of models. First, retrieve relevant information. Second, generate text from that information. By using both together, RAG does an amazing job. Each model’s strengths make up for the other’s weaknesses. So RAG stands out as a groundbreaking method in natural language processing.


what is mean by RAG? give me an example
"""


result = get_completion(prompt)
print("AI response: ", result)
