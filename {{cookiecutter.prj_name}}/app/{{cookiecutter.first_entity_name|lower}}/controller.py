from flask_restx import Resource
from flask import request
from flask_restx import Namespace
from flask_accepts import accepts, responds
from flask.wrappers import Response
from typing import List

from .schema import {{cookiecutter.first_entity_name|capitalize}}Schema
from .model import {{cookiecutter.first_entity_name|capitalize}}
from .service import {{cookiecutter.first_entity_name|capitalize}}Service

api = Namespace("{{cookiecutter.first_entity_name|capitalize}}", description="{{cookiecutter.first_entity_name|capitalize}} information")


@api.route("/")
class {{cookiecutter.first_entity_name|capitalize}}Resource(Resource):
    """{{cookiecutter.first_entity_name|capitalize}}s"""

    @responds(schema={{cookiecutter.first_entity_name|capitalize}}Schema(many=True))
    def get(self) -> List[{{cookiecutter.first_entity_name|capitalize}}]:
        """Get all {{cookiecutter.first_entity_name|capitalize}}s"""

        return {{cookiecutter.first_entity_name|capitalize}}Service.get_all()

    @accepts(schema={{cookiecutter.first_entity_name|capitalize}}Schema, api=api)
    @responds(schema={{cookiecutter.first_entity_name|capitalize}}Schema)
    def post(self):
        """Create a Single {{cookiecutter.first_entity_name|capitalize}}"""

        return {{cookiecutter.first_entity_name|capitalize}}Service.create(request.parsed_obj)


@api.route("/<int:id>")
@api.param("id", "{{cookiecutter.first_entity_name|capitalize}} database ID")
class {{cookiecutter.first_entity_name|capitalize}}IdResource(Resource):
    @responds(schema={{cookiecutter.first_entity_name|capitalize}}Schema)
    def get(self, id: int) -> {{cookiecutter.first_entity_name|capitalize}}:
        """Get Single {{cookiecutter.first_entity_name|capitalize}}"""

        return {{cookiecutter.first_entity_name|capitalize}}Service.get_by_id(id)

    def delete(self, id: int) -> Response:
        """Delete Single {{cookiecutter.first_entity_name|capitalize}}"""

        from flask import jsonify

        id = {{cookiecutter.first_entity_name|capitalize}}Service.delete_by_id(id)
        return jsonify(dict(status="Success", id=id))

    @accepts(schema={{cookiecutter.first_entity_name|capitalize}}Schema, api=api)
    @responds(schema={{cookiecutter.first_entity_name|capitalize}}Schema)
    def put(self, id: int) -> {{cookiecutter.first_entity_name|capitalize}}:
        """Update Single {{cookiecutter.first_entity_name|capitalize}}"""

        changes = request.parsed_obj
        {{cookiecutter.first_entity_name|lower}} = {{cookiecutter.first_entity_name|capitalize}}Service.get_by_id(id)
        return {{cookiecutter.first_entity_name|capitalize}}Service.update({{cookiecutter.first_entity_name|lower}}, changes)
