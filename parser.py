import re

def parse_odds(raw_data):
    """
    Detects sport type + odds (Win/Draw/Loss, Over/Under, Arbitrage).
    Cleans HTML noise and reduces tokens.
    """
    parsed = []

    for entry in raw_data:
        text = entry.get("text", "") or entry.get("html", "")
        
        sport = None
        if re.search(r"football|soccer", text, re.I): sport = "Football"
        elif re.search(r"basketball", text, re.I): sport = "Basketball"
        elif re.search(r"tennis", text, re.I): sport = "Tennis"

        odds_type = []
        if "Over" in text or "Under" in text: odds_type.append("Over/Under")
        if re.search(r"\bDraw\b", text, re.I): odds_type.append("Win/Draw/Loss")
        if "Arbitrage" in text: odds_type.append("Arbitrage")

        parsed.append({
            "sport": sport,
            "odds_type": odds_type,
            "raw_text": text[:500],  # Limit text for token efficiency
            "source_url": entry.get("url", "unknown")
        })
    return parsed
