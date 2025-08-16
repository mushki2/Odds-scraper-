import os
import requests

HF_TOKEN = os.getenv("HUGGINGFACE_TOKEN")
MODEL = "HuggingFaceH4/gwen-2-2b"

def parse_with_llm(raw_text: str):
    """
    Send scraped bookmaker text to Hugging Face Gwen2 model
    and extract structured data (sport, bet type, odds).
    """
    headers = {"Authorization": f"Bearer {HF_TOKEN}"}
    payload = {
        "inputs": f"Extract structured data from this betting site text:\n\n{raw_text}\n\nReturn JSON with keys: sport, bet_type, odds, match_url"
    }

    response = requests.post(
        f"https://api-inference.huggingface.co/models/{MODEL}",
        headers=headers,
        json=payload,
    )

    return response.json()
