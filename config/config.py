# app
import os

HOST = "0.0.0.0"
PORT = "3000"
DEBUG = True

# db
DB_SETTINGS = {
    "DB_HOST": "db" if os.getenv('ENV') == 'dev' else '127.0.0.1',
    "DB_PORT": "5432",
    "DB_DATABASE": "goodnight_development",
    "DB_USERNAME": "postgres",
    "DB_PASSWORD": "postgres",
    "DB_ECHO": True,
}

# picture
STATIC_PATH = "public"
NORMAL_PICTURE_PATH = f"{STATIC_PATH}/uploads/normal_picture/asset/"
