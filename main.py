from fastapi import FastAPI
from scraper import scrape_url
from parser import parse_with_llm
from database import save_match

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Scraper + Gwen2 API is running 🚀"}

@app.post("/scrape")
async def scrape_endpoint(url: str):
    # 1. Scrape bookmaker URL
    raw_text = await scrape_url(url)

    # 2. Parse with Hugging Face Gwen2
    parsed = parse_with_llm(raw_text)

    # 3. Save to Supabase
    match_data = {
        "sport": parsed.get("sport"),
        "bet_type": parsed.get("bet_type"),
        "odds": parsed.get("odds"),
        "match_url": url,
        "raw_text": raw_text[:1000]  # store only snippet to save tokens
    }
    save_match(match_data)

    return {"message": "Scraping & parsing complete ✅", "data": match_data}
