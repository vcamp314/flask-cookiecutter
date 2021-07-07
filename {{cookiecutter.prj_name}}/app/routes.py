def register_routes(api, app, root="api"):
    from app.{{cookiecutter.first_entity_name|lower}} import register_routes as attach_{{cookiecutter.first_entity_name|lower}}

    # Add routes
    attach_{{cookiecutter.first_entity_name|lower}}(api)
