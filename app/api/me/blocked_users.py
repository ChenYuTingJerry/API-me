from sanic import Blueprint, response

from app.models.users import User
from app.serializers.user import UserSerializer

bp = Blueprint("me_block_users", url_prefix="/blocked_users")


@bp.route("/", methods=["GET"])
async def get_block_users(request):
    users = await User.query.where(User.id < 10).gino.all()
    user_serializers = list(map(lambda u: UserSerializer(u).to_dict(), users))
    return response.json(user_serializers)


@bp.route("/", methods=["POST"])
async def create_block_user(request):
    return response.json({"jojo": 15})


@bp.route("/<id:int>", methods=["DELETE"])
async def create_block_user(request):
    return response.json({"jojo": 15})
