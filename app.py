from flask import Flask
from flasgger import Swagger
from routes.upload import upload_bp
from routes.analytics import analytics_bp
from routes.search import search_bp
from utils.logger import setup_logger
from routes.predicts import predict_bp

app = Flask(__name__)
swagger = Swagger(app, template={
    "swagger": "2.0",
    "info": {
        "title": "Property Data Processing API",
        "description": "API for processing and analyzing property data with ML predictions",
        "version": "1.0.0"
    }
})
logger = setup_logger()

# Register Blueprints
app.register_blueprint(upload_bp, url_prefix="/api")
app.register_blueprint(analytics_bp, url_prefix="/api")
app.register_blueprint(search_bp, url_prefix="/api")
app.register_blueprint(predict_bp, url_prefix="/api")

# @app.route("/")
# def home():
#     """
#     Home endpoint
#     ---
#     get:
#       summary: Check if API is running
#       description: Returns a status message confirming the API is operational
#       responses:
#         200:
#           description: API is running
#           schema:
#             properties:
#               message:
#                 type: string
#                 example: Property Data Processing API is running
#     """
#     return {
#         "message": "Property Data Processing API is running"
#     }

if __name__ == "__main__":
    logger.info("Starting Property API server...")
    app.run(host="0.0.0.0", port=5000, debug=True)