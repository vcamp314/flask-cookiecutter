from unittest.mock import patch
from flask.testing import FlaskClient
from flask.wrappers import Response

from app.test.fixtures import client, app  # noqa
from app.{{cookiecutter.first_entity_name|lower}}.model import {{cookiecutter.first_entity_name|capitalize}}
from app.{{cookiecutter.first_entity_name|lower}}.schema import {{cookiecutter.first_entity_name|capitalize}}Schema
from app.{{cookiecutter.first_entity_name|lower}}.service import {{cookiecutter.first_entity_name|capitalize}}Service
from app.{{cookiecutter.first_entity_name|lower}}.interface import {{cookiecutter.first_entity_name|capitalize}}Interface


def {{cookiecutter.first_entity_name|lower}}({{cookiecutter.first_entity_name|lower}}_id: int = 123, name: str = "Test name") -> {{cookiecutter.first_entity_name|capitalize}}:
    return {{cookiecutter.first_entity_name|capitalize}}(id={{cookiecutter.first_entity_name|lower}}_id, name=name, description="controller description")


class Test{{cookiecutter.first_entity_name|capitalize}}Resource:
    @patch.object({{cookiecutter.first_entity_name|capitalize}}Service, "get_all", lambda: [{{cookiecutter.first_entity_name|lower}}(123), {{cookiecutter.first_entity_name|lower}}(456)])
    def test_get(self, client: FlaskClient):  # noqa
        with client:
            results = client.get("/api/{{cookiecutter.first_entity_name|lower}}", follow_redirects=True).get_json()
            expected = {{cookiecutter.first_entity_name|capitalize}}Schema(many=True).dump([{{cookiecutter.first_entity_name|lower}}(456), {{cookiecutter.first_entity_name|lower}}(123)])
            for r in results:
                assert r in expected


class Test{{cookiecutter.first_entity_name|capitalize}}{{cookiecutter.first_entity_name|capitalize}}Resource:
    @patch.object(
        {{cookiecutter.first_entity_name|capitalize}}Service,
        "get_all",
        lambda: [{{cookiecutter.first_entity_name|lower}}(123, name="Test name 1"), {{cookiecutter.first_entity_name|lower}}(456, name="Test name 2")],
    )
    def test_get(self, client: FlaskClient):  # noqa
        with client:
            results: dict = client.get("/api/{{cookiecutter.first_entity_name|lower}}", follow_redirects=True).get_json()
            expected = (
                {{cookiecutter.first_entity_name|capitalize}}Schema(many=True)
                .dump([{{cookiecutter.first_entity_name|lower}}(123, name="Test name 1"), {{cookiecutter.first_entity_name|lower}}(456, name="Test name 2")])
            )
            for r in results:
                assert r in expected

    @patch.object(
        {{cookiecutter.first_entity_name|capitalize}}Service,
        "create",
        lambda create_request: {{cookiecutter.first_entity_name|capitalize}}(
            id=create_request.get("id"),
            name=create_request.get("name"),
            description=create_request.get("description"),
        ),
    )
    def test_post(self, client: FlaskClient):  # noqa
        with client:

            payload = dict(name="name", description="description")
            result: dict = client.post("/api/{{cookiecutter.first_entity_name|lower}}/", json=payload).get_json()
            expected = (
                {{cookiecutter.first_entity_name|capitalize}}Schema()
                .dump({{cookiecutter.first_entity_name|capitalize}}(name=payload["name"], description=payload["description"]))
            )
            print(expected)
            print(result)
            assert result == expected


def fake_update({{cookiecutter.first_entity_name|lower}}: {{cookiecutter.first_entity_name|capitalize}}, changes: {{cookiecutter.first_entity_name|capitalize}}Interface) -> {{cookiecutter.first_entity_name|capitalize}}:
    # To fake an update, just return a new object
    updated_{{cookiecutter.first_entity_name|lower}} = {{cookiecutter.first_entity_name|capitalize}}(id={{cookiecutter.first_entity_name|lower}}.id, name=changes["name"])
    return updated_{{cookiecutter.first_entity_name|lower}}


class Test{{cookiecutter.first_entity_name|capitalize}}IdResource:
    @patch.object({{cookiecutter.first_entity_name|capitalize}}Service, "get_by_id", lambda id: {{cookiecutter.first_entity_name|capitalize}}(id=id))
    def test_get(self, client: FlaskClient):  # noqa
        with client:
            result: dict = client.get("/api/{{cookiecutter.first_entity_name|lower}}/123").get_json()
            expected = {{cookiecutter.first_entity_name|capitalize}}(id=123)
            assert result["id"] == expected.id

    @patch.object({{cookiecutter.first_entity_name|capitalize}}Service, "delete_by_id", lambda id: [id])
    def test_delete(self, client: FlaskClient):  # noqa
        with client:
            result: dict = client.delete("/api/{{cookiecutter.first_entity_name|lower}}/123").get_json()
            expected = dict(status="Success", id=[123])
            assert result == expected

    @patch.object({{cookiecutter.first_entity_name|capitalize}}Service, "get_by_id", lambda id: {{cookiecutter.first_entity_name|capitalize}}(id=id))
    @patch.object({{cookiecutter.first_entity_name|capitalize}}Service, "update", fake_update)
    def test_put(self, client: FlaskClient):  # noqa
        with client:
            result: dict = client.put(
                "/api/{{cookiecutter.first_entity_name|lower}}/123", json={"name": "New name"}
            ).get_json()
            expected: dict = {{cookiecutter.first_entity_name|capitalize}}Schema().dump(
                {{cookiecutter.first_entity_name|capitalize}}(id=123, name="New name")
            )
            assert result == expected
