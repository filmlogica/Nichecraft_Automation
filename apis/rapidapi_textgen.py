import requests
import os
from dotenv import load_dotenv

load_dotenv()

RAPIDAPI_KEY = os.getenv("RAPIDAPI_KEY")

def generate_product_text(prompt="Generate a product description for a digital planner."):
    url = "https://ai-text-generator.p.rapidapi.com/text"
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": RAPIDAPI_KEY,
        "X-RapidAPI-Host": "ai-text-generator.p.rapidapi.com"
    }
    payload = {"prompt": prompt}

    try:
        response = requests.post(url, json=payload, headers=headers)
        return response.json().get("text", "").strip()
    except Exception as e:
        print(f"Error: {e}")
        return ""
