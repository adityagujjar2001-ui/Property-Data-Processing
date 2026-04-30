import pickle
import pandas as pd
from ml.features import get_feature_matrix

# Load model once (production-style)
with open("ml/model.pkl", "rb") as f:
    model = pickle.load(f)


def predict_price(city, area, bedrooms, bathrooms):
    df = pd.DataFrame([{
        "city": city,
        "area": area,
        "bedrooms": bedrooms,
        "bathrooms": bathrooms
    }])

    df = get_feature_matrix(df)

    prediction = model.predict(df)[0]

    return round(float(prediction), 2)