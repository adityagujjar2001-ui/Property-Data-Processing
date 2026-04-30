from flask import Blueprint, request, jsonify
import pandas as pd
from services.data_cleaning import clean_data

upload_bp = Blueprint("upload", __name__)

DATA_STORE = {}

@upload_bp.route("/upload", methods=["POST"])
def upload_file():
    """
    Upload and process a CSV file
    ---
    post:
      summary: Upload property data CSV file
      description: Upload a CSV file with property data for processing and cleaning
      parameters:
        - in: formData
          name: file
          type: file
          required: true
          description: CSV file with property data
      responses:
        200:
          description: File uploaded and processed successfully
          schema:
            properties:
              message:
                type: string
              rows:
                type: integer
    """
    file = request.files["file"]

    df = pd.read_csv(file)
    cleaned_df = clean_data(df)

    DATA_STORE["df"] = cleaned_df

    return jsonify({
        "message": "File uploaded and processed successfully",
        "rows": len(cleaned_df)
    })