from app import ma
from .model import {{cookiecutter.first_entity_name|capitalize}}


class {{cookiecutter.first_entity_name|capitalize}}Schema(ma.SQLAlchemyAutoSchema):
    """{{cookiecutter.first_entity_name|capitalize}}"""

    class Meta:
        model = {{cookiecutter.first_entity_name|capitalize}}
