from flask import Blueprint, request, jsonify
from services.predictor import predict_price

predict_bp = Blueprint("predict", __name__)

@predict_bp.route("/predict-price", methods=["GET"])
def predict():
    """
    Predict property price using ML model
    ---
    get:
      summary: Predict property price
      description: Predicts property price based on city, area, bedrooms, and bathrooms
      parameters:
        - in: query
          name: city
          type: string
          required: true
          description: City name
        - in: query
          name: area
          type: number
          required: true
          description: Property area in square units
        - in: query
          name: bedrooms
          type: integer
          required: true
          description: Number of bedrooms
        - in: query
          name: bathrooms
          type: integer
          required: true
          description: Number of bathrooms
      responses:
        200:
          description: Predicted price
          schema:
            properties:
              predicted_price:
                type: number
    """
    city = request.args.get("city")
    area = float(request.args.get("area"))
    bedrooms = int(request.args.get("bedrooms"))
    bathrooms = int(request.args.get("bathrooms"))

    price = predict_price(city, area, bedrooms, bathrooms)

    return jsonify({
        "predicted_price": price
    })