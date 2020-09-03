import os
import pprint

import sanic
from sanic import Sanic, response
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


def register_health_check(app: Sanic):
    @app.route("/api/health")
    async def health_check(requst):
        return response.json({"status": "OK"})


def create_app() -> sanic:
    app = Sanic(__name__)

    app.config.from_object(config)

    register_listeners(app)
    register_health_check(app)
    register_routes(app)
    return app
