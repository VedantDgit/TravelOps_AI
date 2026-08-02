from flask import Blueprint, request, jsonify

from app.utils import (
    predict_flight_price,
    predict_gender
)

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

        data = request.get_json()

        # Check if request body exists
        if not data:
            return jsonify({
                "success": False,
                "message": "Request body is missing."
            }), 400

        # Required fields
        required_fields = [
            "company",
            "gender",
            "age",
            "from",
            "to",
            "flightType",
            "agency",
            "distance",
            "time",
            "year",
            "month",
            "day",
            "day_of_week"
        ]

        # Check missing fields
        missing_fields = []

        for field in required_fields:

            if field not in data:

                missing_fields.append(field)

        if len(missing_fields) > 0:

            return jsonify({
                "success": False,
                "message": "Missing required fields.",
                "missing_fields": missing_fields
            }), 400

        # Prediction
        predicted_price = predict_flight_price(data)

        return jsonify({
            "success": True,
            "predicted_price": predicted_price
        })

    except Exception as e:

        return jsonify({
            "success": False,
            "error": str(e)
        }), 500
        
@api.route("/predict-gender", methods=["POST"])
def gender_prediction():

    try:

        data = request.get_json()

        if not data:
            return jsonify({
                "success": False,
                "message": "Request body is missing."
            }), 400

        required_fields = [
            "company",
            "age"
        ]

        missing = []

        for field in required_fields:

            if field not in data:

                missing.append(field)

        if len(missing) > 0:

            return jsonify({
                "success": False,
                "message": "Missing required fields.",
                "missing_fields": missing
            }), 400

        prediction = predict_gender(data)

        return jsonify({
            "success": True,
            "predicted_gender": prediction
        })

    except Exception as e:

        return jsonify({
            "success": False,
            "error": str(e)
        }), 500


