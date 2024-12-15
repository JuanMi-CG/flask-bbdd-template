from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_mail import Mail
from flask_wtf.csrf import CSRFProtect
from flask_jwt_extended import JWTManager
from dotenv import load_dotenv
import os

# Carga variables de entorno
load_dotenv()

# Inicialización de extensiones
db = SQLAlchemy()
migrate = Migrate()
mail = Mail()
jwt = JWTManager()
csrf = CSRFProtect()

def create_app():
    app = Flask(__name__)
    try:
        app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        app.config['SQLALCHEMY_ECHO'] = True  # For detailed connection logs

        app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
        app.config['MAIL_SERVER'] = os.getenv('MAIL_SERVER')
        app.config['MAIL_PORT'] = os.getenv('MAIL_PORT')
        app.config['MAIL_USE_TLS'] = os.getenv('MAIL_USE_TLS') == 'True'
        app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
        app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
        app.config['JWT_SECRET_KEY'] = os.getenv('SECRET_KEY')

        # Inicializar extensiones con la app
        db.init_app(app)
        migrate.init_app(app, db)
        mail.init_app(app)
        jwt.init_app(app)
        csrf.init_app(app)

        # Register the blueprint
        from .routes import main
        app.register_blueprint(main)


        with app.app_context():
            db.create_all()

        print("Flask app initialized successfully.")

    except Exception as e:
        print(f"Error initializing Flask app: {e}")

    return app
