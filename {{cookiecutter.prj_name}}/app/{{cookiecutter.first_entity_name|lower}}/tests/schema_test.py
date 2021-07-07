from pytest import fixture

from app.{{cookiecutter.first_entity_name|lower}}.model import {{cookiecutter.first_entity_name|capitalize}}
from app.{{cookiecutter.first_entity_name|lower}}.schema import {{cookiecutter.first_entity_name|capitalize}}Schema
from app.{{cookiecutter.first_entity_name|lower}}.interface import {{cookiecutter.first_entity_name|capitalize}}Interface


@fixture
def schema() -> {{cookiecutter.first_entity_name|capitalize}}Schema:
    return {{cookiecutter.first_entity_name|capitalize}}Schema()


def test_{{cookiecutter.first_entity_name|capitalize}}Schema_create(schema: {{cookiecutter.first_entity_name|capitalize}}Schema):
    assert schema


def test_{{cookiecutter.first_entity_name|capitalize}}Schema_works(schema: {{cookiecutter.first_entity_name|capitalize}}Schema):
    params: {{cookiecutter.first_entity_name|capitalize}}Interface = schema.load(
        {"id": 1, "name": "Test name", "description": "Test description"}
    )
    {{cookiecutter.first_entity_name|lower}} = {{cookiecutter.first_entity_name|capitalize}}(**params)

    assert {{cookiecutter.first_entity_name|lower}}.id == 1
    assert {{cookiecutter.first_entity_name|lower}}.name == "Test name"
    assert {{cookiecutter.first_entity_name|lower}}.description == "Test description"
