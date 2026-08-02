import os
import sys
import joblib
import pandas as pd
import sklearn.compose._column_transformer

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

print("All models loaded successfully.")

def predict_flight_price(data):

    # Convert JSON to DataFrame
    input_df = pd.DataFrame([data])

    # Derive date features if 'date' is provided
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

    # Apply preprocessing
    processed_data = flight_preprocessor.transform(input_df)

    # Predict
    prediction = flight_model.predict(processed_data)

    return round(float(prediction[0]), 2)

def predict_gender(data):

    # Convert JSON to DataFrame
    input_df = pd.DataFrame([data])

    # Scale features
    scaled_data = gender_scaler.transform(input_df)

    # Predict encoded class
    prediction = gender_model.predict(scaled_data)

    # Convert label back to original class
    predicted_gender = gender_label_encoder.inverse_transform(prediction)

    return predicted_gender[0]