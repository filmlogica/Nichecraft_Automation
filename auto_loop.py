import time
from main import run_product_generation

if __name__ == '__main__':
    print("📆 ShopiGenie automation started. Press CTRL+C to stop.")
    while True:
        run_product_generation()
        print("⏳ Waiting 6 hours...")
        time.sleep(6 * 60 * 60)  # 6 hours
