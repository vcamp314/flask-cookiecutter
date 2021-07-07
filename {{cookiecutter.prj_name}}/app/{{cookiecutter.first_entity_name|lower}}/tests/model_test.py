from pytest import fixture
from flask_sqlalchemy import SQLAlchemy

from app.test.fixtures import app, db  # noqa
from app.{{cookiecutter.first_entity_name|lower}}.model import {{cookiecutter.first_entity_name|capitalize}}


@fixture
def {{cookiecutter.first_entity_name|lower}}() -> {{cookiecutter.first_entity_name|capitalize}}:
    return {{cookiecutter.first_entity_name|capitalize}}(id=1, name="Test name", description="Test description")


def test_{{cookiecutter.first_entity_name|capitalize}}_create({{cookiecutter.first_entity_name|lower}}: {{cookiecutter.first_entity_name|capitalize}}):
    assert {{cookiecutter.first_entity_name|lower}}


def test_{{cookiecutter.first_entity_name|capitalize}}_retrieve({{cookiecutter.first_entity_name|lower}}: {{cookiecutter.first_entity_name|capitalize}}, db: SQLAlchemy):  # noqa
    db.session.add({{cookiecutter.first_entity_name|lower}})
    db.session.commit()
    s = {{cookiecutter.first_entity_name|capitalize}}.query.first()
    assert s.__dict__ == {{cookiecutter.first_entity_name|lower}}.__dict__
