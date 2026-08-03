from flask import Flask
from flask_cors import CORS

from app.logger import logger
from app.routes import api


def initialize_swagger(app_instance: Flask):
    """
    Initialize Swagger Documentation.
    """

    app_instance.config["SWAGGER"] = {
        "title": "TravelOps AI API",
        "description": "REST API for Flight Price Prediction, Gender Prediction and Hotel Recommendation",
        "version": "1.0.0",
        "uiversion": 3,
    }

    try:
        from flasgger import Swagger

        logger.info("Swagger Initialized Successfully")
        return Swagger(app_instance)

    except ImportError as exc:
        logger.warning(f"Swagger disabled: {exc}")
        return None

    except Exception as exc:
        logger.exception(f"Swagger initialization failed: {exc}")
        return None


# ==========================================
# Create Flask Application
# ==========================================

app = Flask(__name__)

# Enable CORS
CORS(app)

logger.info("CORS Enabled")

# Initialize Swagger
initialize_swagger(app)

# Register API Blueprint
app.register_blueprint(api)

logger.info("=" * 60)
logger.info("TravelOps AI Server Started Successfully")
logger.info("API Blueprint Registered")
logger.info("All Models Loaded Successfully")
logger.info("=" * 60)

# Print Registered Routes
print("=" * 60)
print("Registered Routes")
print("=" * 60)
print(app.url_map)
print("=" * 60)

logger.info("Registered Routes:")
logger.info(app.url_map)

# ==========================================
# Run Server
# ==========================================

if __name__ == "__main__":
    logger.info("Flask Development Server Running...")
    app.run(debug=True)