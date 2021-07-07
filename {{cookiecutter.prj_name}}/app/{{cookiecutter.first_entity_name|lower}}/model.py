from sqlalchemy import Integer, Column, String
from app import db  # noqa
from .interface import {{cookiecutter.first_entity_name|capitalize}}Interface


class {{cookiecutter.first_entity_name|capitalize}}(db.Model):
    """A {{cookiecutter.first_entity_name|capitalize}}"""

    __tablename__ = "{{cookiecutter.first_entity_name|lower}}"
    id = Column(Integer(), primary_key=True)
    name = Column(String(255))
    description = Column(String(255))

    def update(self, changes: {{cookiecutter.first_entity_name|capitalize}}Interface):
        for key, val in changes.items():
            setattr(self, key, val)
        return
