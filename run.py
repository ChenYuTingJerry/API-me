import sys

from app import create_app
from config import config

app = create_app()

if __name__ == "__main__":
    app.run(host=config.HOST, port=config.PORT)

