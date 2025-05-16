import requests
import os
import shutil
import subprocess
from datetime import datetime
from pathlib import Path
from dotenv import load_dotenv

# Load API keys and config from .env
load_dotenv()
SHOPIFY_API_KEY = os.getenv("SHOPIFY_API_KEY")
SHOPIFY_STORE_URL = os.getenv("SHOPIFY_STORE_URL")
SHOPIFY_API_VERSION = os.getenv("SHOPIFY_API_VERSION", "2023-04")

# Update these with your actual GitHub details
GITHUB_USERNAME = "yourusername"
GITHUB_REPO = "your-repo-name"

def create_product(title, body_html, price, image_url=None):
    url = f"https://{SHOPIFY_STORE_URL}/admin/api/{SHOPIFY_API_VERSION}/products.json"
    headers = {
        "X-Shopify-Access-Token": SHOPIFY_API_KEY,
        "Content-Type": "application/json"
    }

    product_data = {
        "product": {
            "title": title,
            "body_html": body_html,
            "variants": [{"price": str(price)}]
        }
    }

    if image_url:
        product_data["product"]["images"] = [{"src": image_url}]

    try:
        response = requests.post(url, json=product_data, headers=headers)
        if response.status_code == 201:
            print(f"✅ Shopify product created: {title}")
            return response.json()
        else:
            print(f"❌ Shopify product creation failed: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"❌ Shopify API error: {e}")

    return None


def push_zip_to_github(zip_path):
    zip_name = Path(zip_path).name
    target_path = f"downloads/{zip_name}"

    try:
        # Copy the ZIP to /downloads/
        shutil.copy(zip_path, target_path)

        # Git add, commit, and push
        subprocess.run(["git", "add", target_path], check=True)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
        commit_message = f"Add product ZIP: {zip_name} ({timestamp})"
        subprocess.run(["git", "commit", "-m", commit_message], check=True)
        subprocess.run(["git", "push"], check=True)

        print(f"✅ ZIP pushed to GitHub: {target_path}")
        return zip_name
    except Exception as e:
        print(f"❌ GitHub upload failed: {e}")
        return None


def get_github_download_url(zip_name):
    return f"https://{GITHUB_USERNAME}.github.io/{GITHUB_REPO}/downloads/{zip_name}"
