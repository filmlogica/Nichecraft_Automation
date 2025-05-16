from apis.rapidapi_textgen import generate_product_text
from apis.rapidapi_imagegen import generate_image
from utils.zip_builder import build_zip
from utils.trend_fetcher import get_trending_keywords
from utils.shopify_uploader import create_product, push_zip_to_github
import random
import os
import shutil
from pathlib import Path
import subprocess

# GitHub public raw URL setup
GITHUB_USER = "yourusername"  # <-- CHANGE THIS
GITHUB_REPO = "your-repo-name"  # <-- CHANGE THIS

# Size limits
MAX_REPO_MB = 950  # Leave headroom under GitHub's 1GB limit

def get_repo_size_mb():
    try:
        result = subprocess.check_output(["du", "-sm", "."])
        size_mb = int(result.decode().split()[0])
        return size_mb
    except Exception as e:
        print(f"⚠️ Could not calculate repo size: {e}")
        return 0

def cleanup_oldest_zips(folder="downloads", keep=10):
    zips = sorted(Path(folder).glob("*.zip"), key=os.path.getmtime)
    while get_repo_size_mb() > MAX_REPO_MB and len(zips) > keep:
        oldest = zips.pop(0)
        print(f"🗑️ Removing {oldest.name} to save space...")
        os.remove(oldest)

def get_github_download_url(zip_name):
    return f"https://{GITHUB_USER}.github.io/{GITHUB_REPO}/downloads/{zip_name}"

def run_product_generation():
    trend = random.choice(get_trending_keywords())
    title = f"{trend.title()} Digital Product"
    
    print(f"\n🚀 Creating product: {title}")

    # Generate content
    description = generate_product_text(f"Write a Shopify product description for '{title}'.")
    generate_image(f"{trend} product mockup")

    # Save base files
    with open("README.txt", "w") as f:
        f.write(description or "Thank you for your purchase!")

    with open("LICENSE.txt", "w") as f:
        f.write("For personal use only. No resale allowed.")

    # Build ZIP
    zip_path = build_zip(title)
    zip_name = Path(zip_path).name

    # Cleanup if needed
    cleanup_oldest_zips()

    # Push ZIP to GitHub and get download link
    push_zip_to_github(zip_path)
    zip_url = get_github_download_url(zip_name)

    # Add download link to description
    description += f"\n\n📥 [Click here to download your product]({zip_url})"

    # Upload to Shopify
    price = round(random.uniform(5.99, 49.99), 2)
    create_product(title, description, price)

    print(f"✅ Product '{title}' created at ${price} with download link:\n{zip_url}")

if __name__ == '__main__':
    run_product_generation()
