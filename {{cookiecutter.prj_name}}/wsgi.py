import os
from dotenv import load_dotenv
from app import create_app

load_dotenv()
env = os.getenv('FLASK_ENV') or 'test'
app = create_app(env)

if __name__ == '__main__':
    app.run(debug=(env in ('dev', 'test')))
