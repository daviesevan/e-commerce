from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Import all model modules
from .admin import Admin
from .inventory import Inventory
