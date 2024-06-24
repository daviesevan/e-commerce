from flask import Flask
from .config import ApplicationConfiguration
from .models import db
from flask_cors import CORS
from flask_jwt_extended import JWTManager

jwt = JWTManager()

def create_app():

    app = Flask(__name__)
    app.config.from_object(ApplicationConfiguration)

    jwt.init_app(app)
    db.init_app(app)
    CORS(app, supports_credentials=True)

    # Migrate(app, db)
    # Register blueprints 
    from app.admin.auth.routes import admin_auth_bp
    from app.inventory.routes import inventory_bp


    app.register_blueprint(admin_auth_bp)
    app.register_blueprint(inventory_bp)

    with app.app_context():
        db.create_all()

    return app