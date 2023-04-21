from flask.blueprints import Blueprint
from flask import jsonify, request, make_response
from flask_restful import Resource, Api
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

crud_bp = Blueprint("crud_bp", __name__)
api = Api(crud_bp)


class crud_link(Resource):

    def post(self):

        dados = request.get_json()

        if url(dados.get("url")):

            alias_link = dados.get("alias").lower()

            if alias_link:
                if col.find_one({"alias": alias_link}):
                    return make_response(jsonify({"msg": "alias já utilizada."}), 400)

                col.insert_one({
                        "alias": alias_link.replace(" ", "%20"),
                        "redirecionar": dados.get("url")
                    })

                return jsonify({"teu_link": f"{request.host}/{alias_link}"})

            else:
                return make_response(jsonify({"msg": "digite um alias para o seu link."}), 400)
        else:
            return make_response(jsonify({"msg": "url inválida."}), 400)


api.add_resource(crud_link, "/urls")
