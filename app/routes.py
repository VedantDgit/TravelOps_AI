from flask import Blueprint, request, jsonify

from app.utils import predict_flight_price

api = Blueprint(
    "api",
    __name__
)


@api.route("/")
def home():

    return {
        "project": "TravelOps AI",
        "status": "Running",
        "version": "1.0.0"
    }


@api.route("/health")
def health():

    return {
        "status": "Healthy",
        "models": "Loaded Successfully"
    }

@api.route("/predict-flight-price", methods=["POST"])
def predict_price():

    try:

        # Receive JSON
        data = request.get_json()

        # Prediction
        predicted_price = predict_flight_price(data)

        # Response
        return jsonify({
            "success": True,
            "predicted_price": predicted_price
        })

    except Exception as e:

        return jsonify({
            "success": False,
            "error": str(e)
        }), 400

