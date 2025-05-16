from flask import Flask
from apis.rapidapi_textgen import generate_product_text
from apis.rapidapi_imagegen import generate_image
from utils.zip_builder import build_zip
from utils.trend_fetcher import get_trending_keywords
from utils.shopify_uploader import create_product
import random

app = Flask(__name__)

@app.route('/')
def home():
    return "🧞 Nichecraft_Automation is alive! Visit /generate-product to create and upload."

@app.route('/generate-product')
def generate_product():
    # 1. Get a trending topic
    trend = random.choice(get_trending_keywords())
    title = f"{trend.title()} Digital Product"
    
    # 2. Generate product description
    description = generate_product_text(f"Write a persuasive Shopify description for a product titled '{title}'.")

    # 3. Generate product image
    generate_image(f"{trend} cover design for a digital product")

    # 4. Write readme and license
    with open("README.txt", "w") as f:
        f.write(description or "Thank you for your purchase!")

    with open("LICENSE.txt", "w") as f:
        f.write("For personal use only. No redistribution or resale allowed.")

    # 5. Package into a ZIP
    zip_path = build_zip(title)

    # 6. Upload to Shopify
    price = round(random.uniform(5.99, 49.99), 2)
    image_url = None  # Shopify accepts image URLs or uploads via a separate API (can be added later)
    create_product(title, description, price, image_url)

    return f"✅ Product '{title}' created and uploaded with price ${price}!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
