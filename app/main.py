from flask import Flask
from flask_cors import CORS

from app.routes import api


def initialize_swagger(app_instance: Flask):
    """Initialize Swagger only when Flasgger is available."""
    app_instance.config["SWAGGER"] = {
        "title": "TravelOps AI API",
        "description": "REST API for Flight Price Prediction, Gender Prediction and Hotel Recommendation",
        "version": "1.0.0",
        "uiversion": 3,
    }

    try:
        from flasgger import Swagger
    except ImportError as exc:
        print(f"Swagger disabled: {exc}")
        return None

    try:
        return Swagger(app_instance)
    except Exception as exc:  # pragma: no cover - defensive fallback
        print(f"Swagger initialization skipped: {exc}")
        return None


# Create Flask App
app = Flask(__name__)

# Enable CORS
CORS(app)

# Initialize Swagger
initialize_swagger(app)

# Register Blueprint
app.register_blueprint(api)

# Print all registered routes
print("=" * 60)
print("Registered Routes")
print("=" * 60)
print(app.url_map)
print("=" * 60)

# Run Application
if __name__ == "__main__":
    app.run(debug=True)
