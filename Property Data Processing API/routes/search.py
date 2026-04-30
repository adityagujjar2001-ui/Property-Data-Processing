from flask import Blueprint, request, jsonify
from routes.upload import DATA_STORE

search_bp = Blueprint("search", __name__)

@search_bp.route("/properties", methods=["GET"])
def search_properties():
    """
    Search and filter properties
    ---
    get:
      summary: Search properties
      description: Search properties by city and/or maximum price
      parameters:
        - in: query
          name: city
          type: string
          description: Filter by city name
        - in: query
          name: max_price
          type: number
          description: Filter by maximum price
      responses:
        200:
          description: List of matching properties
        400:
          description: No data uploaded
    """
    df = DATA_STORE.get("df")

    if df is None:
        return jsonify({"error": "No data uploaded"}), 400

    city = request.args.get("city")
    max_price = request.args.get("max_price")

    filtered = df

    if city:
        filtered = filtered[filtered["city"] == city]

    if max_price:
        filtered = filtered[filtered["price"] <= float(max_price)]

    return jsonify(filtered.to_dict(orient="records"))