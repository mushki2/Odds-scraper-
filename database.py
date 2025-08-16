import os
from supabase import create_client, Client

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def save_match(data: dict):
    """
    Save parsed match data into Supabase
    """
    response = supabase.table("matches").insert(data).execute()
    return response
