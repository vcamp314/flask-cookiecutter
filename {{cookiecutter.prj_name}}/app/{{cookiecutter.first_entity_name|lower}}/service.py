from typing import List

from app import db  # noqa
from .model import {{cookiecutter.first_entity_name|capitalize}}
from .interface import {{cookiecutter.first_entity_name|capitalize}}Interface


class {{cookiecutter.first_entity_name|capitalize}}Service:
    @staticmethod
    def get_all() -> List[{{cookiecutter.first_entity_name|capitalize}}]:
        return {{cookiecutter.first_entity_name|capitalize}}.query.all()

    @staticmethod
    def get_by_id({{cookiecutter.first_entity_name|lower}}_id: int) -> {{cookiecutter.first_entity_name|capitalize}}:
        return {{cookiecutter.first_entity_name|capitalize}}.query.get({{cookiecutter.first_entity_name|lower}}_id)

    @staticmethod
    def update({{cookiecutter.first_entity_name|lower}}: {{cookiecutter.first_entity_name|capitalize}}, {{cookiecutter.first_entity_name|lower}}_change_updates: {{cookiecutter.first_entity_name|capitalize}}Interface) -> {{cookiecutter.first_entity_name|capitalize}}:
        {{cookiecutter.first_entity_name|lower}}.update({{cookiecutter.first_entity_name|lower}}_change_updates)
        db.session.commit()
        return {{cookiecutter.first_entity_name|lower}}

    @staticmethod
    def delete_by_id({{cookiecutter.first_entity_name|lower}}_id: int) -> List[int]:
        {{cookiecutter.first_entity_name|lower}} = {{cookiecutter.first_entity_name|capitalize}}.query.filter({{cookiecutter.first_entity_name|capitalize}}.id == {{cookiecutter.first_entity_name|lower}}_id).first()
        if not {{cookiecutter.first_entity_name|lower}}:
            return []
        db.session.delete({{cookiecutter.first_entity_name|lower}})
        db.session.commit()
        return [{{cookiecutter.first_entity_name|lower}}_id]

    @staticmethod
    def create(new_attrs: {{cookiecutter.first_entity_name|capitalize}}Interface) -> {{cookiecutter.first_entity_name|capitalize}}:
        new_{{cookiecutter.first_entity_name|lower}} = {{cookiecutter.first_entity_name|capitalize}}(
            id=new_attrs["id"],
            name=new_attrs["name"],
            description=new_attrs["description"],
        )

        db.session.add(new_{{cookiecutter.first_entity_name|lower}})
        db.session.commit()

        return new_{{cookiecutter.first_entity_name|lower}}
