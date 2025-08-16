import crawler4ai

async def scrape_url(url: str) -> str:
    """
    Scrape a bookmaker page and return raw text.
    """
    job = await crawler4ai.run(
        {
            "url": url,
            "extract": {"text": True},  
            "render_js": True
        }
    )
    return job["text"]
