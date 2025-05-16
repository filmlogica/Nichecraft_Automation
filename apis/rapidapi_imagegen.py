import requests
import os
from dotenv import load_dotenv

load_dotenv()
RAPIDAPI_KEY = os.getenv("RAPIDAPI_KEY")

def generate_image(prompt="Digital planner cover with sunrise"):
    url = "https://deepai.org/api/text2img"
    headers = {
        "api-key": RAPIDAPI_KEY
    }
    try:
        response = requests.post(url, data={'text': prompt}, headers=headers)
        img_url = response.json().get("output_url")
        if img_url:
            img_data = requests.get(img_url).content
            with open("generated_image.png", "wb") as f:
                f.write(img_data)
            return "generated_image.png"
    except Exception as e:
        print(f"Error generating image: {e}")
    return None
