from google import genai
from config import GEMINI_API_KEY

client = genai.Client(api_key=GEMINI_API_KEY)


def generate_response(context, question, history):

    prompt = f"""
You are a strict RAG-based assistant.

RULES:
- Answer ONLY from the given context
- If answer is not in context → say "Answer not found in provided documents"
- Do NOT hallucinate
- Keep answer concise
- Answer in same language as user

Context:
{context}

Chat History:
{history}

Question:
{question}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text