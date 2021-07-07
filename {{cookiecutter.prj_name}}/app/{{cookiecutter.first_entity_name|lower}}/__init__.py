from .model import {{cookiecutter.first_entity_name|capitalize}}
from .schema import {{cookiecutter.first_entity_name|capitalize}}Schema


def register_routes(root_api, root="/api"):
    from .controller import api as {{cookiecutter.first_entity_name|lower}}_api

    root_api.add_namespace({{cookiecutter.first_entity_name|lower}}_api, path=f"{root}/{{cookiecutter.first_entity_name|lower}}")
