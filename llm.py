import httpx
import os

HUGGINGFACE_TOKEN = os.getenv("HUGGINGFACE_TOKEN")

async def analyze_with_llm(parsed_data: list):
    """
    Sends parsed bookmaker odds to Hugging Face LLM for summarization/analysis.
    """
    headers = {"Authorization": f"Bearer {HUGGINGFACE_TOKEN}"}
    url = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.2"

    async with httpx.AsyncClient(timeout=60.0) as client:
        response = await client.post(url, headers=headers, json={
            "inputs": f"Summarize and structure these betting odds: {parsed_data}"
        })
        return response.json()
