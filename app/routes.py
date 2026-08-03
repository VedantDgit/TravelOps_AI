from flask import Blueprint, request, jsonify
import time
from app.logger import logger
from app.utils import (
    predict_flight_price,
    predict_gender,
    predict_recommendation
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
    """
    Predict Flight Price
    ---
    tags:
      - Flight Prediction

    consumes:
      - application/json

    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            from:
              type: string
              example: Brasilia (DF)
            to:
              type: string
              example: Rio de Janeiro (RJ)
            flightType:
              type: string
              example: firstClass
            agency:
              type: string
              example: FlyingDrops
            distance:
              type: number
              example: 830
            time:
              type: number
              example: 2.5
            year:
              type: integer
              example: 2021
            month:
              type: integer
              example: 8
            day:
              type: integer
              example: 15
            day_of_week:
              type: string
              example: Sunday
            
    responses:
        200:
            description: Flight price predicted successfully        
    """
    start_time = time.time()     
    try:
        
        logger.info("Flight Price Prediction API Called")
         
        data = request.get_json()
        logger.info(f"Request Data: {data}")
        # Check if request body exists
        if not data:
            logger.warning("Request body is missing.")
            
            return jsonify({
                "success": False,
                "message": "Request body is missing."
            }), 400

        # Required fields
        required_fields = [

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
            logger.warning(f"Missing Fields: {missing_fields}")
            
            return jsonify({
                "success": False,
                "message": "Missing required fields.",
                "missing_fields": missing_fields
            }), 400

        prediction = predict_flight_price(data)
        execution_time = round(time.time() - start_time, 3)
        
        logger.info(f"Predicted Flight Price: {prediction}")
        logger.info(f"Execution Time: {execution_time} sec")

        
        return jsonify({
            "success": True,
            "message": "Flight price predicted successfully.",
            "predicted_price": prediction
        }), 200

    except Exception as e:
        logger.exception("Flight Price Prediction Failed")
        
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500
        
@api.route("/predict-gender", methods=["POST"])
def gender_prediction():
    """
    Predict Gender
    ---
    tags:
      - Gender Prediction

    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            company:
              type: string
              example: "Wonka Company"
            age:
              type: integer
              example: 25

    responses:
      200:
        description: Gender predicted successfully
      400:
        description: Invalid request
      500:
        description: Internal server error
    """

    start_time = time.time()

    try:

        logger.info("Gender Prediction API Called")

        data = request.get_json()

        logger.info(f"Request Data: {data}")

        if not data:

            logger.warning("Request body is missing.")

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

            logger.warning(f"Missing Fields: {missing}")

            return jsonify({
                "success": False,
                "message": "Missing required fields.",
                "missing_fields": missing
            }), 400

        # Validate age
        try:
            data["age"] = int(data["age"])

        except (ValueError, TypeError):

            logger.warning("Invalid age received.")

            return jsonify({
                "success": False,
                "message": "Invalid data type for 'age'. Expected an integer."
            }), 400

        prediction = predict_gender(data)

        execution_time = round(time.time() - start_time, 3)

        logger.info(f"Predicted Gender: {prediction}")
        logger.info(f"Execution Time: {execution_time} sec")

        return jsonify({
            "success": True,
            "message": "Gender predicted successfully.",
            "predicted_gender": prediction
        }), 200

    except Exception as e:

        logger.exception("Gender Prediction Failed")

        return jsonify({
            "success": False,
            "error": str(e)
        }), 500


print("Recommendation route loaded")


@api.route("/recommend-hotels", methods=["POST"])
def recommend_hotels():
    """
    Hotel Recommendation
    ---
    tags:
      - Hotel Recommendation

    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            userCode:
              type: integer
              example: 25

    responses:
      200:
        description: Hotel recommendations generated successfully
      404:
        description: User not found
      500:
        description: Internal server error
    """

    start_time = time.time()

    try:

        logger.info("Hotel Recommendation API Called")

        data = request.get_json()

        logger.info(f"Request Data: {data}")

        if not data:

            logger.warning("Request body is missing.")

            return jsonify({
                "success": False,
                "message": "Request body is missing."
            }), 400

        if "userCode" not in data:

            logger.warning("userCode is missing.")

            return jsonify({
                "success": False,
                "message": "userCode is required."
            }), 400

        try:

            user_code = int(data["userCode"])

        except (ValueError, TypeError):

            logger.warning("Invalid userCode received.")

            return jsonify({
                "success": False,
                "message": "userCode must be an integer."
            }), 400

        recommendations = predict_recommendation(
            user_code=user_code
        )

        if isinstance(recommendations, str):

            logger.warning(recommendations)

            return jsonify({
                "success": False,
                "message": recommendations
            }), 404

        execution_time = round(time.time() - start_time, 3)

        logger.info(
            f"Recommendations generated successfully for User: {user_code}"
        )

        logger.info(
            f"Execution Time: {execution_time} sec"
        )

        return jsonify({
            "success": True,
            "message": "Recommendations generated successfully.",
            "recommendations": recommendations.to_dict(
                orient="records"
            )
        }), 200

    except Exception as e:

        logger.exception("Hotel Recommendation Failed")

        return jsonify({
            "success": False,
            "message": "Internal Server Error",
            "error": str(e)
        }), 500
