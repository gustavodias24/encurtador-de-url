from flask.blueprints import Blueprint
from flask import jsonify, request, make_response
from flask_restful import Resource, Api
from validators import url
import json
import api


crud_bp = Blueprint("crud_bp", __name__)
api_crud = Api(crud_bp)


class crud_link(Resource):
    def get(self):

        dados = request.args

        if url(dados.get("url")):

            alias_link = dados.get("alias")

            if alias_link:
                # verificar se alias do link já foi utlizado
                if api.col.find_one({"alias": alias_link}):
                    return make_response(jsonify({"msg": "alias já utilizada."}), 400)
            else:
                return make_response(jsonify({"msg": "digite um alias para o seu link."}), 400)

            api.col.insert_one({
                "alias": alias_link,
                "redirecionar": dados.get("url")
            })

            return jsonify({"teu_link": f"{request.host}/{alias_link}"})
        else:
            return make_response(jsonify({"msg": "url inválida."}), 400)


api_crud.add_resource(crud_link, "/urls")
