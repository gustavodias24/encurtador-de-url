from flask.blueprints import Blueprint
from flask import request, render_template
from validators import url
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

write_bp = Blueprint("write_bp", __name__)


@write_bp.route("/encurtar", methods=["GET", "POST"])
def encurtar():

    # 0 sem erro 1 com erro
    error = 1
    resultado = ""
    alias_link = ""

    dados = request.form

    if url(dados.get("url")):

        alias_link = dados.get("alias").lower()

        if alias_link:
            if col.find_one({"alias": alias_link}):
                resultado = "Essa alias já esta sendo utilizada."
            else:
                col.insert_one({
                    "alias": alias_link.replace(" ", "%20"),
                    "redirecionar": dados.get("url")
                })
                error = 0
                resultado = f"{request.host}/{alias_link}"
        else:
            resultado = "digite um alias para o seu link."
    else:
        resultado = "url inválida."

    obj_resp = {
        "resultado": resultado,
        "error": error,
        "alias": alias_link
    }
    return render_template("index.html", obj_resp=obj_resp)
