from fastapi import FastAPI
from scraper import scrape_bookmakers
from parser import parse_odds
from llm import analyze_with_llm
import asyncio

app = FastAPI()

BOOKMAKER_URLS = [
    "https://www.betika.com",
    "https://www.betway.co.ke",
    "https://www.22bet.co.ke",
    "https://www.sportpesa.co.ke",
    "https://www.odibets.com",
    "https://www.mozzartbet.co.ke",
    "https://www.premierbet.co.ke",
    "https://www.betwinner.ke",
    "https://www.bongobongo.ke",
    "https://www.mcheza.co.ke"
]

@app.get("/scrape-odds")
async def scrape_and_analyze():
    raw_data = scrape_bookmakers(BOOKMAKER_URLS)
    parsed = parse_odds(raw_data)
    analysis = await analyze_with_llm(parsed)
    return {"parsed_odds": parsed, "llm_analysis": analysis}
