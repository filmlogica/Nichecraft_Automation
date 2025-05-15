import requests
from config import SHOPIFY_API_KEY, SHOPIFY_STORE_URL, SHOPIFY_API_VERSION

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
            "variants": [
                {
                    "price": str(price)
                }
            ]
        }
    }

    if image_url:
        product_data["product"]["images"] = [{"src": image_url}]

    response = requests.post(url, json=product_data, headers=headers)

    if response.status_code == 201:
        print(f"✅ Product '{title}' created.")
        return response.json()
    else:
        print(f"❌ Failed to create product: {response.status_code} - {response.text}")
        return None
