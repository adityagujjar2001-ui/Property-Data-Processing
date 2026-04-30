import pandas as pd

def get_summary(df: pd.DataFrame):
    return {
        "avg_price": float(df["price"].mean()),
        "median_price": float(df["price"].median()),
        "max_price": float(df["price"].max()),
        "min_price": float(df["price"].min())
    }


def detect_outliers(df: pd.DataFrame):
    q1 = df["price_per_sqm"].quantile(0.25)
    q3 = df["price_per_sqm"].quantile(0.75)
    iqr = q3 - q1

    lower = q1 - 1.5 * iqr
    upper = q3 + 1.5 * iqr

    return df[(df["price_per_sqm"] < lower) | (df["price_per_sqm"] > upper)]