import requests

def ask_llm(context, question):
    prompt = f"""
You are a helpful AI tutor.

Answer the user's question ONLY using the context below.
If answer not in context, say "Not found in document".

Context:
{context}

User question:
{question}
"""

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "mistral",
            "prompt": prompt,
            "stream": False
        }
    )

    return response.json()["response"]
