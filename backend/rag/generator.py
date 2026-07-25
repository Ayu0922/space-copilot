from groq import Groq
from config import GROQ_API_KEY, LLM_MODEL

client = Groq(api_key=GROQ_API_KEY)

SYSTEM_PROMPT = """You are a space research assistant with deep knowledge of astronomy, 
astrophysics, space missions, and related fields. You have access to research papers, 
NASA/ISRO datasets, and live space news.

When answering:
- Be precise and cite the source context when available
- If the context does not contain the answer, say so honestly
- Keep answers clear and suitable for researchers and enthusiasts alike
- Use metric units and standard scientific notation"""

def generate_answer(query: str, context_chunks: list[dict], history: list[dict] = None) -> str:
    context_text = ""
    if context_chunks:
        context_text = "\n\n--- Relevant context from documents ---\n"
        for i, chunk in enumerate(context_chunks, 1):
            source = chunk["metadata"].get("source", "Unknown")
            context_text += f"\n[{i}] Source: {source}\n{chunk['text']}\n"
        context_text += "\n--- End of context ---\n"

    messages = [{"role": "system", "content": SYSTEM_PROMPT}]

    if history:
        for msg in history[-6:]:
            messages.append({"role": msg["role"], "content": msg["content"]})

    user_message = f"{context_text}\n\nUser question: {query}" if context_text else query
    messages.append({"role": "user", "content": user_message})

    response = client.chat.completions.create(
        model=LLM_MODEL,
        messages=messages,
        max_tokens=1024,
        temperature=0.3,
    )

    return response.choices[0].message.content