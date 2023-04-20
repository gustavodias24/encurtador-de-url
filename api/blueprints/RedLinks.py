from flask import Blueprint, jsonify, make_response, redirect
import os
import json

redlinks_bp = Blueprint("redlinks_bp", __name__)


@redlinks_bp.route("/", methods=["GET"])
def default_page():
    return jsonify({"msg": "Pagina em construcao..."})


@redlinks_bp.route("/<string:alias>", methods=["GET"])
def rediLink(alias):
    with open(os.path.join(os.getcwd(), "api","blueprints", "raw-data", "data.json"), "r") as file:
        for link in json.loads(file.read()):
            if link["alias"] == alias:
                return redirect(link["redirecionar"])
        return make_response(jsonify({"msg": "not found"}), 404)
