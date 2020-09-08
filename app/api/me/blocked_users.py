import json
from dataclasses import asdict

from marshmallow import Schema, fields
from sanic import Blueprint, response

from app.model.picture import NormalPicture
from app.model.user import UserOtherUserBlockShip, User
from app.serializers.user import BlockUserSerializer

bp = Blueprint("me_block_users", url_prefix="/blocked_users")


class CreateBlockUserSchema(Schema):
    token = fields.String()
    blocked_user_id = fields.Int(required=True)


class GetBlockUserSchema(Schema):
    offset = fields.Int(required=True)
    limit = fields.Int(required=True)
    token = fields.String(required=True)
    device_system_name = fields.String()


create_block_user_schema = CreateBlockUserSchema()
get_block_user_schema = GetBlockUserSchema()


@bp.route("/", methods=["GET"])
async def get_block_users(request):
    current_user = request.ctx.current_user
    errors = get_block_user_schema.validate(request.args)
    if errors:
        return response.json(errors, status=422)
    limit = request.args.get("limit", 0)
    offset = request.args.get("offset", 0)
    users = (
        await User.load(
            User.id,
            User.name,
            User.gender,
            User.age,
            block_ship=UserOtherUserBlockShip.load(
                UserOtherUserBlockShip.user_id, UserOtherUserBlockShip.other_user_id
            ).on(User.id == UserOtherUserBlockShip.other_user_id),
            picture=NormalPicture.load(NormalPicture.asset, NormalPicture.id).on(
                NormalPicture.id == User.profile_picture_id
            ),
        )
        .where(UserOtherUserBlockShip.user_id == current_user.id)
        .limit(limit)
        .offset(offset)
        .gino.all()
    )

    blocked_users = tuple(
        map(lambda u: BlockUserSerializer(u, u.picture).to_dict(), users,)
    )
    return response.json(blocked_users)


@bp.route("/", methods=["POST"])
async def create_block_user(request):
    current_user = request.ctx.current_user
    request_body = json.loads(request.body)
    errors = create_block_user_schema.validate(request_body)
    if errors:
        return response.json(errors, status=422)
    blocked_user = (
        await UserOtherUserBlockShip.query.where(
            UserOtherUserBlockShip.user_id == current_user.id
        )
        .where(UserOtherUserBlockShip.other_user_id == request_body["blocked_user_id"])
        .gino.first()
    )

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
