import pandas as pd

# -----------------------------
# Feature Columns Definition
# -----------------------------
NUMERIC_FEATURES = ["area", "bedrooms", "bathrooms"]
CATEGORICAL_FEATURES = ["city"]


# -----------------------------
# Feature Engineering Function
# -----------------------------
def build_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Central feature engineering pipeline.
    Ensures same transformations in training & inference.
    """

    df = df.copy()

    # -------------------------
    # Handle missing values
    # -------------------------
    df["area"] = df["area"].fillna(df["area"].median())
    df["bedrooms"] = df["bedrooms"].fillna(df["bedrooms"].median())
    df["bathrooms"] = df["bathrooms"].fillna(df["bathrooms"].median())
    df["city"] = df["city"].fillna("Unknown")

    # -------------------------
    # Feature Engineering
    # -------------------------

    # Price-relevant interaction feature
    df["rooms_total"] = df["bedrooms"] + df["bathrooms"]

    # Area per room (strong real estate signal)
    df["area_per_room"] = df["area"] / (df["rooms_total"] + 1)

    # Log transform (helps stabilize price distribution in training)
    df["log_area"] = (df["area"] + 1).apply(lambda x: float(x) ** 0.5)

    return df


# -----------------------------
# Feature Selector for Model
# -----------------------------
def get_feature_matrix(df: pd.DataFrame) -> pd.DataFrame:
    """
    Returns final feature set used for ML model training/inference.
    """

    df = build_features(df)

    feature_columns = NUMERIC_FEATURES + [
        "rooms_total",
        "area_per_room",
        "log_area",
        "city"
    ]

    return df[feature_columns]