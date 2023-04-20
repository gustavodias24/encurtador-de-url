from flask.blueprints import Blueprint
from flask import jsonify, request, make_response
from flask_restful import Resource, Api
from validators import url
import json
import os

crud_bp = Blueprint("crud_bp", __name__)
api = Api(crud_bp)


class crud_link(Resource):
    def __init__(self):
        self.path_file = os.path.join(os.getcwd(), "api","blueprints", "raw-data", "data.json")

    def post(self):
        data = request.args.get("url")
        if url(data):
            with open(self.path_file, "r") as file:
                links_existentes = json.loads(file.read())
                alias_link = request.args.get("alias")
                if alias_link:
                    # verificar se alias do link já foi utlizado
                    for link in links_existentes:
                        if link["alias"] == alias_link:
                            return make_response(jsonify({"msg": "alias já utilizada."}), 400)
                else:
                    return make_response(jsonify({"msg": "digite um alias para o seu link."}), 400)

                with open(self.path_file, "w") as file_update:
                    novo_link = {
                        "alias": alias_link,
                        "redirecionar": data
                    }

                    links_existentes.append(novo_link)
                    json.dump(links_existentes, file_update)
                    return jsonify({"teu_link": f"https://www.benicio.cloud/{alias_link}"})
        else:
            return make_response(jsonify({"msg": "url inválida."}), 400)


api.add_resource(crud_link, "/urls")
