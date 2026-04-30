import pandas as pd

def clean_data(df: pd.DataFrame):

    # Drop duplicates
    df = df.drop_duplicates()

    # Fill missing values
    df['price'] = df['price'].fillna(df['price'].median())
    df['area'] = df['area'].fillna(df['area'].median())

    # Normalize area to sqm (assuming sqft input)
    df['area_sqm'] = df['area'] * 0.092903

    # Feature: price per sqm
    df['price_per_sqm'] = df['price'] / df['area_sqm']

    # Remove extreme outliers (basic filter)
    df = df[df['price_per_sqm'] < df['price_per_sqm'].quantile(0.99)]

    return df