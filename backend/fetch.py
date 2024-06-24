import requests
from flask import Flask
from app import db, create_app
from app.models.inventory import Inventory

# Create the Flask app and configure it
app = create_app()

def fetch_and_store_inventory():
    url = 'https://fakestoreapi.com/products'
    response = requests.get(url)

    if response.status_code == 200:
        products = response.json()

        with app.app_context():
            for product in products:
                inventory_item = Inventory(
                    id=product['id'],
                    title=product['title'],
                    price=product['price'] * 100,
                    description=product['description'],
                    category=product['category'],
                    image=product['image']
                )
                db.session.add(inventory_item)

            db.session.commit()
            print("Inventory items have been added to the database.")
    else:
        print(f"Failed to fetch data from API. Status code: {response.status_code}")

if __name__ == "__main__":
    fetch_and_store_inventory()
