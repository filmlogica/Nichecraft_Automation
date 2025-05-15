from flask import Flask
from utils.trend_fetcher import get_trending_keywords
from utils.shopify_uploader import create_product

app = Flask(__name__)

@app.route('/generate')
def generate_and_upload_product():
    trend = get_trending_keywords()[0]
    product_title = f"{trend} Exclusive Merch"
    description = f"Get your hands on the trending {trend} product before it’s gone!"
    price = 19.99

    result = create_product(product_title, description, price)

    return f"Product created: {product_title}" if result else "Product creation failed."

@app.route('/')
def home():
    return "ShopiGenie is online! Visit /generate to create a product."
