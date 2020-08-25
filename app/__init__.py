import sanic
from httpx import URL
from sanic import Sanic
from sanic_openapi import swagger_blueprint

from app import api
from app import db
from app.models.api_token import ApiToken
from app.models.user import User
from config import config


def register_listeners(app: Sanic):
    @app.listener("after_server_start")
    async def after_server_start(_, loop):
        print("after_server_start")
        db.pg.init(loop)
        await db.pg.connect(app.config["DB_SETTINGS"])

    @app.listener("before_server_stop")
    async def before_server_stop(_, loop):
        print("before_server_stop")
        await db.pg.close()


def register_middleware(app: Sanic):
    @app.middleware("request")
    async def add_current_user(request):
        user_token = request.args.get("token")
        if user_token:
            current_user = await User.load(
                api_tokens=ApiToken.on(User.id == ApiToken.user_id)
            ).gino.first()
            request.ctx.current_user = current_user


def register_routes(app: Sanic):
    app.blueprint(api.bp)
    app.blueprint(swagger_blueprint)


def create_app() -> sanic:
    app = Sanic(__name__)

    app.config.from_object(config)

    register_listeners(app)
    register_routes(app)
    register_middleware(app)
    # print(app.router.routes_all)
    return app
