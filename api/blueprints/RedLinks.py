from flask import Blueprint, jsonify, make_response, redirect, request
from decouple import config
from pymongo import MongoClient

client = MongoClient(
    "mongodb+srv://{}:{}@clusterurls.wwd3kag.mongodb.net/?retryWrites=true&w=majority".format(
        config("USER"),
        config("PASS")
    )
)

db = client["dataGeral"]
col = db["colUrls"]



redlinks_bp = Blueprint("redlinks_bp", __name__)


@redlinks_bp.route("/", methods=["GET"])
def default_page():
    return jsonify({"msg": "Pagina em construcao..."})


@redlinks_bp.route("/<string:alias>", methods=["GET"])
def rediLink(alias):
    if link := col.find_one({"alias": alias}):
        return redirect(link["redirecionar"])
    return make_response(jsonify({"msg": "not found"}), 404)
