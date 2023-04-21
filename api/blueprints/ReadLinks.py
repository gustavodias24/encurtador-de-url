from flask import Blueprint, jsonify, make_response, redirect, render_template
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


readLinks_bp = Blueprint("redlinks_bp", __name__)


@readLinks_bp.route("/", methods=["GET"])
def default_page():
    obj_resp = {
        "resultado": "",
        "error": ""
    }
    return render_template("index.html", obj_resp=obj_resp)


@readLinks_bp.route("/<string:alias>", methods=["GET"])
def rediLink(alias):
    if dados := col.find_one({"alias": alias}):
        return redirect(dados["redirecionar"])
    return make_response(jsonify({"msg": "link not found"}), 404)
