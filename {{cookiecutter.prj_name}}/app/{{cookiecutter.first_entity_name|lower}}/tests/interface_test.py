from pytest import fixture

from app.{{cookiecutter.first_entity_name|lower}}.model import {{cookiecutter.first_entity_name|capitalize}}
from app.{{cookiecutter.first_entity_name|lower}}.interface import {{cookiecutter.first_entity_name|capitalize}}Interface


@fixture
def interface() -> {{cookiecutter.first_entity_name|capitalize}}Interface:

    params: {{cookiecutter.first_entity_name|capitalize}}Interface = {
        "id": 1,
        "name": "Test name",
        "description": "Test description",
    }
    return params


def test_{{cookiecutter.first_entity_name|capitalize}}Interface_create(interface: {{cookiecutter.first_entity_name|capitalize}}Interface):
    assert interface


def test_{{cookiecutter.first_entity_name|capitalize}}Interface_works(interface: {{cookiecutter.first_entity_name|capitalize}}Interface):
    assert {{cookiecutter.first_entity_name|capitalize}}(**interface)
