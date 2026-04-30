from flask import Blueprint, jsonify
from services.analytics import get_summary, detect_outliers
from routes.upload import DATA_STORE

analytics_bp = Blueprint("analytics", __name__)

@analytics_bp.route("/summary", methods=["GET"])
def summary():
    """
    Get data summary statistics
    ---
    get:
      summary: Get summary statistics
      description: Returns statistical summary of uploaded property data
      responses:
        200:
          description: Summary statistics
        400:
          description: No data uploaded
    """
    df = DATA_STORE.get("df")

    if df is None:
        return jsonify({"error": "No data uploaded"}), 400

    return jsonify(get_summary(df))


@analytics_bp.route("/outliers", methods=["GET"])
def outliers():
    """
    Detect outliers in property data
    ---
    get:
      summary: Detect outliers
      description: Identifies outlier records in the uploaded property data
      responses:
        200:
          description: List of outlier records
        400:
          description: No data uploaded
    """
    df = DATA_STORE.get("df")

    if df is None:
        return jsonify({"error": "No data uploaded"}), 400

    result = detect_outliers(df)
    return jsonify(result.to_dict(orient="records"))