import os
import sys
import joblib
import pandas as pd
import sklearn.compose._column_transformer
from app.logger import logger


class _RemainderColsList(list):
    pass

sklearn.compose._column_transformer._RemainderColsList = _RemainderColsList
setattr(sys.modules['__main__'], '_RemainderColsList', _RemainderColsList)

from app.config import MODEL_DIR


flight_model = joblib.load(
    os.path.join(
        MODEL_DIR,
        "flight_price_model.pkl"
    )
)

flight_preprocessor = joblib.load(
    os.path.join(
        MODEL_DIR,
        "flight_preprocessor.pkl"
    )
)

gender_model = joblib.load(
    os.path.join(
        MODEL_DIR,
        "gender_model.pkl"
    )
)

gender_scaler = joblib.load(
    os.path.join(
        MODEL_DIR,
        "gender_scaler.pkl"
    )
)

gender_label_encoder = joblib.load(
    os.path.join(
        MODEL_DIR,
        "gender_label_encoder.pkl"
    )
)

recommendation_model = joblib.load(
    os.path.join(
        MODEL_DIR,
        "recommendation_model.pkl"
    )
)

recommendation_preprocessor = joblib.load(
    os.path.join(
        MODEL_DIR,
        "recommendation_preprocessor.pkl"
    )
)

recommendation_dataset = joblib.load(
    os.path.join(
        MODEL_DIR,
        "recommendation_dataset.pkl"
    )
)

logger.info("=" * 50)
logger.info("All models loaded successfully.")
logger.info("Flight Price Model Loaded")
logger.info("Gender Model Loaded")
logger.info("Recommendation Model Loaded")
logger.info("=" * 50)



def predict_flight_price(data):

    try:

        logger.info(f"Flight Price Prediction Request: {data}")

        input_df = pd.DataFrame([data])

        if "date" in input_df.columns:
            date_series = pd.to_datetime(input_df["date"])

            if "year" not in input_df.columns:
                input_df["year"] = date_series.dt.year

            if "month" not in input_df.columns:
                input_df["month"] = date_series.dt.month

            if "day" not in input_df.columns:
                input_df["day"] = date_series.dt.day

            if "day_of_week" not in input_df.columns:
                input_df["day_of_week"] = date_series.dt.day_name()

        processed_data = flight_preprocessor.transform(input_df)

        prediction = flight_model.predict(processed_data)

        logger.info(f"Predicted Flight Price: {prediction[0]}")

        return round(float(prediction[0]), 2)

    except Exception as e:
        logger.exception("Flight Price Prediction Failed")
        raise

def predict_gender(data):

    try:

        logger.info(f"Gender Prediction Request: {data}")

        input_df = pd.DataFrame([data])

        input_df = pd.get_dummies(
            input_df,
            columns=["company"],
            drop_first=True,
            dtype=int
        )

        expected_columns = [
            "age",
            "company_Acme Factory",
            "company_Monsters CYA",
            "company_Umbrella LTDA",
            "company_Wonka Company"
        ]

        for col in expected_columns:
            if col not in input_df.columns:
                input_df[col] = 0

        input_df = input_df[expected_columns]

        scaled = gender_scaler.transform(input_df)

        pred = gender_model.predict(scaled)

        gender = gender_label_encoder.inverse_transform(pred)

        # 👇 Prediction ke baad
        logger.info(f"Predicted Gender: {gender[0]}")

        return gender[0]

    except Exception:
        logger.exception("Gender Prediction Failed")
        raise

def recommend_for_user(
    user_code,
    dataset,
    preprocessor,
    model,
    top_n=5
):

    user_trips = dataset[
        dataset["userCode"] == user_code
    ]

    if user_trips.empty:
        return f"User Code {user_code} not found in database."

    sample_trip = user_trips.iloc[:1]

    sample_prep = preprocessor.transform(
        sample_trip
    )

    distances, indices = model.kneighbors(
        sample_prep,
        n_neighbors=top_n + 1
    )

    neighbor_indices = indices[0][1:]
    neighbor_distances = distances[0][1:]

    recommendations = dataset.iloc[
        neighbor_indices
    ].copy()

    recommendations["similarity_score"] = (
        1 - neighbor_distances
    ).round(4)

    result = recommendations[
        [
            "userCode",
            "hotelName",
            "place",
            "hotelPrice",
            "days",
            "flightType",
            "similarity_score"
        ]
    ]

    return result.head(top_n)

def predict_recommendation(
    user_code,
    top_n=5
):

    try:

        logger.info(f"Recommendation Request for User: {user_code}")

        recommendations = recommend_for_user(
            user_code=user_code,
            dataset=recommendation_dataset,
            preprocessor=recommendation_preprocessor,
            model=recommendation_model,
            top_n=top_n
        )

        # If user not found
        if isinstance(recommendations, str):
            logger.warning(recommendations)
            return recommendations

        logger.info(
            f"Recommendation Generated Successfully for User: {user_code}"
        )

        logger.info(
            f"Total Recommendations Returned: {len(recommendations)}"
        )

        return recommendations

    except Exception as e:

        logger.exception(
            f"Recommendation Failed for User: {user_code}"
        )

        raise