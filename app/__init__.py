import os

import rollbar
import sanic
from sanic import Sanic, response
from sanic.handlers import ErrorHandler
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
    @app.route("/")
    async def health_check(request):
        return response.json({"status": "OK"})


def register_monitor(app: Sanic):
    class RollbarExceptionHandler(ErrorHandler):
        def default(self, request, exception):
            rollbar.report_exc_info(request=request)
            return super().default(request, exception)

    if os.getenv("ENV") == "prod":
        environment = "production"
    elif os.getenv("ENV") == "staging":
        environment = "staging"

    rollbar.init(os.getenv("ROLLBAR_ACCESS_TOKEN"), environment=environment)
    app.error_handler = RollbarExceptionHandler()


def create_app() -> sanic:
    app = Sanic(__name__)
    app.static("/", "./public")
    app.config.from_object(config)

    # register_monitor(app)
    register_listeners(app)
    register_health_check(app)
    register_routes(app)
    return app
