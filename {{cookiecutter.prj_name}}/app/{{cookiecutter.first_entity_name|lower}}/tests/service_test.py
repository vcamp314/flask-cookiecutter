from app.test.fixtures import app, db  # noqa
from flask_sqlalchemy import SQLAlchemy

from typing import List
from app.{{cookiecutter.first_entity_name|lower}}.model import {{cookiecutter.first_entity_name|capitalize}}
from app.{{cookiecutter.first_entity_name|lower}}.service import {{cookiecutter.first_entity_name|capitalize}}Service  # noqa
from app.{{cookiecutter.first_entity_name|lower}}.interface import {{cookiecutter.first_entity_name|capitalize}}Interface


def test_get_all(db: SQLAlchemy):  # noqa
    yin: {{cookiecutter.first_entity_name|capitalize}} = {{cookiecutter.first_entity_name|capitalize}}(id=1, name="Yin", description="Test description")
    yang: {{cookiecutter.first_entity_name|capitalize}} = {{cookiecutter.first_entity_name|capitalize}}(id=2, name="Yaang", description="Test description")
    db.session.add(yin)
    db.session.add(yang)
    db.session.commit()

    results: List[{{cookiecutter.first_entity_name|capitalize}}] = {{cookiecutter.first_entity_name|capitalize}}Service.get_all()

    assert len(results) == 2
    assert yin in results and yang in results


def test_update(db: SQLAlchemy):  # noqa
    yin: {{cookiecutter.first_entity_name|capitalize}} = {{cookiecutter.first_entity_name|capitalize}}(id=1, name="Yin", description="Test description")

    db.session.add(yin)
    db.session.commit()
    updates = dict(name="Yang")

    {{cookiecutter.first_entity_name|capitalize}}Service.update(yin, updates)

    result: {{cookiecutter.first_entity_name|capitalize}} = {{cookiecutter.first_entity_name|capitalize}}.query.get(yin.id)
    assert result.name == "Yang"


def test_delete_by_id(db: SQLAlchemy):  # noqa
    yin: {{cookiecutter.first_entity_name|capitalize}} = {{cookiecutter.first_entity_name|capitalize}}(id=1, name="Yin", description="Test description")
    yang: {{cookiecutter.first_entity_name|capitalize}} = {{cookiecutter.first_entity_name|capitalize}}(id=2, name="Yang", description="Test description")
    db.session.add(yin)
    db.session.add(yang)
    db.session.commit()

    {{cookiecutter.first_entity_name|capitalize}}Service.delete_by_id(1)
    results: List[{{cookiecutter.first_entity_name|capitalize}}] = {{cookiecutter.first_entity_name|capitalize}}.query.all()

    assert len(results) == 1
    assert yin not in results and yang in results


def test_create(db: SQLAlchemy):  # noqa

    yin: {{cookiecutter.first_entity_name|capitalize}}Interface = {{cookiecutter.first_entity_name|capitalize}}Interface(
        id=1, name="Yin", description="Test description"
    )
    {{cookiecutter.first_entity_name|capitalize}}Service.create(yin)
    results: List[{{cookiecutter.first_entity_name|capitalize}}] = {{cookiecutter.first_entity_name|capitalize}}.query.all()

    assert len(results) == 1

    for k in yin.keys():
        assert getattr(results[0], k) == yin[k]
