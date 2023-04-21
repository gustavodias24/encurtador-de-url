from flask import Blueprint, jsonify, make_response, redirect, request
import api


redlinks_bp = Blueprint("redlinks_bp", __name__)


@redlinks_bp.route("/", methods=["GET"])
def default_page():
    return jsonify({"msg": "Pagina em construcao..."})


@redlinks_bp.route("/<string:alias>", methods=["GET"])
def rediLink(alias):
    if link := api.col.find_one({"alias": alias}):
        return redirect(link["redirecionar"])
    return make_response(jsonify({"msg": "not found"}), 404)
