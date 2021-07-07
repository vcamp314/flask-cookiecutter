from flask_script import Command

from app import db
from app.{{cookiecutter.first_entity_name|lower}} import {{cookiecutter.first_entity_name|capitalize}}


def seed_things():
    classes = [{{cookiecutter.first_entity_name|capitalize}}]
    for klass in classes:
        seed_thing(klass)


def seed_thing(cls):
    things = [
        {"name": "Pizza Slicer", "description": "Cut delicious pizza"},
        {"name": "Rolling Pin", "description": "Roll delicious pizza"},
        {"name": "Pizza Oven", "description": "Bake delicious pizza"},
    ]
    db.session.bulk_insert_mappings(cls, things)


def seed_db():
    print('seeding..')
    seed_things()
    # add seeding logic here


class SeedCommand(Command):
    """ Seed the DB."""

    def run(self):
        if (
            input(
                "Are you sure you want to drop all tables and recreate? (y/N)\n"
            ).lower()
            == "y"
        ):
            print("Dropping tables...")
            db.drop_all()
            db.create_all()
            seed_db()
            db.session.commit()

            print("DB successfully seeded.")
