import requests
import json
import pandas as pd
import time

# --------------------------------------------------
# AliExpress Business API Text Search Endpoint
# --------------------------------------------------
SEARCH_API_URL = "https://aliexpress-business-api.p.rapidapi.com/textsearch.php"

API_HEADERS = {
    "x-rapidapi-key": "YOUR_RAPIDAPI_KEY",  # Replace with your actual API key
    "x-rapidapi-host": "aliexpress-business-api.p.rapidapi.com",
    "Accept": "application/json"
}

# --------------------------------------------------
# Keywords to Search For (Winning Niches)
# --------------------------------------------------
SEARCH_QUERIES = [
    "wireless earbuds", "phone accessories", "gaming mouse", "mechanical keyboard", "USB-C hub", "portable SSD",
    "face serum", "nail extension kit", "LED makeup mirror", "hair growth oil", "jade roller", "face massage tool",
    "kitchen organizer", "LED home lights", "wall art", "smart kitchen scale", "silicone baking mats", "storage bins",
    "yoga mat", "muscle massage gun", "adjustable dumbbells", "resistance bands", "weighted jump rope", "foldable treadmill",
    "dog harness", "cat self-groomer", "pet water dispenser", "automatic pet feeder", "dog training collar", "cat tree tower",
    "car phone holder", "LED car lights", "seat cushion", "wireless car charger", "trunk organizer", "blind spot mirrors",
    "smartwatch", "mini projector", "portable blender", "wireless charging pad", "smart LED strip lights", "Bluetooth tracker",
    "solar power bank", "tactical flashlight", "camping hammock", "portable water filter", "waterproof backpack", "emergency sleeping bag",
    "baby carrier", "breastfeeding pillow", "silicone baby bibs", "portable bottle warmer", "baby monitor", "diaper bag backpack",
    "standing desk converter", "blue light blocking glasses", "wireless ergonomic mouse", "noise-canceling headphones", "USB desk fan", "laptop stand",
    # Additional winning niche suggestions for women:
    "Luxury Handbag Organizer",
    "Elegant Jewelry Display Stand",
    "Designer Sunglasses for Women",
    "Fashionable Statement Earrings",
    "Portable Compact Mirror with LED Light",
    "Trendy Women's Watches",
    "Silk Scarf Multifunctional Wrap",
    "Beauty Blender Makeup Sponge",
    "Skincare Fridge for Cosmetics",
    "Adjustable High Heel Insoles",
    # Additional winning niche suggestions for pregnant women/new baby care:
    "Maternity Support Belt for Back Pain",
    "Pregnancy Pillow for Side Sleeping",
    "Baby Belly Wrap for Prenatal Support",
    "Nursing Bras with Easy Access",
    "Portable Breast Pump"
]

# --------------------------------------------------
# Winning Product Criteria
# --------------------------------------------------
MIN_ORDERS = 5       # Minimum orders (after removing '+' and commas)
MIN_RATING = 4      # Minimum rating
MAX_PRICE = 30.0    # Maximum target sale price (USD)

# --------------------------------------------------
# Function to Fetch Products from the Text Search API
# --------------------------------------------------
def fetch_products(keyword, pages=3):
    """
    Search for products using the text search endpoint.
    Returns a list of product dictionaries with selected details.
    """
    all_products = []
    for page_index in range(1, pages + 1):
        params = {
            "keyWord": keyword,
            "pageSize": 50,
            "pageIndex": page_index,
            "country": "US",       # Target market: United States
            "currency": "USD",
            "lang": "en",
            "filter": "orders, price",    # Filter by orders
            "sortBy": "desc"       # Descending: highest orders first
        }
        try:
            response = requests.get(SEARCH_API_URL, headers=API_HEADERS, params=params)
            print(f"🔍 Searching '{keyword}' (page {page_index}): status {response.status_code}")
            if response.status_code == 200:
                data = response.json()
                items = data.get("data", {}).get("itemList", [])
                print(f"📩 Found {len(items)} items for '{keyword}' on page {page_index}")
                for item in items:
                    try:
                        price = float(item.get("targetSalePrice", "0"))
                    except Exception:
                        price = 0.0
                    try:
                        rating = float(item.get("score", "0"))
                    except Exception:
                        rating = 0.0
                    orders_str = item.get("orders", "0").replace("+", "").replace(",", "")
                    try:
                        orders = int(orders_str)
                    except Exception:
                        orders = 0
                    product = {
                        "Product Name": item.get("title", "N/A"),
                        "Price": price,
                        "Orders": orders,
                        "Rating": rating,
                        "Item ID": item.get("itemId", ""),
                        "URL": f"https://www.aliexpress.com/item/{item.get('itemId', '')}.html",
                        "Category ID": item.get("cateId", "")
                    }
                    all_products.append(product)
            else:
                print(f"❌ Error fetching '{keyword}': {response.text}")
        except Exception as e:
            print(f"❌ Exception fetching '{keyword}' (page {page_index}): {e}")
        time.sleep(1)
    return all_products

# --------------------------------------------------
# Function to Filter Winning Products
# --------------------------------------------------
def analyze_winning_products(products):
    """
    Filters products based on winning criteria.
    """
    winning = []
    for prod in products:
        if (prod["Orders"] >= MIN_ORDERS and
            prod["Rating"] >= MIN_RATING and
            prod["Price"] <= MAX_PRICE):
            winning.append(prod)
    winning = sorted(winning, key=lambda x: x["Orders"], reverse=True)
    return winning

# --------------------------------------------------
# Function to Save Data to an Excel File
# --------------------------------------------------
def save_to_excel(products, filename="winning_products.xlsx"):
    if products:
        df = pd.DataFrame(products)
        with pd.ExcelWriter(filename) as writer:
            df.to_excel(writer, index=False, sheet_name="WinningProducts")
        print(f"✅ Data successfully saved to {filename}")
    else:
        print("⚠️ No winning products found; nothing saved.")

# --------------------------------------------------
# Main Workflow
# --------------------------------------------------
def main():
    all_products = []
    
    # Loop through each keyword and fetch products (1 page per query)
    for query in SEARCH_QUERIES:
        products = fetch_products(query, pages=1)
        all_products.extend(products)
    
    print(f"Total products fetched: {len(all_products)}")
    
    # Filter products using winning criteria
    winning_products = analyze_winning_products(all_products)
    print(f"Total winning products: {len(winning_products)}")
    
    # Save winning products to an Excel file
    save_to_excel(winning_products)

if __name__ == "__main__":
    main()
