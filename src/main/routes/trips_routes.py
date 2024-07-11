from flask import jsonify, Blueprint

# Criação de uma rota;

trips_routes_bp = Blueprint("trip_route", __name__)

@trips_routes_bp.route("/trips", methods=["POST"])
def create_trip():
    return jsonify({"salve": "pessoal"}), 200 