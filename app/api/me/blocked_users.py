import json
from dataclasses import asdict

from sanic import Blueprint, response

from app.models.user import UserOtherUserBlockShip, User
from app.serializers.user import BlockUserSerializer

bp = Blueprint("me_block_users", url_prefix="/blocked_users")


@bp.route("/", methods=["GET"])
async def get_block_users(request):
    current_user = request.ctx.current_user
    limit = request.args.get("limit")
    offset = request.args.get("offset")
    users = (
        await User.load(
            User.id,
            block_ship=UserOtherUserBlockShip.load(
                UserOtherUserBlockShip.user_id, UserOtherUserBlockShip.other_user_id
            ).on(User.id == UserOtherUserBlockShip.other_user_id),
        )
        .where(UserOtherUserBlockShip.user_id == current_user.id)
        .limit(limit)
        .offset(offset)
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
    current_user = request.ctx.current_user
    request_body = json.loads(request.body)
    blocked_user = await UserOtherUserBlockShip.query.where(
        UserOtherUserBlockShip.user_id == current_user.id
        and UserOtherUserBlockShip.other_user_id == request_body["blocked_user_id"]
    ).gino.first()

    if not blocked_user:
        await UserOtherUserBlockShip.create(
            user_id=current_user.id, other_user_id=request_body["blocked_user_id"]
        )
    return response.json({"success": True})


@bp.route("/<user_id:int>", methods=["DELETE"])
async def delete_block_user(request, user_id):
    current_user = request.ctx.current_user
    await UserOtherUserBlockShip.delete.where(
        UserOtherUserBlockShip.other_user_id == user_id
    ).where(UserOtherUserBlockShip.user_id == current_user.id).gino.status()

    return response.json({"success": True})
