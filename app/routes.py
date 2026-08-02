from flask import Blueprint

api = Blueprint("api", __name__)

@api.route("/")
def home():
    return {"message": "TravelOps AI API Running Successfully 🚀"}

@api.route("/health")
def health():
    return {"status": "OK", "message": "API is healthy"}