from apify_client import ApifyClient
import os

APIFY_TOKEN = os.getenv("APIFY_TOKEN")

def scrape_bookmakers(bookmaker_urls: list):
    """
    Scrapes bookmaker sites for odds using Apify SDK.
    """
    client = ApifyClient(APIFY_TOKEN)

    results = []
    for url in bookmaker_urls:
        run = client.actor("apify/website-scraper").call(
            run_input={
                "startUrls": [{"url": url}],
                "crawlerType": "cheerio",
                "maxDepth": 2,
                "maxPagesPerCrawl": 5,
                "useChrome": True,
            }
        )
        items = list(client.dataset(run["defaultDatasetId"]).iterate_items())
        results.extend(items)
    return results
