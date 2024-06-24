from flask import Blueprint, jsonify
from app.models.inventory import Inventory

inventory_bp = Blueprint(
    'inventory',
    __name__,
    url_prefix='/inventory'
)

@inventory_bp.get('/all')
def all():
    inventory_items = Inventory.query.all()
    inventory_list = [{
        'id': item.id,
        'title': item.title,
        'price': item.price,
        'description': item.description,
        'category': item.category,
        'image': item.image
    } for item in inventory_items]

    return jsonify(inventory_list)