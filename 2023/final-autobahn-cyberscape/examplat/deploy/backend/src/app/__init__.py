from flask import Flask
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from .config import get_config

cors = CORS()
db = SQLAlchemy()
migrate = Migrate()
bcrypt = Bcrypt()

def create_app(config_name=None):
    app = Flask(__name__)
    app.config.from_object(get_config(config_name))

    from .api import api_bp

    app.register_blueprint(api_bp)

    cors.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)
    return app

app = create_app()
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)