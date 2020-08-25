from dataclasses import asdict

from sanic import Blueprint, response

from app.models.user import UserOtherUserBlockShip, User
from app.serializers.user import BlockUserSerializer

bp = Blueprint("me_block_users", url_prefix="/blocked_users")


@bp.route("/", methods=["GET"])
async def get_block_users(request):
    current_user = request.ctx.current_user
    users = (
        await User.load(
            block_ships=UserOtherUserBlockShip.on(
                User.id == UserOtherUserBlockShip.other_user_id
            )
        )
        .where(UserOtherUserBlockShip.user_id == current_user.id)
        .gino.all()
    )
    blocked_users = list(
        map(
            lambda u: asdict(
                BlockUserSerializer(id=u.id, name=u.name, gender=u.gender, age=u.age,)
            ),
            users,
        )
    )
    return response.json(blocked_users)


@bp.route("/", methods=["POST"])
async def create_block_user(request):
    pass
    # return response.json(user_serializers)


@bp.route("/<id:int>", methods=["DELETE"])
async def create_block_user(request):
    return response.json({"jojo": 15})
