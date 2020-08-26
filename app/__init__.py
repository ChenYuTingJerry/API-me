import sanic
from httpx import URL
from sanic import Sanic
from sanic_openapi import swagger_blueprint

from app import api
from app import db
from config import config


def register_listeners(app: Sanic):
    @app.listener("after_server_start")
    async def after_server_start(_, loop):
        db.pg.init(loop)
        await db.pg.connect(app.config["DB_SETTINGS"])

    @app.listener("before_server_stop")
    async def before_server_stop(_, loop):
        await db.pg.close()


def register_routes(app: Sanic):
    app.blueprint(api.bp)
    app.blueprint(swagger_blueprint)


def create_app() -> sanic:
    app = Sanic(__name__)

    app.config.from_object(config)

    register_listeners(app)
    register_routes(app)
    # print(app.router.routes_all)
    return app
