from sanic import Blueprint

from ..models.api_token import ApiToken
from ..models.user import User
from ..utils import dynamic

modules = dynamic.import_submodules(__name__, __file__)
blueprints = map(lambda m: m.bp, modules)
bp = Blueprint.group(*blueprints, url_prefix="/api/v2")


@bp.middleware("request")
async def add_current_user(request):
    user_token = request.args.get("token")
    if user_token:
        current_user = await User.load(
            User.id,
            User.name,
            api_token=ApiToken.load(ApiToken.id).on(User.id == ApiToken.user_id),
        ).gino.first()
        request.ctx.current_user = current_user
